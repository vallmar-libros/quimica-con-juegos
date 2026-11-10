"""Masa a partir de la fórmula, con la tabla de elementos.py. Python 3.8 o posterior.

Suma la masa atómica de cada átomo y redondea a los decimales del dato menos preciso, como el libro. Dice qué masa es: masa
molecular (sustancias moleculares) o masa de la unidad fórmula (compuestos iónicos: llevan un metal o el ion amonio), en u,
y la masa molar en g/mol, que es la que se usa en las cuentas con moles.

Uso:
  python programas/masa.py H2SO4
  python programas/masa.py "Ca(OH)2"
  python programas/masa.py --tabla        (las masas atómicas que usa el libro y su fuente)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import elementos as E  # noqa: E402
import quimica as Q  # noqa: E402


def main(argv):
    if len(argv) < 2 or argv[1] in ("--ayuda", "-h", "--help"):
        print(__doc__)
        return 2
    if argv[1] == "--tabla":
        print(f"Fuente: {E.FUENTE_MASAS}")
        for s, e in sorted(E.ELEMENTOS.items(), key=lambda x: x[1]["Z"]):
            print(f"{e['Z']:>3} {s:<3} {e['nombre']:<12} {Q.numero(e['masa'], nd=Q.decimales(e['masa'])):>9}")
        return 0
    try:
        f = argv[1]
        m, _, _ = Q.masa_molecular(f)
        mag = Q.magnitud_masa(f)
        print(f"{mag[0].upper() + mag[1:]}: " + Q.texto_masa(f, "u") + f"  (masa molar: {Q.numero(m, nd=Q.decimales(m))} g/mol)")
        return 0
    except Q.ErrorQuimico as e:
        print(f"No lo entiendo: {e}.")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
