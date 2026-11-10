"""Comprueba tu respuesta a un reto de «Química con juegos» (Leo Vallmar). Python 3.8 o posterior, sin instalar nada.

El programa vuelve a resolver el reto con los datos de datos/retos.json (con cuentas exactas, no con un modelo de
lenguaje) y compara tu respuesta: números con un margen del 2 % por el redondeo, fórmulas átomo a átomo, nombres
volviendo del nombre a la fórmula y coeficientes de una ecuación uno a uno. Solo dice si está bien o qué respuesta no
cuadra; no da la solución.

Uso:
  python programas/comprobar.py Q-00-03 "3; 5; 2; 9"                (respuestas en el orden del reto, separadas por ;)
  python programas/comprobar.py Q-02-01 "7 7 7; 17 18 17; ..."       (protones, neutrones y electrones de cada uno)
  python programas/comprobar.py Q-03-03 "óxido de hierro(III); ..."  (nombres o fórmulas)
  python programas/comprobar.py Q-05-03 "1, 5, 3, 4"                (coeficientes de la ecuación, en orden)
  python programas/comprobar.py Q-03-05 "A, D, B, F, C, E"           (dominó: el orden de las fichas)
  python programas/comprobar.py Q-01-02 Hugo                         («¿quién tiene razón?»: el nombre)
  python programas/comprobar.py Q-05-03 --pasos                      (enseña la solución: úsalo después de intentarlo)
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

import modelos_quimica as M  # noqa: E402
import quimica as Q  # noqa: E402

RETOS = AQUI.parent / "datos" / "retos.json"


def sin_tildes(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower().strip()) if unicodedata.category(c) != "Mn")


def cargar(codigo):
    retos = json.loads(RETOS.read_text(encoding="utf-8"))["retos"]
    codigo = codigo.strip().upper()
    if codigo not in retos:
        print(f"No hay ningún reto con el código {codigo}. Los códigos son como Q-03-02.")
        sys.exit(2)
    return codigo, retos[codigo]


def primer_numero(t):
    m = re.search(r"[+-]?\d+(?:[.,]\d+)?(?:\s*[·x×*]\s*10\s*\^?\s*[+-−]?\d+|\s*·\s*10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+|[eE][+-]?\d+)?", t)
    if not m:
        raise ValueError(f"«{t.strip()}» no tiene ningún número")
    return Q.leer_numero(m.group(0))


def bien(r, dado):
    t = r["tipo"]
    if t == "numero":
        x = primer_numero(dado)
        ref = r["valor"]
        return abs(x - ref) <= 0.02 * abs(ref) + 1e-12
    if t == "terna":
        nums = [int(x) for x in re.findall(r"\d+", dado)]
        return nums == r["valor"]
    if t == "simbolo":
        d = dado.strip().split()[0].strip(",.()") if dado.strip() else ""
        return d == r["valor"] or sin_tildes(dado).startswith(sin_tildes(Q.ELEMENTOS[r["valor"]]["nombre"]))
    if t in ("opcion", "quien"):
        return sin_tildes(dado) == sin_tildes(r["valor"]) or sin_tildes(dado) == sin_tildes(r["valor"]).replace("mezcla ", "")
    if t == "ion":
        d = re.sub(r"^(ion|cation|anion)\s+", "", sin_tildes(dado)).replace(" (", "(")
        return d == re.sub(r"^ion\s+", "", sin_tildes(r["valor"]))
    if t == "nombre":
        return Q.nombre_correcto(dado, r["formula"])
    if t == "formula":
        return Q.misma_formula(dado.strip(), r["valor"])
    if t == "coeficientes":
        return [int(x) for x in re.findall(r"\d+", dado)] == r["valor"]
    if t == "orden":
        return [x.strip().upper() for x in re.split(r"[,\s]+", dado) if x.strip()] == r["valor"]
    raise ValueError(t)


def main(argv):
    if len(argv) < 3 or argv[1] in ("--ayuda", "-h", "--help"):
        print(__doc__)
        return 2
    codigo, r = cargar(argv[1])
    s = M.resolver(r["tipo"], r["datos"])
    if argv[2] == "--pasos":
        print(s.texto())
        return 0
    if r["tipo"].startswith("exp-"):
        print(f"El reto {codigo} es un experimento: compara lo que observas con tu predicción. Si tiene medidas, usa programas/experimento.py.")
        return 2
    esperadas = s.respuestas
    if esperadas[0]["tipo"] in ("coeficientes", "orden"):
        partes = [argv[2]]
    else:
        partes = [x for x in argv[2].split(";") if x.strip()]
    if len(partes) > len(esperadas):
        print(f"Este reto tiene {len(esperadas)} respuestas y has escrito {len(partes)}. Sepáralas con punto y coma (;).")
        return 2
    todo = True
    for i, (p, e) in enumerate(zip(partes, esperadas)):
        nombre = e["etiqueta"].rstrip(":") or f"respuesta {i + 1}"
        try:
            ok = bien(e, p)
        except (ValueError, Q.ErrorQuimico) as err:
            print(f"«{p.strip()}»: {err}")
            return 2
        print(f"«{p.strip()}»: {'bien' if ok else 'no cuadra'} ({nombre}).")
        todo = todo and ok
    if todo and len(partes) < len(esperadas):
        print(f"Vas bien, pero faltan {len(esperadas) - len(partes)} respuestas.")
        return 1
    if todo:
        print("Respuesta correcta.")
        return 0
    print("Revisa las que no cuadran antes de mirar la solución.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
