# Guía para familias sin Python

**No hace falta ningún programa para usar el libro.** Cada reto se comprueba en papel (contando átomos y cargas, sumando con la tabla del libro o volviendo del nombre a la fórmula) y las soluciones están al final del libro y en la carpeta [soluciones/](soluciones/soluciones-cap-00.md). Los programas son una ayuda más, no una obligación.

Si queréis usarlos en un ordenador (no funcionan en el móvil ni en la tableta), estos son los pasos. Hacedlos con una persona adulta; si el ordenador es del centro o de otra persona, pedid permiso antes de instalar nada.

## 1. Instalar Python (una sola vez)

- **Windows**: entrad en https://www.python.org/downloads/, descargad la versión 3 que se ofrece y abrid el instalador. Marcad la casilla **Add python.exe to PATH** antes de pulsar **Install Now**.
- **macOS**: la misma página, el instalador para macOS; se instala como cualquier otra aplicación.
- **Linux**: suele venir instalado; comprobadlo con `python3 --version` en una terminal.

Sirve cualquier Python 3.8 o posterior. Los programas no necesitan nada más.

## 2. Descargar los materiales

En la página del repositorio, botón verde **Code** → **Download ZIP**. Descomprimid el ZIP en una carpeta fácil de encontrar, por ejemplo en el Escritorio.

## 3. Abrir una terminal en esa carpeta

- **Windows**: abrid la carpeta descomprimida, haced clic en la barra de dirección, escribid `cmd` y pulsad Intro.
- **macOS**: clic derecho sobre la carpeta → **Servicios** → **Nueva terminal en la carpeta** (si no aparece, abrid **Terminal**, escribid `cd ` con un espacio detrás, arrastrad la carpeta a la ventana y pulsad Intro).
- **Linux**: clic derecho dentro de la carpeta → **Abrir en una terminal**.

## 4. Probar un programa

Escribid esta orden y pulsad Intro:

```text
python programas/contar.py "H2O"
```

Debe contestar `H₂O: 2 de H, 1 de O; en total, 3 átomos.` En Windows, si no funciona `python`, probad `py` en su lugar; en macOS y Linux, `python3`.

## 5. Usarlo con los retos

Cada reto del libro trae su orden. Cómo escribir fórmulas, cargas y ecuaciones: [FORMULAS.md](FORMULAS.md). `comprobar.py` solo dice si una respuesta está bien; con `--pasos` enseña la solución, así que usadlo después de intentarlo.

Vuelve al [README](README.md).
