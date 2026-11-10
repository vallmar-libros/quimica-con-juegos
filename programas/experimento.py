"""Analiza tus medidas del experimento de la báscula de «Química con juegos» (Leo Vallmar). Python 3.8 o posterior.

Escribe la masa de antes y la de después (en gramos). El programa calcula la diferencia y te dice si cabe en el margen de
una báscula de cocina (1 g arriba o abajo) o si ha salido gas del vaso abierto.

Uso:
  python programas/experimento.py Q-04-04 "312,4" "311,1"
  python programas/experimento.py Q-00-02 "405" "405"
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import quimica as Q  # noqa: E402

MARGEN_G = 1.0


def main(argv):
    if len(argv) < 4 or argv[1] in ("--ayuda", "-h", "--help"):
        print(__doc__)
        return 2
    try:
        antes, despues = Q.leer_numero(argv[2]), Q.leer_numero(argv[3])
    except ValueError as e:
        print(e)
        return 2
    dif = antes - despues
    print(f"Antes: {Q.numero(antes, nd=1)} g. Después: {Q.numero(despues, nd=1)} g. Diferencia: {Q.numero(dif, nd=1)} g.")
    if abs(dif) <= MARGEN_G:
        print("La masa es la misma dentro del margen de la báscula (1 g): no ha salido nada del vaso.")
    elif dif > 0:
        print(f"Faltan {Q.numero(dif, nd=1)} g: es la masa del gas que ha salido del vaso abierto. La masa total se conserva.")
    else:
        print("Después pesa más: revisa que has pesado lo mismo las dos veces (vaso, plato, cuchara y bandeja).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
