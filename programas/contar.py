"""Contador de átomos de «Química con juegos» (Leo Vallmar). Python 3.8 o posterior, sin instalar nada.

Con una fórmula, cuenta los átomos de cada elemento. Con una ecuación, cuenta los átomos (y la carga, si hay iones) a cada
lado de la flecha y dice «Ajustada» o «No ajustada». No ajusta la ecuación por ti: solo la comprueba.

Uso:
  python programas/contar.py "Ca(OH)2"
  python programas/contar.py "CH4 + 2 O2 -> CO2 + 2 H2O"
  python programas/contar.py "Cu + 2 Ag+ -> Cu^2+ + 2 Ag"        (cargas con + o -, o con ^: Fe^3+, SO4^2-)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import quimica as Q  # noqa: E402


def main(argv):
    if len(argv) < 2 or argv[1] in ("--ayuda", "-h", "--help"):
        print(__doc__)
        return 2
    t = " ".join(argv[1:])
    try:
        if Q.FLECHA.search(t):
            c = Q.comprobar_ecuacion(t)
            izq, der = Q.leer_ecuacion(t)
            print(Q.escribir_ecuacion(izq, der))
            print(f"{'elemento':<10}{'izquierda':>10}{'derecha':>10}")
            for el in c["orden"]:
                marca = "" if c["izquierda"][el] == c["derecha"][el] else "   <- no cuadra"
                print(f"{el:<10}{c['izquierda'][el]:>10}{c['derecha'][el]:>10}{marca}")
            if c["carga"] != (0, 0):
                print(f"{'carga':<10}{Q.signo(c['carga'][0]):>10}{Q.signo(c['carga'][1]):>10}" +
                      ("" if c["carga"][0] == c["carga"][1] else "   <- no cuadra"))
            if c["ajustada"]:
                print("Ajustada.")
                return 0
            print("No ajustada.")
            return 1
        a, carga = Q.atomos(t)
        orden = Q.orden_elementos([(1, t)], [])
        print(Q.bonita(t) + ": " + ", ".join(f"{a[el]} de {el}" for el in orden) + f"; en total, {sum(a.values())} átomo{'' if sum(a.values()) == 1 else 's'}" +
              (f"; carga {Q.signo(carga)}" if carga else "") + ".")
        return 0
    except Q.ErrorQuimico as e:
        print(f"No lo entiendo: {e}.")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
