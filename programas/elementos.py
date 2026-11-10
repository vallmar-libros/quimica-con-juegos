"""Los elementos que usan los retos de «Química con juegos» (Leo Vallmar): número atómico, nombre, grupo, periodo, tipo y
masa atómica. Python 3.8 o posterior, sin instalar nada.

Masas atómicas: pesos atómicos estándar abreviados de la Comisión de Abundancias Isotópicas y Pesos Atómicos de la IUPAC
(CIAAW), con cinco cifras significativas, tal como los publica en https://www.ciaaw.org/abridged-atomic-weights.htm
(«Abridged Standard Atomic Weights 2024», basada en el informe «Atomic Weights 2021»). Son datos (hechos), escritos una vez a mano y contrastados en el
G1 del libro: los 31 coinciden con la tabla de la CIAAW. Solo están los elementos que necesitan los retos: no es una copia
de la tabla de la CIAAW. La CIAAW permite el uso educativo con reconocimiento; para uso comercial pide contactar con su
Secretaría, así que esta lista se cita como fuente de los datos y su redistribución está pendiente de una decisión humana.

Grupo y periodo: tabla periódica de la IUPAC (grupos 1 a 18). Tipo: metal, no metal, semimetal o gas noble, como en
los libros de 2.º a 4.º de ESO.
"""
from decimal import Decimal

FUENTE_MASAS = ("© CIAAW/IUPAC, Abridged Standard Atomic Weights 2024: "
                "https://www.ciaaw.org/abridged-atomic-weights.htm")
AVOGADRO_EXACTA = Decimal("6.02214076E23")      # mol⁻¹, valor exacto desde la redefinición del SI de 2019
AVOGADRO_LIBRO = Decimal("6.022E23")            # el que usa el libro en las cuentas

# símbolo: (Z, nombre, grupo, periodo, tipo, masa atómica como texto)
_DATOS = {
    "H": (1, "hidrógeno", 1, 1, "no metal", "1.008"),
    "He": (2, "helio", 18, 1, "gas noble", "4.0026"),
    "Li": (3, "litio", 1, 2, "metal", "6.94"),
    "Be": (4, "berilio", 2, 2, "metal", "9.0122"),
    "B": (5, "boro", 13, 2, "semimetal", "10.81"),
    "C": (6, "carbono", 14, 2, "no metal", "12.011"),
    "N": (7, "nitrógeno", 15, 2, "no metal", "14.007"),
    "O": (8, "oxígeno", 16, 2, "no metal", "15.999"),
    "F": (9, "flúor", 17, 2, "no metal", "18.998"),
    "Ne": (10, "neón", 18, 2, "gas noble", "20.180"),
    "Na": (11, "sodio", 1, 3, "metal", "22.990"),
    "Mg": (12, "magnesio", 2, 3, "metal", "24.305"),
    "Al": (13, "aluminio", 13, 3, "metal", "26.982"),
    "Si": (14, "silicio", 14, 3, "semimetal", "28.085"),
    "P": (15, "fósforo", 15, 3, "no metal", "30.974"),
    "S": (16, "azufre", 16, 3, "no metal", "32.06"),
    "Cl": (17, "cloro", 17, 3, "no metal", "35.45"),
    "Ar": (18, "argón", 18, 3, "gas noble", "39.95"),
    "K": (19, "potasio", 1, 4, "metal", "39.098"),
    "Ca": (20, "calcio", 2, 4, "metal", "40.078"),
    "Mn": (25, "manganeso", 7, 4, "metal", "54.938"),
    "Fe": (26, "hierro", 8, 4, "metal", "55.845"),
    "Ni": (28, "níquel", 10, 4, "metal", "58.693"),
    "Cu": (29, "cobre", 11, 4, "metal", "63.546"),
    "Zn": (30, "cinc", 12, 4, "metal", "65.38"),
    "Br": (35, "bromo", 17, 4, "no metal", "79.904"),
    "Ag": (47, "plata", 11, 5, "metal", "107.87"),
    "I": (53, "yodo", 17, 5, "no metal", "126.90"),
    "Ba": (56, "bario", 2, 6, "metal", "137.33"),
    "Au": (79, "oro", 11, 6, "metal", "196.97"),
    "Pb": (82, "plomo", 14, 6, "metal", "207.2"),
}

ELEMENTOS = {s: {"Z": z, "nombre": n, "grupo": g, "periodo": p, "tipo": t, "masa": Decimal(m)}
             for s, (z, n, g, p, t, m) in _DATOS.items()}
MASAS = {s: e["masa"] for s, e in ELEMENTOS.items()}
POR_Z = {e["Z"]: s for s, e in ELEMENTOS.items()}
# Carga del ion monoatómico más común de los 20 primeros elementos (solo los que forman uno sin ambigüedad en ESO).
ION_COMUN = {"Li": 1, "Be": 2, "N": -3, "O": -2, "F": -1, "Na": 1, "Mg": 2, "Al": 3, "S": -2, "Cl": -1, "K": 1, "Ca": 2}
