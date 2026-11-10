"""Química exacta para «Química con juegos» (Leo Vallmar). Python 3.8 o posterior, sin instalar nada.

Lo que hace este módulo, siempre con cuentas exactas (fracciones y decimales), nunca con un modelo de lenguaje:
- lee fórmulas («Ca(OH)2», «Fe^3+», «SO₄²⁻») y cuenta los átomos de cada elemento y la carga;
- lee ecuaciones («2 H2 + O2 -> 2 H2O»), cuenta átomos y cargas a cada lado y dice si están ajustadas;
- ajusta ecuaciones resolviendo un sistema lineal con fracciones: da los coeficientes enteros más pequeños y avisa si el
  ajuste no es único;
- calcula masas moleculares con la tabla de elementos.py, redondeando a los decimales del dato menos preciso;
- nombra y formula compuestos binarios (Stock y prefijos) con reglas, y vuelve del nombre a la fórmula.
"""
from __future__ import annotations

import re
from collections import Counter
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import reduce
from math import gcd

from elementos import ELEMENTOS, MASAS

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")
DESUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻−", "0123456789" "0123456789" "+--")


class ErrorQuimico(ValueError):
    pass


# ================================================================ números en español


def _miles(ent):
    return ent if len(ent) <= 4 else f"{int(ent):,}".replace(",", " ")


def numero(x, nd=None, cifras=3):
    """«18,015», «0,0456», «12 346»: coma decimal y sin ceros finales. `nd` = decimales fijos; si no, `cifras` significativas."""
    d = Decimal(str(x))
    if nd is None:
        if d == 0:
            return "0"
        exp = d.adjusted()
        nd = max(0, cifras - 1 - exp)
        q = d.quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)
        ent, _, dec = format(abs(q), "f").partition(".")       # cifras significativas: se conservan los ceros finales
    else:
        q = d.quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)
        ent, _, dec = format(abs(q), "f").partition(".")
    s = _miles(ent) + ("," + dec if dec else "")
    return ("−" if q < 0 and s.strip("0,") else "") + s


def signo(x):
    """«+2», «−3», «0» con el signo menos tipográfico."""
    return "0" if x == 0 else (f"+{x}" if x > 0 else f"−{-x}")


def cientifico(x, cifras=4):
    """«6,022 · 10²³». Para números de 0,01 a 99 999 devuelve el número normal."""
    x = float(x)
    if x == 0 or 1e-2 <= abs(x) < 1e5:
        return numero(x, cifras=cifras)
    from math import floor, log10
    k = floor(log10(abs(x)))
    m = Decimal(repr(x / 10 ** k)).quantize(Decimal(1).scaleb(-(cifras - 1)), rounding=ROUND_HALF_UP)
    if abs(m) >= 10:
        m, k = m / 10, k + 1
    return f"{numero(m, cifras=cifras)} · 10{str(k).translate(SUP)}"


def leer_numero(t):
    """«18,02», «6,022 · 10^23», «6,022·10²³», «1.5e3» → float."""
    t = t.strip().translate(DESUB).replace(" ", "").replace("×", "·").replace("x10", "·10").replace("*10", "·10")
    m = re.fullmatch(r"([+-]?\d+(?:[.,]\d+)?)(?:·10\^?([+-]?\d+)|[eE]([+-]?\d+))?", t)
    if not m:
        raise ValueError(f"«{t}» no es un número")
    base = float(m.group(1).replace(",", "."))
    exp = m.group(2) or m.group(3)
    return base * 10 ** int(exp) if exp else base


# ================================================================ fórmulas


TOKEN = re.compile(r"([A-Z][a-z]?)(\d*)|(\()|(\))(\d*)")


def separar_carga(f):
    """«Fe^3+» / «Fe3+» al final con ^ / «SO₄²⁻» / «Na+» → («Fe», 3). Sin carga → (f, 0)."""
    s = f.strip().translate(DESUB).replace(" ", "")
    m = re.fullmatch(r"(.+?)\^(\d*)([+-])", s)
    if m:
        n = int(m.group(2) or 1)
        return m.group(1), n if m.group(3) == "+" else -n
    m = re.fullmatch(r"(.*[A-Za-z)\]])([+-])", s)
    if m:
        return m.group(1), 1 if m.group(2) == "+" else -1
    return s, 0


def _carga_sup(f):
    """Para leer «SO₄²⁻» hace falta distinguir subíndice y superíndice: se hace antes de traducirlos."""
    m = re.fullmatch(r"(.*?)([⁰¹²³⁴⁵⁶⁷⁸⁹]*)([⁺⁻])", f.strip())
    if m:
        n = int(m.group(2).translate(DESUB) or 1)
        return m.group(1).translate(DESUB), n if m.group(3) == "⁺" else -n
    return None


def pista_formula(f):
    """Ayuda para el error más común al escribir en la consola: cargas sin «^» o símbolos en minúscula."""
    s = f.strip()
    if re.search(r"\d[+-]$", s) and "^" not in s:
        return ". Las cargas se escriben con ^ delante: Fe^3+, SO4^2-, NH4^+ (con una sola carga vale Na+ o Cl-)"
    if re.match(r"[a-z]", s):
        return ". Cada símbolo empieza por mayúscula: H2O, no h2o"
    if " " in s:
        return ". Escribe la fórmula sin espacios, entre comillas: \"Ca(OH)2\""
    return ""


def atomos(f):
    """Átomos de cada elemento de una fórmula (Counter) y su carga: atomos("Ca(OH)2") → (Counter({'O': 2, 'H': 2, 'Ca': 1}), 0)."""
    sup = _carga_sup(f)
    base, carga = sup if sup else separar_carga(f)
    pila = [Counter()]
    pos = 0
    while pos < len(base):
        m = TOKEN.match(base, pos)
        if not m:
            raise ErrorQuimico(f"no entiendo la fórmula «{f}» (posición {pos + 1})" + pista_formula(f))
        sim, n, abre, cierra, n2 = m.groups()
        if sim:
            if sim not in ELEMENTOS:
                raise ErrorQuimico(f"«{sim}» no es un elemento de la tabla del libro")
            pila[-1][sim] += int(n or 1)
        elif abre:
            pila.append(Counter())
        else:
            if len(pila) == 1:
                raise ErrorQuimico(f"paréntesis sin abrir en «{f}»")
            grupo = pila.pop()
            for k, v in grupo.items():
                pila[-1][k] += v * int(n2 or 1)
        pos = m.end()
    if len(pila) != 1 or not pila[0]:
        raise ErrorQuimico(f"fórmula incompleta «{f}»")
    return pila[0], carga


def bonita(f):
    """«Ca(OH)2» → «Ca(OH)₂»; «Fe^3+» → «Fe³⁺»; «SO4^2-» → «SO₄²⁻»."""
    sup = _carga_sup(f)
    base, carga = sup if sup else separar_carga(f)
    t = re.sub(r"(?<=[A-Za-z)])(\d+)", lambda m: m.group(1).translate(SUB), base)
    if carga:
        t += (str(abs(carga)) if abs(carga) > 1 else "").translate(SUP) + ("⁺" if carga > 0 else "⁻")
    return t


def simple(f):
    """Forma ASCII canónica: «Ca(OH)₂» → «Ca(OH)2», «Fe³⁺» → «Fe^3+»."""
    sup = _carga_sup(f)
    base, carga = sup if sup else separar_carga(f)
    return base + (f"^{abs(carga) if abs(carga) > 1 else ''}{'+' if carga > 0 else '-'}" if carga else "")


def misma_formula(a, b):
    """Dos fórmulas escritas igual (mismos átomos en el mismo orden de escritura y misma carga)."""
    try:
        return simple(a).replace(" ", "") == simple(b).replace(" ", "")
    except ErrorQuimico:
        return False


# ================================================================ ecuaciones

FLECHA = re.compile(r"\s*(?:->|→|=>|=)\s*")


def leer_ecuacion(e):
    """«2 H2 + O2 -> 2 H2O» → ([(2, 'H2'), (1, 'O2')], [(2, 'H2O')]). Los coeficientes que faltan valen 1."""
    partes = FLECHA.split(e.strip())
    if len(partes) != 2:
        raise ErrorQuimico("la ecuación necesita una flecha «->» entre reactivos y productos")

    def lado(t):
        out = []
        for trozo in re.split(r"\s+\+\s+|\s*\+\s*(?=\d*\s*[A-Z(])", t.strip()):
            trozo = trozo.strip()
            m = re.fullmatch(r"(\d+)?\s*(.+)", trozo)
            if not m or not m.group(2):
                raise ErrorQuimico(f"no entiendo «{trozo}»")
            out.append((int(m.group(1) or 1), m.group(2).strip()))
        return out
    return lado(partes[0]), lado(partes[1])


def recuento(lado):
    """Átomos de cada elemento y carga total de un lado de la ecuación."""
    c, q = Counter(), 0
    for k, f in lado:
        a, carga = atomos(f)
        for el, n in a.items():
            c[el] += k * n
        q += k * carga
    return c, q


def orden_elementos(izq, der):
    vistos = []
    for lado in (izq, der):
        for _, f in lado:
            for m in re.finditer(r"[A-Z][a-z]?", separar_carga(f)[0].translate(DESUB)):
                if m.group(0) not in vistos:
                    vistos.append(m.group(0))
    return vistos


def comprobar_ecuacion(e):
    """{'ajustada': bool, 'izquierda': {...}, 'derecha': {...}, 'carga': (qi, qd), 'falla': [elementos que no cuadran]}."""
    izq, der = leer_ecuacion(e) if isinstance(e, str) else e
    ci, qi = recuento(izq)
    cd, qd = recuento(der)
    orden = orden_elementos(izq, der)
    falla = [el for el in orden if ci[el] != cd[el]]
    if qi != qd:
        falla.append("carga")
    return {"ajustada": not falla, "izquierda": {el: ci[el] for el in orden}, "derecha": {el: cd[el] for el in orden},
            "carga": (qi, qd), "falla": falla, "orden": orden}


def escribir_ecuacion(izq, der, bonito=True):
    f = bonita if bonito else (lambda x: x)

    def lado(xs):
        return " + ".join((f"{k} " if k != 1 else "") + f(s) for k, s in xs)
    return f"{lado(izq)} {'→' if bonito else '->'} {lado(der)}"


def _rref_nulo(filas, ncols):
    """Base del núcleo de una matriz de enteros con fracciones exactas (eliminación de Gauss-Jordan)."""
    M = [[Fraction(x) for x in fila] for fila in filas]
    pivotes, r = [], 0
    for col in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        p = M[r][col]
        M[r] = [x / p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                fct = M[i][col]
                M[i] = [a - fct * b for a, b in zip(M[i], M[r])]
        pivotes.append(col)
        r += 1
        if r == len(M):
            break
    libres = [c for c in range(ncols) if c not in pivotes]
    base = []
    for fl in libres:
        v = [Fraction(0)] * ncols
        v[fl] = Fraction(1)
        for i, pc in enumerate(pivotes):
            v[pc] = -M[i][fl]
        base.append(v)
    return base


def ajustar(reactivos, productos):
    """Coeficientes enteros más pequeños que conservan átomos y carga. Lanza ErrorQuimico si no hay ajuste o no es único."""
    especies = list(reactivos) + list(productos)
    datos = [atomos(f) for f in especies]
    elementos = sorted({el for a, _ in datos for el in a})
    filas = []
    for el in elementos:
        filas.append([a[el] * (1 if i < len(reactivos) else -1) for i, (a, _) in enumerate(datos)])
    if any(q for _, q in datos):
        filas.append([q * (1 if i < len(reactivos) else -1) for i, (_, q) in enumerate(datos)])
    base = _rref_nulo(filas, len(especies))
    if len(base) != 1:
        raise ErrorQuimico("la ecuación no tiene un ajuste único" if base else "la ecuación no se puede ajustar")
    v = base[0]
    if all(x <= 0 for x in v):
        v = [-x for x in v]
    if any(x <= 0 for x in v):
        raise ErrorQuimico("el ajuste exige un coeficiente cero o negativo: revisa reactivos y productos")
    mcm = reduce(lambda a, b: a * b // gcd(a, b), (x.denominator for x in v), 1)
    ent = [int(x * mcm) for x in v]
    g = reduce(gcd, ent)
    ent = [x // g for x in ent]
    return ent[:len(reactivos)], ent[len(reactivos):]


# ================================================================ masas


def decimales(d: Decimal) -> int:
    return max(0, -d.as_tuple().exponent)


def masa_molecular(f):
    """(masa redondeada a los decimales del dato menos preciso, términos [(n, símbolo, masa)], suma exacta)."""
    a, _ = atomos(f)
    orden = []
    for m in re.finditer(r"[A-Z][a-z]?", separar_carga(f)[0].translate(DESUB)):
        if m.group(0) not in orden:
            orden.append(m.group(0))
    terminos = [(a[el], el, MASAS[el]) for el in orden]
    exacta = sum((n * m for n, _, m in terminos), Decimal(0))
    nd = min(decimales(m) for _, _, m in terminos)
    return exacta.quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP), terminos, exacta


METAL = {s for s, e in ELEMENTOS.items() if e["tipo"] == "metal"}


def es_ionica(f):
    """True si la fórmula es de un compuesto iónico: lleva un metal, o el ion amonio (NH₄) junto con otro grupo o elemento.
    Así se decide el nombre de su masa: masa de la unidad fórmula (iónicos) o masa molecular (moleculares)."""
    a, _ = atomos(f)
    if any(el in METAL for el in a):
        return True
    base = separar_carga(f.translate(DESUB))[0] if not _carga_sup(f) else _carga_sup(f)[0]
    return "NH4" in base and base.replace("(NH4)", "").replace("NH4", "") != ""


def magnitud_masa(f):
    """«masa de la unidad fórmula» para un compuesto iónico; «masa molecular» para una sustancia molecular."""
    return "masa de la unidad fórmula" if es_ionica(f) else "masa molecular"


def texto_masa(f, unidad="u", terminos=None, resultado=None):
    """«M(H₂O) = 2 · 1,008 + 15,999 = 18,015 u» (el texto que imprime el libro)."""
    m, t, _ = masa_molecular(f)
    t = terminos or t
    m = resultado if resultado is not None else m
    if len(t) == 1 and t[0][0] == 1 and terminos is None:
        return f"M({bonita(f)}) = {numero(m, nd=decimales(m))} {unidad}"
    partes = " + ".join((f"{n} · " if n != 1 else "") + numero(ms, nd=decimales(ms)) for n, _, ms in t)
    return f"M({bonita(f)}) = {partes} = {numero(m, nd=decimales(m))} {unidad}"


MASA_TXT = re.compile(r"M\(((?:[A-Za-z₀-₉]|\([A-Za-z₀-₉]+\)[₀-₉]*)+)\) = ([0-9 ·,+]+?) = ([0-9 ,]+?) (u|g/mol)")


def revisar_textos_masa(texto):
    """Busca cada «M(X) = términos = resultado» de un texto y lo recalcula con la tabla: lista de problemas (vacía = bien)."""
    p = []
    for m in MASA_TXT.finditer(texto):
        f, terms, res = m.group(1), m.group(2), m.group(3)
        try:
            bien, t, _ = masa_molecular(f)
        except ErrorQuimico as e:
            p.append(f"«{m.group(0)}»: {e}")
            continue
        esperado = " + ".join((f"{n} · " if n != 1 else "") + numero(ms, nd=decimales(ms)) for n, _, ms in t)
        if terms.strip() != esperado:
            p.append(f"«{m.group(0)}»: los términos no son los de la tabla ({esperado})")
        if Decimal(res.replace(" ", "").replace(",", ".")) != bien:
            p.append(f"«{m.group(0)}»: la suma no es {numero(bien, nd=decimales(bien))}")
    return p


# ================================================================ partículas


def particulas(simbolo, A, carga=0):
    Z = ELEMENTOS[simbolo]["Z"]
    if A < Z:
        raise ErrorQuimico(f"un núcleo de {simbolo} no puede tener número másico {A}")
    return {"protones": Z, "neutrones": A - Z, "electrones": Z - carga}


# ================================================================ nomenclatura de compuestos binarios

ROMANOS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII"}
DE_ROMANO = {v: k for k, v in ROMANOS.items()}
PREFIJOS = {1: "mono", 2: "di", 3: "tri", 4: "tetra", 5: "penta", 6: "hexa", 7: "hepta"}
DE_PREFIJO = {v: k for k, v in PREFIJOS.items()}
# Aniones monoatómicos (raíz del nombre y carga) que usa el libro.
ANIONES = {"H": ("hidruro", -1), "F": ("fluoruro", -1), "Cl": ("cloruro", -1), "Br": ("bromuro", -1), "I": ("yoduro", -1),
           "O": ("óxido", -2), "S": ("sulfuro", -2), "N": ("nitruro", -3)}
DE_ANION = {v[0]: k for k, v in ANIONES.items()}
# Números de oxidación positivos que usa el libro (los metales de valencia variable llevan número romano en Stock).
POSITIVOS = {"Li": [1], "Na": [1], "K": [1], "Ag": [1], "Be": [2], "Mg": [2], "Ca": [2], "Ba": [2], "Zn": [2], "Al": [3],
             "Fe": [2, 3], "Cu": [1, 2], "Pb": [2, 4], "H": [1], "C": [2, 4], "S": [4, 6], "N": [3, 4, 5], "P": [3, 5],
             "Si": [4], "B": [3]}
METALES_NOMBRE = {s: ELEMENTOS[s]["nombre"] for s in POSITIVOS}
DE_NOMBRE = {v: k for k, v in METALES_NOMBRE.items()}


def ion_nombre(simbolo, carga):
    """Na⁺ → «ion sodio»; Fe³⁺ → «ion hierro(III)»; Cl⁻ → «ion cloruro»."""
    if carga < 0:
        raiz, q = ANIONES[simbolo]
        if q != carga:
            raise ErrorQuimico(f"el libro solo usa {simbolo} con carga {q}")
        return f"ion {raiz}"
    if carga not in POSITIVOS.get(simbolo, []):
        raise ErrorQuimico(f"el libro no usa {simbolo} con carga +{carga}")
    nombre = ELEMENTOS[simbolo]["nombre"]
    return f"ion {nombre}" + (f"({ROMANOS[carga]})" if len(POSITIVOS[simbolo]) > 1 else "")


def subindices(q_pos, q_neg):
    """Cargas +a y −b → subíndices (b, a) simplificados para que la suma de cargas sea cero."""
    a, b = q_pos, -q_neg
    g = gcd(a, b)
    return b // g, a // g


def formula_binaria(pos, n_pos, neg, n_neg):
    return f"{pos}{n_pos if n_pos > 1 else ''}{neg}{n_neg if n_neg > 1 else ''}"


def componer(pos, carga_pos, neg):
    """Fórmula del compuesto neutro de un catión (o elemento con número de oxidación positivo) y un anión del libro."""
    q_neg = ANIONES[neg][1]
    if carga_pos not in POSITIVOS.get(pos, []):
        raise ErrorQuimico(f"el libro no usa {pos} con +{carga_pos}")
    n_pos, n_neg = subindices(carga_pos, q_neg)
    return formula_binaria(pos, n_pos, neg, n_neg)


def descomponer(f):
    """«Fe2O3» → ('Fe', 2, 'O', 3). Solo compuestos binarios con el elemento positivo delante."""
    m = re.fullmatch(r"([A-Z][a-z]?)(\d*)([A-Z][a-z]?)(\d*)", simple(f))
    if not m:
        raise ErrorQuimico(f"«{f}» no es un compuesto binario de los del libro")
    pos, n1, neg, n2 = m.group(1), int(m.group(2) or 1), m.group(3), int(m.group(4) or 1)
    if neg not in ANIONES or pos not in POSITIVOS or pos == neg:
        raise ErrorQuimico(f"«{f}» no es un compuesto binario de los del libro")
    return pos, n1, neg, n2


def numero_oxidacion(f):
    """Número de oxidación del elemento positivo: el negativo actúa con la carga de su anión y la suma es cero."""
    pos, n1, neg, n2 = descomponer(f)
    total = -ANIONES[neg][1] * n2
    if total % n1:
        raise ErrorQuimico(f"en «{f}» las cargas no pueden sumar cero")
    q = total // n1
    if q not in POSITIVOS[pos]:
        raise ErrorQuimico(f"en «{f}» el {ELEMENTOS[pos]['nombre']} actuaría con +{q}, que el libro no usa")
    if componer(pos, q, neg) != simple(f):
        raise ErrorQuimico(f"«{f}» no está simplificada: los subíndices tienen un divisor común")
    return q


def variable(pos):
    return len(POSITIVOS[pos]) > 1


def _pref(n, raiz, usar_mono):
    if n == 1 and not usar_mono:
        return raiz
    p = PREFIJOS[n]
    if raiz.startswith("ó") and p == "mono":
        return "monóxido"
    return p + raiz


def nombres(f):
    """{'stock': nombre o None, 'prefijos': nombre, 'acepta': [nombres correctos]} de un compuesto binario."""
    pos, n1, neg, n2 = descomponer(f)
    q = numero_oxidacion(f)
    raiz = ANIONES[neg][0]
    el = ELEMENTOS[pos]["nombre"]
    metal = ELEMENTOS[pos]["tipo"] == "metal"
    stock = None
    if metal:
        stock = f"{raiz} de {el}" + (f"({ROMANOS[q]})" if variable(pos) else "")
    elif pos == "H":
        stock = f"{raiz} de hidrógeno"
    mono = variable(pos)
    pref = f"{_pref(n2, raiz, mono)} de {_pref(n1, el, False)}"
    acepta = {pref, pref.replace("monóxido", "monoóxido")}
    if not metal and pos != "H" and mono:
        acepta.add(f"{raiz} de {el}({ROMANOS[q]})")         # Stock de un no metal: «óxido de azufre(VI)»
    if not mono:
        acepta.add(f"{raiz} de {el}")                       # «cloruro de calcio» también es correcto para CaCl₂
    if stock:
        acepta.add(stock)
    acepta |= {x.replace("aó", "ó").replace("oó", "ó") for x in list(acepta)}   # «pentóxido» además de «pentaóxido»
    return {"stock": stock, "prefijos": pref, "acepta": sorted(acepta)}


def normalizar_nombre(t):
    t = t.strip().lower().replace("( ", "(").replace(" )", ")")
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\s*\(\s*", "(", t)
    return t


PREF_RE = "|".join(sorted(DE_PREFIJO, key=len, reverse=True))


def formula_de_nombre(nombre):
    """Del nombre (Stock o prefijos) a la fórmula: «óxido de hierro(III)» → «Fe2O3»; «trióxido de dihierro» → «Fe2O3»."""
    t = normalizar_nombre(nombre)
    t = t.replace("monóxido", "monoóxido").replace("pentóxido", "pentaóxido").replace("hexóxido", "hexaóxido").replace(
        "heptóxido", "heptaóxido").replace("tetróxido", "tetraóxido")
    m = re.fullmatch(rf"(?:(?P<p1>{PREF_RE}))?(?P<raiz>\w+?) de (?:(?P<p2>{PREF_RE}))?(?P<el>[a-záéíóúñ]+)(?:\((?P<rom>[ivx]+)\))?", t)
    if not m:
        raise ErrorQuimico(f"no entiendo el nombre «{nombre}»")
    raiz, el = m.group("raiz"), m.group("el")
    if raiz not in DE_ANION:
        raise ErrorQuimico(f"«{raiz}» no es un anión del libro")
    if el not in DE_NOMBRE:
        if m.group("p2") and (m.group("p2") + el) in DE_NOMBRE:
            el = m.group("p2") + el
        else:
            raise ErrorQuimico(f"«{el}» no es un elemento de los compuestos del libro")
    neg, pos = DE_ANION[raiz], DE_NOMBRE[el]
    p1, p2, rom = m.group("p1"), m.group("p2"), m.group("rom")
    if p1 or p2:
        if rom:
            raise ErrorQuimico("un nombre no lleva a la vez prefijos y número romano")
        n_neg, n_pos = DE_PREFIJO.get(p1, 1), DE_PREFIJO.get(p2, 1)
        f = formula_binaria(pos, n_pos, neg, n_neg)
        numero_oxidacion(f)
        return f
    if rom:
        q = DE_ROMANO.get(rom.upper())
        if q is None:
            raise ErrorQuimico(f"número romano «{rom}» no válido")
        return componer(pos, q, neg)
    if len(POSITIVOS[pos]) > 1:
        raise ErrorQuimico(f"«{nombre}» es ambiguo: el {el} puede actuar con " + " o ".join(f"+{x}" for x in POSITIVOS[pos]))
    return componer(pos, POSITIVOS[pos][0], neg)


def nombre_correcto(dado, f):
    """¿El nombre dado corresponde a la fórmula? (Se comprueba volviendo a la fórmula, no comparando cadenas.)"""
    try:
        return misma_formula(formula_de_nombre(dado), f)
    except ErrorQuimico:
        return False
