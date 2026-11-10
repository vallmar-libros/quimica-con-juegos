"""Nombra y formula los compuestos binarios de «Química con juegos» (Leo Vallmar). Python 3.8 o posterior.

Con una fórmula da sus nombres (Stock y prefijos); con un nombre da la fórmula. Usa las reglas del libro: las cargas
tienen que sumar cero, el número romano es la carga del metal y los prefijos cuentan átomos. Solo conoce los iones y
los elementos de la tabla del libro.

Uso:
  python programas/nombrar.py Fe2O3
  python programas/nombrar.py "óxido de hierro(III)"
  python programas/nombrar.py "trióxido de dihierro"
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import quimica as Q  # noqa: E402


def main(argv):
    if len(argv) < 2 or argv[1] in ("--ayuda", "-h", "--help"):
        print(__doc__)
        return 2
    t = " ".join(argv[1:]).strip()
    try:
        if " " not in t and t[:1].isupper():
            n = Q.nombres(t)
            print(f"{Q.bonita(t)}")
            if n["stock"]:
                print(f"  Stock:    {n['stock']}")
            print(f"  Prefijos: {n['prefijos']}")
            return 0
        f = Q.formula_de_nombre(t)
        print(f"{t} → {Q.bonita(f)}")
        return 0
    except Q.ErrorQuimico as e:
        print(f"No lo entiendo: {e}.")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
