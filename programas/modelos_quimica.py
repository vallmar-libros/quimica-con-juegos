"""Modelos de «Química con juegos» (Leo Vallmar): cada reto se resuelve con una cadena de pasos calculados con quimica.py.

Las soluciones del libro salen de aquí. Cada paso guarda su valor y, cuando se puede, una comprobación independiente
(una ecuación que debe estar ajustada, una masa que debe salir de la tabla, un nombre que debe volver a su fórmula). El
«detective de la IA» usa `error = {"paso": k, "tipo": t}` para meter a propósito un fallo en el paso k: los pasos
siguientes arrastran el valor equivocado. Solo usa la biblioteca estándar de Python 3.8 o posterior.
"""
from __future__ import annotations

import re
from decimal import Decimal

import quimica as Q
from elementos import AVOGADRO_LIBRO, ELEMENTOS, ION_COMUN

numero, bonita, signo = Q.numero, Q.bonita, Q.signo


class ErrorDeModelo(ValueError):
    pass


def pl(n, sing, plur):
    return f"{n} {sing if n == 1 else plur}"


def letra(i):
    return chr(97 + i) + ")"


def _q(x):
    return float(x)


class Sol:
    """Pasos y respuestas de una solución. `toca(k, tipo)` dice si el error inyectado cae en el paso k."""

    def __init__(self, error=None):
        self.pasos, self.respuestas = [], []
        self.error = error
        self.error_info = None

    def siguiente(self):
        return len(self.pasos) + 1

    def toca(self, tipo):
        e = self.error
        return bool(e) and e["paso"] == self.siguiente() and e["tipo"] == tipo

    def marcar(self, explica):
        self.error_info = {"paso": self.siguiente(), "explica": explica}

    def paso(self, texto, valor, chequeo=None):
        self.pasos.append({"n": self.siguiente(), "texto": texto, "valor": valor, "chequeo": chequeo})

    def resp(self, etiqueta, texto, valor, tipo, unidad="", formula=None):
        self.respuestas.append({"etiqueta": etiqueta, "texto": texto, "valor": valor, "tipo": tipo, "unidad": unidad,
                                "formula": formula})

    def texto(self):
        pasos = " ".join(f"({p['n']}) {p['texto']}" for p in self.pasos)
        resp = "; ".join(f"{r['etiqueta']} {r['texto']}" if r["etiqueta"] else r["texto"] for r in self.respuestas)
        return f"{pasos} Respuesta: {resp}."


def comprobar_chequeo(ch):
    """True si la comprobación independiente de un paso se cumple (None si el paso no tiene)."""
    if not ch:
        return None
    t = ch["tipo"]
    if t == "ecuacion":
        return Q.comprobar_ecuacion(ch["ecuacion"])["ajustada"]
    if t == "masa":
        return not Q.revisar_textos_masa(ch["texto"])
    if t == "nombre":
        return Q.nombre_correcto(ch["nombre"], ch["formula"])
    if t == "neutra":
        a, q = Q.atomos(ch["formula"])
        return q == 0 and sum(ch["cargas"][el] * n for el, n in a.items()) == 0
    if t == "particulas":
        return Q.particulas(ch["simbolo"], ch["A"], ch["carga"]) == ch["valores"]
    if t == "cuenta":
        return abs(ch["calculado"] - ch["esperado"]) <= 1e-9 * max(1, abs(ch["esperado"]))
    raise ErrorDeModelo(f"comprobación desconocida {t}")


def lista_y(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " y " + xs[-1]


def recuento_txt(c):
    return ", ".join(f"{el} {n}" for el, n in c.items())


# ================================================================ 1. contar átomos


def r_contar(s, d):
    for i, f in enumerate(d["formulas"]):
        a, _ = Q.atomos(f)
        orden = Q.orden_elementos([(1, f)], [])
        partes = [f"{a[el]} de {el}" for el in orden]
        total = sum(a.values())
        if s.toca("parentesis") and "(" in f:
            plano = Q.atomos(f.split("(")[0] + f.split("(")[1].split(")")[0])[0]
            total_mal = sum(plano.values())
            sub = re.search(r"\)(\d*)", f).group(1) or "1"
            s.marcar(f"el chat ha ignorado el subíndice {sub} que va detrás del paréntesis de {bonita(f)}: ese {sub} multiplica todo lo "
                     f"de dentro, así que hay " + lista_y(partes) + f": {total} átomos")
            s.paso(f"{bonita(f)}: " + lista_y([f"{plano[el]} de {el}" for el in orden]) + f"; en total, {total_mal} átomos.",
                   total_mal, {"tipo": "cuenta", "calculado": total_mal, "esperado": total})
            total = total_mal
        else:
            s.paso(f"{bonita(f)}: " + lista_y(partes) + f"; en total, {total} átomos.", total,
                   {"tipo": "cuenta", "calculado": total, "esperado": sum(a.values())})
        s.resp(f"{letra(i)} {bonita(f)}:", f"{total} átomos", total, "numero", "átomos")


# ================================================================ 2. partículas de átomos, iones e isótopos


def especie_txt(sim, A, q):
    sup = str(A).translate(Q.SUP)
    car = "" if not q else (str(abs(q)) if abs(q) > 1 else "").translate(Q.SUP) + ("⁺" if q > 0 else "⁻")
    return f"{sup}{sim}{car}"


def r_particulas(s, d):
    for i, (sim, A, q) in enumerate(d["especies"]):
        bien = Q.particulas(sim, A, q)
        Z = ELEMENTOS[sim]["Z"]
        e = bien["electrones"]
        if s.toca("carga-al-reves") and q:
            e = Z + q
            s.marcar(f"un ion con carga {signo(q)} tiene {abs(q)} electrones {'menos' if q > 0 else 'más'} que el átomo neutro; "
                     "el chat ha sumado la carga en lugar de restarla")
            val = {"protones": Z, "neutrones": A - Z, "electrones": e}
            s.paso(f"{especie_txt(sim, A, q)}: Z = {Z}, así que {pl(Z, 'protón', 'protones')}; neutrones = {A} − {Z} = {A - Z}; electrones = {Z} + {abs(q)} = {e}.",
                   [Z, A - Z, e], {"tipo": "particulas", "simbolo": sim, "A": A, "carga": q, "valores": val})
        else:
            op = f"{Z} − {q} = {e}" if q > 0 else (f"{Z} + {-q} = {e}" if q < 0 else f"protones = {e}, porque es neutro")
            s.paso(f"{especie_txt(sim, A, q)}: Z = {Z}, así que {pl(Z, 'protón', 'protones')}; neutrones = {A} − {Z} = {A - Z}; electrones = {op}.",
                   [Z, A - Z, e], {"tipo": "particulas", "simbolo": sim, "A": A, "carga": q,
                                   "valores": {"protones": Z, "neutrones": A - Z, "electrones": e}})
        s.resp(f"{letra(i)} {especie_txt(sim, A, q)}:", f"{pl(Z, 'protón', 'protones')}, {pl(A - Z, 'neutrón', 'neutrones')} y {pl(e, 'electrón', 'electrones')}", [Z, A - Z, e], "terna")


# ================================================================ 3. tabla periódica: casillas y pistas


def r_casillas(s, d):
    por = {(e["grupo"], e["periodo"]): sym for sym, e in ELEMENTOS.items()}
    for i, (g, p) in enumerate(d["casillas"]):
        sym = por.get((g, p))
        if sym is None:
            raise ErrorDeModelo(f"no hay elemento del libro en el grupo {g}, periodo {p}")
        e = ELEMENTOS[sym]
        s.paso(f"Grupo {g}, periodo {p}: {sym} ({e['nombre']}), {e['tipo']}.", sym)
        s.resp(f"{letra(i)}", f"{sym} ({e['nombre']})", sym, "simbolo")


def cumple(sym, pista):
    e = ELEMENTOS[sym]
    k, v = pista
    if k == "periodo":
        return e["periodo"] == v
    if k == "grupo":
        return e["grupo"] == v
    if k == "tipo":
        return e["tipo"] == v
    if k == "ion":
        return ION_COMUN.get(sym) == v
    if k == "zpar":
        return (e["Z"] % 2 == 0) == v
    if k == "zmayor":
        return e["Z"] > v
    raise ErrorDeModelo(f"pista desconocida {k}")


def pista_txt(p):
    k, v = p
    if k == "periodo":
        return f"Estoy en el periodo {v}."
    if k == "grupo":
        return f"Estoy en el grupo {v}."
    if k == "tipo":
        return {"metal": "Soy un metal.", "no metal": "Soy un no metal.", "gas noble": "Soy un gas noble.",
                "semimetal": "Soy un semimetal."}[v]
    if k == "ion":
        return f"Mi ion más común tiene carga {abs(v)}{'+' if v > 0 else '−'}."
    if k == "zpar":
        return "Mi número atómico es par." if v else "Mi número atómico es impar."
    if k == "zmayor":
        return f"Tengo más de {v} protones."
    raise ErrorDeModelo(k)


CANDIDATOS = sorted((s for s, e in ELEMENTOS.items() if 2 <= e["Z"] <= 20), key=lambda s: ELEMENTOS[s]["Z"])


def r_pistas(s, d):
    for i, pistas in enumerate(d["acertijos"]):
        quedan = list(CANDIDATOS)
        trozos = []
        for p in pistas:
            quedan = [x for x in quedan if cumple(x, tuple(p))]
            trozos.append(f"«{pista_txt(p)[:-1]}» deja {lista_y(quedan) if quedan else 'ninguno'}")
        if len(quedan) != 1:
            raise ErrorDeModelo(f"el acertijo {i + 1} no tiene solución única: {quedan}")
        sym = quedan[0]
        s.paso(f"Acertijo {i + 1}: " + "; ".join(trozos) + ".", sym)
        s.resp(f"{letra(i)}", f"{sym} ({ELEMENTOS[sym]['nombre']})", sym, "simbolo")


# ================================================================ 4. clasificaciones con respuesta fija

MATERIA = {  # sustancia: clase (los casos dudosos, como la leche o el agua del mar, no se usan)
    "agua destilada": "compuesto", "sal de mesa (cloruro de sodio)": "compuesto", "azúcar (sacarosa)": "compuesto",
    "dióxido de carbono": "compuesto", "oxígeno": "elemento", "hierro": "elemento", "cobre": "elemento",
    "diamante (carbono)": "elemento", "aire limpio": "mezcla homogénea", "agua con azúcar disuelto": "mezcla homogénea",
    "vinagre": "mezcla homogénea", "bronce (aleación de cobre y estaño)": "mezcla homogénea", "agua con aceite": "mezcla heterogénea",
    "arena con agua": "mezcla heterogénea", "granito": "mezcla heterogénea", "ensalada": "mezcla heterogénea",
    "agua con sal disuelta": "mezcla homogénea", "aluminio": "elemento",
}
CLASES = ["elemento", "compuesto", "mezcla homogénea", "mezcla heterogénea"]
POR_QUE = {"elemento": "un solo tipo de átomo", "compuesto": "un solo tipo de sustancia, formada por átomos de varios elementos",
           "mezcla homogénea": "varias sustancias en una sola fase, con la misma composición en todas sus partes",
           "mezcla heterogénea": "varias sustancias en fases o partes con distinta composición"}

CAMBIOS = {
    "fundirse un cubito de hielo": "físico", "disolver sal en agua": "físico", "romperse un vaso": "físico",
    "secarse un charco": "físico", "triturar azúcar hasta hacerla polvo": "físico", "empañarse el espejo en la ducha": "físico",
    "doblar un clip": "físico", "congelar un zumo": "físico", "oxidarse un clavo": "químico", "cocer un huevo": "químico",
    "fermentar la masa del pan": "químico", "ponerse marrón una manzana cortada": "químico", "agriarse la leche": "químico",
    "salir burbujas al echar bicarbonato en vinagre": "químico", "tostar pan": "químico", "digerir los alimentos": "químico",
}
POR_QUE_CAMBIO = {"físico": "la sustancia sigue siendo la misma", "químico": "se forman sustancias nuevas"}


def r_clasificar(s, d):
    for i, x in enumerate(d["items"]):
        c = MATERIA[x]
        s.paso(f"{x[0].upper() + x[1:]}: {c} ({POR_QUE[c]}).", c)
        s.resp(f"{letra(i)}", c, c, "opcion")


def r_cambio(s, d):
    for i, x in enumerate(d["items"]):
        c = CAMBIOS[x]
        s.paso(f"{x[0].upper() + x[1:]}: cambio {c} ({POR_QUE_CAMBIO[c]}).", c)
        s.resp(f"{letra(i)}", c, c, "opcion")


# ================================================================ 5. ¿quién tiene razón?

ESCENAS = {
    "disolver": {"situacion": "Echas una cucharada de azúcar en un vaso de agua, remueves y el azúcar deja de verse.",
                 "personajes": ["Lucía", "Hugo", "Sara"],
                 "dichos": ["El azúcar ha desaparecido.", "El azúcar sigue ahí, repartido en partículas tan pequeñas que no se ven.",
                            "El azúcar se ha convertido en agua."],
                 "razon": "Hugo", "porque": "Las partículas de azúcar se reparten entre las de agua: es una mezcla homogénea, "
                 "no una sustancia nueva. La masa total del recipiente, el agua y el azúcar no cambia al disolverlo, y si dejas que el agua "
                 "se evapore, el azúcar vuelve a aparecer."},
    "evaporar": {"situacion": "Un charco de agua se seca al sol.", "personajes": ["Lucía", "Hugo", "Sara"],
                 "dichos": ["Las partículas de agua se han destruido.", "Las partículas de agua se han hecho más grandes y ligeras.",
                            "Las partículas de agua son las mismas, pero ahora están separadas y moviéndose en el aire."],
                 "razon": "Sara", "porque": "En un cambio de estado las partículas no se destruyen ni cambian de tamaño: cambia lo "
                 "separadas que están y cómo se mueven."},
    "gas-masa": {"situacion": "Tres amigos discuten si el aire tiene masa.", "personajes": ["Lucía", "Hugo", "Sara"],
                 "dichos": ["El aire no tiene masa: no pesa nada.", "Un gas tiene masa, aunque sea mucho menos denso que un líquido.",
                            "Los gases tienen masa negativa: por eso suben los globos."],
                 "razon": "Hugo", "porque": "Los gases están hechos de partículas con masa. Que sean poco densos (mucha separación "
                 "entre partículas) no quiere decir que no tengan masa."},
    "oxidar": {"situacion": "En un tarro de cristal bien cerrado, con aire dentro, un clavo de hierro se oxida durante semanas. "
                            "¿Qué pasa con la masa de todo el tarro?",
               "personajes": ["Lucía", "Hugo", "Sara"],
               "dichos": ["Baja, porque el hierro se gasta.", "Sube, porque aparece óxido nuevo.",
                          "No cambia: el oxígeno del aire pasa al óxido sin salir del tarro."],
               "razon": "Sara", "porque": "Ley de conservación de la masa: en un sistema cerrado los átomos se reordenan, pero no "
               "aparecen ni desaparecen. El clavo gana la masa del oxígeno que pierde el aire."},
}


def r_quien(s, d):
    es = ESCENAS[d["escena"]]
    s.paso(es["porque"], es["razon"])
    s.resp("", f"tiene razón {es['razon']}", es["razon"], "quien")


# ================================================================ 6. conservación de la masa


def r_conservacion(s, d):
    if d["modo"] == "vaso":
        a, b = Decimal(str(d["antes"])), Decimal(str(d["despues"]))
        gas = a - b
        s.paso(f"Masa antes − masa después = {numero(a, nd=1)} g − {numero(b, nd=1)} g = {numero(gas, nd=1)} g.", _q(gas),
               {"tipo": "cuenta", "calculado": _q(gas), "esperado": _q(a - b)})
        s.paso("Esa masa no se ha destruido: es el gas que ha salido del vaso abierto.", "gas")
        s.resp("", f"{numero(gas, nd=1)} g de gas", _q(gas), "numero", "g")
        return
    reac = [(n, Decimal(str(m))) for n, m in d["reactivos"]]
    (pc, mc), pd = d["producto_conocido"], d["producto_pedido"]
    total = sum(m for _, m in reac)
    s.paso("Masa de los reactivos: " + " + ".join(f"{numero(m, nd=1)} g" for _, m in reac) + f" = {numero(total, nd=1)} g.", _q(total),
           {"tipo": "cuenta", "calculado": _q(total), "esperado": _q(total)})
    x = total - Decimal(str(mc))
    s.paso(f"En un sistema cerrado, los productos tienen la misma masa: {pd} = {numero(total, nd=1)} g − {numero(Decimal(str(mc)), nd=1)} g "
           f"= {numero(x, nd=1)} g.", _q(x))
    s.resp("", f"{numero(x, nd=1)} g de {pd}", _q(x), "numero", "g")


# ================================================================ 7. masas a partir de la fórmula y proporciones definidas


def nombre_masa(f, unidad):
    """Qué masa se calcula: masa molar (g/mol) en las cuentas con moles; si no, masa molecular (sustancias moleculares) o
    masa de la unidad fórmula (compuestos iónicos), según Q.es_ionica."""
    if unidad == "g/mol":
        return f"Masa molar de {bonita(f)}"
    m = Q.magnitud_masa(f)
    return f"{m[0].upper() + m[1:]} de {bonita(f)}"


def masa_paso(s, f, unidad="u"):
    """Paso de masa a partir de la fórmula. Errores: «subindice» (cuenta una vez un elemento que lleva subíndice) y
    «parentesis»."""
    bien, t, _ = Q.masa_molecular(f)
    pre = nombre_masa(f, unidad) + ": "
    if s.toca("subindice") and any(n > 1 for n, _, _ in t):
        k = next(i for i, (n, _, _) in enumerate(t) if n > 1)
        t2 = [(1 if i == k else n, el, m) for i, (n, el, m) in enumerate(t)]
        mal = sum((n * m for n, _, m in t2), Decimal(0)).quantize(bien)
        s.marcar(f"en {bonita(f)} hay {t[k][0]} átomos de {t[k][1]} y el chat ha sumado su masa una sola vez")
        txt = Q.texto_masa(f, unidad, terminos=t2, resultado=mal)
        s.paso(pre + txt + ".", _q(mal), {"tipo": "masa", "texto": txt})
        return mal
    if s.toca("parentesis") and "(" in f:
        dentro = f.split("(")[1].split(")")[0]
        plano = f.split("(")[0] + dentro
        t2 = Q.masa_molecular(plano)[1]
        mal = sum((n * m for n, _, m in t2), Decimal(0)).quantize(bien)
        s.marcar(f"el chat ha ignorado el subíndice que va detrás del paréntesis de {bonita(f)}, que multiplica todo lo de dentro")
        txt = Q.texto_masa(f, unidad, terminos=t2, resultado=mal)
        s.paso(pre + txt + ".", _q(mal), {"tipo": "masa", "texto": txt})
        return mal
    txt = Q.texto_masa(f, unidad)
    s.paso(pre + txt + ".", _q(bien), {"tipo": "masa", "texto": txt})
    return bien


def r_masa_molecular(s, d):
    for i, f in enumerate(d["formulas"]):
        m = masa_paso(s, f)
        s.resp(f"{letra(i)} {bonita(f)}:", f"{numero(m, nd=Q.decimales(m))} u", _q(m), "numero", "u", formula=f)


def r_proporciones(s, d):
    f = d["formula"]
    a, _ = Q.atomos(f)
    (el_dado, m_dado), el_pide = d["dado"], d["pide"]
    m_dado = Decimal(str(m_dado))
    parte = {el: a[el] * ELEMENTOS[el]["masa"] for el in a}
    orden = Q.orden_elementos([(1, f)], [])
    s.paso(f"En {bonita(f)} hay " + " por cada ".join(
        f"{numero(parte[el], nd=Q.decimales(parte[el]))} u de {el}" for el in orden) + ".",
        {el: _q(v) for el, v in parte.items()})
    razon = parte[el_pide] / parte[el_dado]
    if s.toca("proporcion-invertida"):
        razon = parte[el_dado] / parte[el_pide]
        s.marcar(f"la proporción es masa de {el_pide} entre masa de {el_dado}, no al revés")
        s.paso(f"Proporción {el_pide} : {el_dado} = {numero(parte[el_dado], nd=Q.decimales(parte[el_dado]))} : {numero(parte[el_pide], nd=Q.decimales(parte[el_pide]))} = {numero(razon, cifras=4)}.",
               _q(razon), {"tipo": "cuenta", "calculado": _q(razon), "esperado": _q(parte[el_pide] / parte[el_dado])})
    else:
        s.paso(f"Proporción {el_pide} : {el_dado} = {numero(parte[el_pide], nd=Q.decimales(parte[el_pide]))} : {numero(parte[el_dado], nd=Q.decimales(parte[el_dado]))} = {numero(razon, cifras=4)}.",
               _q(razon), {"tipo": "cuenta", "calculado": _q(razon), "esperado": _q(razon)})
    m_pide = m_dado * razon
    s.paso(f"Con {numero(m_dado, cifras=3)} g de {el_dado} se combinan {numero(m_dado, cifras=3)} g · {numero(razon, cifras=4)} = {numero(m_pide, cifras=3)} g de {el_pide}.",
           _q(m_pide))
    total = m_dado + m_pide
    s.paso(f"Se forman {numero(m_dado, cifras=3)} g + {numero(m_pide, cifras=3)} g = {numero(total, cifras=3)} g de {bonita(f)} (la masa se conserva).",
           _q(total))
    s.resp("a)", f"{numero(m_pide, cifras=3)} g de {el_pide}", _q(m_pide), "numero", "g")
    s.resp("b)", f"{numero(total, cifras=3)} g de {bonita(f)}", _q(total), "numero", "g")


# ================================================================ 8. iones, fórmulas y nombres


def r_formula_ionica(s, d):
    for i, (pos, q, neg) in enumerate(d["pares"]):
        f = Q.componer(pos, q, neg)
        qn = Q.ANIONES[neg][1]
        _, n1, _, n2 = Q.descomponer(f)
        ion_p = bonita(f"{pos}^{q if q > 1 else ''}+")
        ion_n = bonita(f"{neg}^{-qn if qn < -1 else ''}-")
        cargas = {pos: q, neg: qn}
        if s.toca("cargas") and (n1, n2) != (1, 1):
            mal = f"{pos}{neg}"
            s.marcar(f"{ion_p} y {ion_n} no tienen cargas iguales y opuestas: con un ion de cada, la carga total es "
                     f"{signo(q + qn)}, no cero")
            s.paso(f"{ion_p} con {ion_n}: uno de cada, {bonita(mal)}.", mal, {"tipo": "neutra", "formula": mal, "cargas": cargas})
            f = mal
        else:
            s.paso(f"{ion_p} con {ion_n}: hacen falta {n1} {ion_p} ({signo(n1 * q)}) y {n2} {ion_n} ({signo(n2 * qn)}) para que las cargas sumen "
                   f"cero: {bonita(f)}.", f, {"tipo": "neutra", "formula": f, "cargas": cargas})
        s.resp(f"{letra(i)} {ion_p} y {ion_n}:", bonita(f), Q.simple(f), "formula")


def r_nombrar_ion(s, d):
    for i, (sym, q) in enumerate(d["iones"]):
        n = Q.ion_nombre(sym, q)
        ion = bonita(f"{sym}^{abs(q) if abs(q) > 1 else ''}{'+' if q > 0 else '-'}")
        if q > 0:
            extra = (f"; el hierro, el cobre y el plomo pueden tener varios estados de oxidación, así que se escribe en números "
                     "romanos (en un ion monoatómico coincide con su carga)"
                     if Q.variable(sym) else "; en estos retos tiene un único estado de carga, así que no lleva número romano")
            s.paso(f"{ion}: catión de {ELEMENTOS[sym]['nombre']}{extra}: {n}.", n)
        else:
            s.paso(f"{ion}: anión; el nombre acaba en «-uro» (o es «óxido»): {n}.", n)
        s.resp(f"{letra(i)} {ion}:", n, n, "ion", formula=f"{sym}:{q}")


def nombre_paso(s, f, sistema):
    """Paso que nombra un compuesto binario. Errores: «stock» (número romano leído del subíndice) y «prefijo»."""
    ns = Q.nombres(f)
    pos, n1, neg, n2 = Q.descomponer(f)
    q = Q.numero_oxidacion(f)
    qn = Q.ANIONES[neg][1]
    el = ELEMENTOS[pos]["nombre"]
    if sistema == "stock":
        nombre = ns["stock"]
        if Q.variable(pos):
            if s.toca("stock") and n1 != q:
                mal_q = n1
                nombre = f"{Q.ANIONES[neg][0]} de {el}({Q.ROMANOS[mal_q]})"
                s.marcar(f"el número romano es el estado de oxidación del {el}, que se calcula con las cargas: {n2} · ({signo(qn)}) = {signo(n2 * qn)}, "
                         f"repartido entre {n1} átomo{'s' if n1 > 1 else ''} de {el}, da +{q}; el chat ha copiado el subíndice")
                s.paso(f"{bonita(f)}: el {el} lleva subíndice {n1}, así que actúa con +{mal_q}: {nombre}.", nombre,
                       {"tipo": "nombre", "nombre": nombre, "formula": f})
                return nombre
            s.paso(f"{bonita(f)}: {pl(n2, Q.ANIONES[neg][0], Q.ANIONES[neg][0] + 's')} {'suma' if n2 == 1 else 'suman'} {signo(n2 * qn)}; "
                   + (f"el átomo de {el} debe sumar {signo(-n2 * qn)}, así que actúa con +{q}: {nombre}." if n1 == 1 else
                      f"{n1} átomos de {el} deben sumar {signo(-n2 * qn)}, así que cada uno actúa con +{q}: {nombre}."), nombre,
                   {"tipo": "nombre", "nombre": nombre, "formula": f})
        else:
            s.paso(f"{bonita(f)}: el {el} solo actúa con +{q}, así que no lleva número romano: {nombre}.", nombre,
                   {"tipo": "nombre", "nombre": nombre, "formula": f})
        return nombre
    nombre = ns["prefijos"]
    if s.toca("prefijo") and n1 != n2:
        nombre = f"{Q._pref(n1, Q.ANIONES[neg][0], Q.variable(pos))} de {Q._pref(n2, el, False)}"
        s.marcar(f"el prefijo de «{Q.ANIONES[neg][0]}» cuenta los átomos de {neg} ({n2}) y el de «{el}» los de {pos} ({n1}); el chat los ha cambiado")
        s.paso(f"{bonita(f)}: {n1} de {pos} y {n2} de {neg}: {nombre}.", nombre, {"tipo": "nombre", "nombre": nombre, "formula": f})
        return nombre
    s.paso(f"{bonita(f)}: {n2} átomo{'s' if n2 > 1 else ''} de {neg} y {n1} de {pos}: {nombre}.", nombre,
           {"tipo": "nombre", "nombre": nombre, "formula": f})
    return nombre


def r_nombrar(s, d):
    for i, f in enumerate(d["formulas"]):
        n = nombre_paso(s, f, d["sistema"] if d["sistema"] != "mixto" else ("stock" if Q.nombres(f)["stock"] else "prefijos"))
        s.resp(f"{letra(i)} {bonita(f)}:", n, n, "nombre", formula=Q.simple(f))


def r_formular(s, d):
    for i, n in enumerate(d["nombres"]):
        f = Q.formula_de_nombre(n)
        pos, n1, neg, n2 = Q.descomponer(f)
        q = Q.numero_oxidacion(f)
        if "(" in n:
            s.paso(f"{n[0].upper() + n[1:]}: {pos} con +{q} y {neg} con {signo(Q.ANIONES[neg][1])}; para que sumen cero: {bonita(f)}.", f,
                   {"tipo": "nombre", "nombre": n, "formula": f})
        elif any(n.startswith(p) for p in list(Q.DE_PREFIJO) + ["mon"]) or " de di" in n or " de tri" in n:
            s.paso(f"{n[0].upper() + n[1:]}: los prefijos dan {n1} de {pos} y {n2} de {neg}: {bonita(f)}.", f,
                   {"tipo": "nombre", "nombre": n, "formula": f})
        else:
            s.paso(f"{n[0].upper() + n[1:]}: el {ELEMENTOS[pos]['nombre']} solo actúa con +{q} y el {neg} con {signo(Q.ANIONES[neg][1])}: {bonita(f)}.", f,
                   {"tipo": "nombre", "nombre": n, "formula": f})
        s.resp(f"{letra(i)}", bonita(f), Q.simple(f), "formula")


def r_domino(s, d):
    fichas = {k: (f, n) for k, f, n in d["fichas"]}
    por_formula = {Q.simple(f): k for k, (f, _) in fichas.items()}
    orden = ["A"]
    while len(orden) < len(fichas):
        _, n = fichas[orden[-1]]
        k = por_formula[Q.formula_de_nombre(n)]
        if k in orden:
            raise ErrorDeModelo("el dominó se cierra antes de usar todas las fichas")
        orden.append(k)
    if por_formula[Q.formula_de_nombre(fichas[orden[-1]][1])] != "A":
        raise ErrorDeModelo("el dominó no se cierra")
    for a, b in zip(orden, orden[1:] + ["A"]):
        s.paso(f"{a} acaba en «{fichas[a][1]}», que es {bonita(fichas[b][0])}: sigue {b}.", b)
    s.resp("", ", ".join(orden), orden, "orden")
    s.orden = orden


# ================================================================ 9. ecuaciones: recuento y ajuste


def r_recuento(s, d):
    for i, e in enumerate(d["ecuaciones"]):
        c = Q.comprobar_ecuacion(e)
        izq, der = Q.leer_ecuacion(e)
        txt = f"{Q.escribir_ecuacion(izq, der)}: izquierda {recuento_txt(c['izquierda'])}; derecha {recuento_txt(c['derecha'])}"
        if c["carga"] != (0, 0):
            txt += f"; carga {signo(c['carga'][0])} y {signo(c['carga'][1])}"
        if c["ajustada"]:
            txt += ". Ajustada."
        else:
            nombres = {"carga": "la carga"}
            txt += ". No ajustada: no cuadra " + lista_y([nombres.get(x, x) for x in c["falla"]]) + "."
        s.paso(txt, c["ajustada"])
        s.resp(f"{letra(i)}", "sí" if c["ajustada"] else "no", "sí" if c["ajustada"] else "no", "opcion")


def ajuste_pasos(s, reactivos, productos):
    """Tres pasos: recuento sin coeficientes, coeficientes del ajuste exacto y comprobación. Error: «mal-ajustada»."""
    c0 = Q.comprobar_ecuacion(([(1, r) for r in reactivos], [(1, p) for p in productos]))
    t0 = (f"Sin coeficientes: izquierda {recuento_txt(c0['izquierda'])}; derecha {recuento_txt(c0['derecha'])}")
    if c0["carga"] != (0, 0):
        t0 += f"; carga {signo(c0['carga'][0])} y {signo(c0['carga'][1])}"
    s.paso(t0 + ".", [c0["izquierda"], c0["derecha"]])
    a, b = Q.ajustar(reactivos, productos)
    coefs = a + b
    if s.toca("mal-ajustada"):
        mal = list(coefs)
        # cambia el coeficiente de la especie cuyo elemento más repetido «cuadra a ojo» (el oxígeno, si está)
        k = next((i for i, f in enumerate(list(reactivos) + list(productos)) if f in ("O2", "H2O", "O2^0")), len(coefs) - 1)
        mal[k] = mal[k] + 1 if mal[k] > 1 else mal[k] + 1
        izq = list(zip(mal[:len(a)], reactivos))
        der = list(zip(mal[len(a):], productos))
        e = Q.escribir_ecuacion(izq, der)
        cm = Q.comprobar_ecuacion((izq, der))
        s.marcar(f"con esos coeficientes no cuadra {lista_y(cm['falla'])}: izquierda {recuento_txt(cm['izquierda'])} y derecha "
                 f"{recuento_txt(cm['derecha'])}")
        s.paso(f"Coeficientes {', '.join(map(str, mal))}: {e}.", mal, {"tipo": "ecuacion", "ecuacion": Q.escribir_ecuacion(izq, der, False)})
        s.paso("Comprobación: ya está ajustada.", "ajustada")
        return mal, e
    izq, der = list(zip(a, reactivos)), list(zip(b, productos))
    e = Q.escribir_ecuacion(izq, der)
    s.paso(f"Coeficientes {', '.join(map(str, coefs))}: {e}.", coefs, {"tipo": "ecuacion", "ecuacion": Q.escribir_ecuacion(izq, der, False)})
    c = Q.comprobar_ecuacion((izq, der))
    t = f"Comprobación: izquierda {recuento_txt(c['izquierda'])}; derecha {recuento_txt(c['derecha'])}"
    if any(Q.atomos(x)[1] for x in list(reactivos) + list(productos)):
        t += f"; carga {signo(c['carga'][0])} a cada lado"
    s.paso(t + ". Ajustada.", "ajustada")
    return coefs, e


def r_ajuste(s, d):
    coefs, e = ajuste_pasos(s, d["reactivos"], d["productos"])
    s.resp("", f"{e} (coeficientes {', '.join(map(str, coefs))})", coefs, "coeficientes")


# ================================================================ 10. mol, concentración y estequiometría


def r_mol(s, d):
    f, m = d["formula"], Decimal(str(d["m"]))
    M = masa_paso(s, f, "g/mol")
    n = m / M
    if s.toca("mol-por-masa"):
        n = m * M
        s.marcar("el número de moles es la masa dividida entre la masa molar (g : g/mol = mol); el chat ha multiplicado")
        s.paso(f"n = m · M = {numero(m, cifras=3)} g · {numero(M, nd=Q.decimales(M))} g/mol = {numero(n, cifras=3)} mol.", _q(n),
               {"tipo": "cuenta", "calculado": _q(n), "esperado": _q(m / M)})
    else:
        s.paso(f"n = m : M = {numero(m, cifras=3)} g : {numero(M, nd=Q.decimales(M))} g/mol = {numero(n, cifras=4)} mol.", _q(n),
               {"tipo": "cuenta", "calculado": _q(n), "esperado": _q(m / M)})
    s.resp("a)", f"{numero(n, cifras=3)} mol", _q(n), "numero", "mol")
    if d.get("particulas"):
        N = n * AVOGADRO_LIBRO
        que = d.get("unidad_particula", "moléculas")
        s.paso(f"N = n · 6,022 · 10²³ = {numero(n, cifras=4)} mol · 6,022 · 10²³ por mol = {Q.cientifico(N, 3)} {que}.", _q(N))
        s.resp("b)", f"{Q.cientifico(N, 3)} {que}", _q(N), "numero", que)


def r_concentracion(s, d):
    V_mL = Decimal(str(d["V_mL"]))
    V = V_mL / 1000
    if s.toca("ml-sin-convertir"):
        V = V_mL
        s.marcar("la concentración en g/L pide el volumen en litros: hay que dividir los mililitros entre 1000, y el chat ha "
                 "usado los mililitros tal cual")
        s.paso(f"V = {numero(V_mL, nd=0)} mL, que uso tal cual: V = {numero(V_mL, nd=0)}.", _q(V), {"tipo": "cuenta", "calculado": _q(V), "esperado": _q(V_mL / 1000)})
    else:
        s.paso(f"V = {numero(V_mL, nd=0)} mL = {numero(V, nd=3)} L.", _q(V), {"tipo": "cuenta", "calculado": _q(V), "esperado": _q(V)})
    if d["modo"] == "c":
        m = Decimal(str(d["m"]))
        c = m / V
        s.paso(f"c = m : V = {numero(m, cifras=3)} g : {numero(V, nd=3) if V != V_mL else numero(V, nd=0)} {'L' if V != V_mL else 'mL'} = {numero(c, cifras=3)} g/L.", _q(c))
        s.resp("", f"{numero(c, cifras=3)} g/L", _q(c), "numero", "g/L")
    else:
        c = Decimal(str(d["c"]))
        m = c * V
        s.paso(f"m = c · V = {numero(c, cifras=3)} g/L · {numero(V, nd=3) if V != V_mL else numero(V, nd=0)} {'L' if V != V_mL else 'mL'} = {numero(m, cifras=3)} g.", _q(m))
        s.resp("", f"{numero(m, cifras=3)} g de {d['soluto']}", _q(m), "numero", "g")


def r_estequiometria(s, d):
    reac, prod = d["reactivos"], d["productos"]
    dado, m_dado = d["dado"], Decimal(str(d["m"]))
    pide = d["pide"]
    a, b = Q.ajustar(reac, prod)
    especies = list(reac) + list(prod)
    coef = dict(zip(especies, a + b))
    izq, der = list(zip(a, reac)), list(zip(b, prod))
    e = Q.escribir_ecuacion(izq, der)
    s.paso(f"Ecuación ajustada: {e}.", a + b, {"tipo": "ecuacion", "ecuacion": Q.escribir_ecuacion(izq, der, False)})
    M1 = masa_paso(s, dado, "g/mol")
    n1 = m_dado / M1
    s.paso(f"n({bonita(dado)}) = {numero(m_dado, cifras=3)} g : {numero(M1, nd=Q.decimales(M1))} g/mol = {numero(n1, cifras=4)} mol.", _q(n1),
           {"tipo": "cuenta", "calculado": _q(n1), "esperado": _q(m_dado / M1)})
    ka, kb = coef[dado], coef[pide]
    razon = Decimal(kb) / Decimal(ka)
    if s.toca("sin-coeficientes") and ka != kb:
        n2 = n1
        s.marcar(f"la ecuación ajustada dice {ka} mol de {bonita(dado)} por cada {kb} mol de {bonita(pide)}; el chat ha usado uno por uno")
        s.paso(f"Por cada mol de {bonita(dado)} sale un mol de {bonita(pide)}: n({bonita(pide)}) = {numero(n2, cifras=4)} mol.", _q(n2),
               {"tipo": "cuenta", "calculado": _q(n2), "esperado": _q(n1 * razon)})
    else:
        n2 = n1 * razon
        verbo = ("da" if ka == 1 else "dan") if pide in prod else ("reacciona con" if ka == 1 else "reaccionan con")
        rel = f"{ka} mol de {bonita(dado)} {verbo} {kb} mol de {bonita(pide)}"
        s.paso(f"Según la ecuación, {rel}: n({bonita(pide)}) = {numero(n1, cifras=4)} mol · {kb} : {ka} = {numero(n2, cifras=4)} mol.", _q(n2),
               {"tipo": "cuenta", "calculado": _q(n2), "esperado": _q(n1 * razon)})
    M2 = masa_paso(s, pide, "g/mol")
    m2 = n2 * M2
    s.paso(f"m({bonita(pide)}) = {numero(n2, cifras=4)} mol · {numero(M2, nd=Q.decimales(M2))} g/mol = {numero(m2, cifras=3)} g.", _q(m2))
    s.resp("", f"{numero(m2, cifras=3)} g de {bonita(pide)}", _q(m2), "numero", "g")


# ================================================================ 11. experimentos (lo esperado sale de las guías leídas)

ESPERADO = {
    "exp-disolver": ["La masa total (vaso, agua, azúcar, plato y cuchara) es la misma antes y después de disolverlo (la báscula "
                     "de cocina puede variar 1 g arriba o abajo).", "El azúcar no desaparece: sus partículas se reparten entre las del agua."],
    "exp-disolucion": ["Lo esperable es que el azúcar se disuelva antes en el agua tibia que en la fría, si todo lo demás es igual: "
                       "la misma cantidad de agua y de azúcar y la misma forma de remover.", "Con más temperatura, las partículas se "
                       "mueven más deprisa y se mezclan antes. Si al repetir los tiempos cambian mucho, busca qué variable no "
                       "controlaste."],
    "exp-cristales": ["Al cabo de unos días el agua se evapora y en el plato quedan cristales de sal con caras planas.",
                      "La sal no había desaparecido al disolverse: estaba repartida en el agua."],
    "exp-lombarda": ["El agua de lombarda cambia de color: con el vinagre se vuelve rosa o roja (ácido); con el bicarbonato, verde o "
                     "azulada (básico); con la sal y con el azúcar se queda morada, más o menos como el vaso testigo.",
                     "Por eso el agua de lombarda sirve de indicador: su color dice si algo es ácido o básico."],
    "exp-vaso-abierto": ["Al mezclar salen burbujas y la báscula marca menos que antes.", "La masa que falta es la del gas (dióxido de "
                         "carbono) que ha salido al aire: en un vaso abierto no se puede pesar. La masa total se conserva."],
    "exp-levadura": ["En el vaso con agua tibia y azúcar sale espuma antes y en más cantidad que en el de agua fría o en el que no "
                     "tiene azúcar.", "La temperatura y tener «alimento» (el azúcar) son factores que cambian la velocidad del proceso."],
    "exp-neutralizacion": ["El agua de lombarda con vinagre empieza rosa o roja. Al añadir bicarbonato salen burbujas: el "
                           "bicarbonato reacciona con el ácido acético del vinagre y se forma dióxido de carbono.",
                           "Tras varias veces, el color pasa a morado y, si sigues, a verde o azulado. El cambio de color indica "
                           "que la mezcla es menos ácida; no prueba que se haya gastado exactamente todo el ácido, porque el "
                           "indicador cambia de color poco a poco, no en un punto exacto.",
                           "Si llegas al límite de veces y el color no ha cambiado, no añadas más: apúntalo y avisa a la "
                           "persona adulta (el vinagre o la lombarda pueden ser distintos)."],
}


def r_experimento(s, d, tipo):
    for t in ESPERADO[tipo]:
        s.paso(t, t)
    if tipo == "exp-vaso-abierto":
        a, b = Decimal(str(d["antes"][0])), Decimal(str(d["despues"][0]))
        s.paso(f"Con los datos de ejemplo: {numero(a, nd=1)} g − {numero(b, nd=1)} g = {numero(a - b, nd=1)} g de gas.", _q(a - b))
        s.resp("", f"{numero(a - b, nd=1)} g de gas en el ejemplo", _q(a - b), "numero", "g")
    else:
        s.resp("", "compara tu predicción con lo observado", None, "observacion")


RESOLVER = {"contar-atomos": r_contar, "particulas": r_particulas, "tabla-casillas": r_casillas, "tabla-pistas": r_pistas,
            "clasificar-materia": r_clasificar, "cambio-fisico-quimico": r_cambio, "quien-tiene-razon": r_quien,
            "conservacion-masa": r_conservacion, "masa-molecular": r_masa_molecular, "proporciones": r_proporciones,
            "formula-ionica": r_formula_ionica, "nombrar-ion": r_nombrar_ion, "nombrar": r_nombrar, "formular": r_formular,
            "domino": r_domino, "recuento-ecuacion": r_recuento, "ajuste": r_ajuste, "mol": r_mol,
            "concentracion": r_concentracion, "estequiometria": r_estequiometria}


def resolver(tipo, datos, error=None):
    s = Sol(error)
    if tipo.startswith("exp-"):
        r_experimento(s, datos, tipo)
    elif tipo in RESOLVER:
        RESOLVER[tipo](s, datos)
    else:
        raise ErrorDeModelo(f"tipo de reto desconocido: {tipo}")
    if error and s.error_info is None:
        raise ErrorDeModelo(f"el error {error} no se puede meter en este reto")
    return s
