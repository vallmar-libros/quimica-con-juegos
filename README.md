# Materiales de «Química con juegos»

*70 retos para predecir, ajustar y comprobar, con y sin IA* — Leo Vallmar. Colección «Ciencias con juegos».

Materiales del libro, con la fecha de la edición de noviembre de 2026 (versión del 2026-11-10). El libro funciona entero sin ellos.

**Versión.** Al publicar el repositorio, los materiales de esta edición se fijan con la etiqueta de Git `edicion-2026-11`; es la versión que corresponde al libro impreso.

**Antes de cualquier experimento, lee [SEGURIDAD.md](SEGURIDAD.md).** Siempre con una persona adulta delante, solo materiales de cocina, sin calentar nada y sin comer ni beber nada de lo preparado.

## Contenido

### Retos, con su código (Q-capítulo-número)
- [retos/retos-cap-00.md](retos/retos-cap-00.md) — Capítulo 0. Cómo usar este libro: juega, duda, comprueba (3 retos)
- [retos/retos-cap-01.md](retos/retos-cap-01.md) — Capítulo 1. La materia y sus partículas (8 retos)
- [retos/retos-cap-02.md](retos/retos-cap-02.md) — Capítulo 2. Átomos y tabla periódica (8 retos)
- [retos/retos-cap-03.md](retos/retos-cap-03.md) — Capítulo 3. Formular y nombrar: iones y compuestos binarios (9 retos)
- [retos/retos-cap-04.md](retos/retos-cap-04.md) — Capítulo 4. Cambios químicos y química de la cocina (12 retos)
- [retos/retos-cap-05.md](retos/retos-cap-05.md) — Capítulo 5. Ajustar ecuaciones (4.º) (8 retos)
- [retos/retos-cap-06.md](retos/retos-cap-06.md) — Capítulo 6. El mol, las disoluciones y la estequiometría (4.º) (9 retos)
- [retos/retos-cap-07.md](retos/retos-cap-07.md) — Capítulo 7. Detective de la IA (7 retos)
- [retos/retos-cap-08.md](retos/retos-cap-08.md) — Capítulo 8. Retos finales (6 retos)

### Soluciones, en carpeta aparte
- [soluciones/soluciones-cap-00.md](soluciones/soluciones-cap-00.md)
- [soluciones/soluciones-cap-01.md](soluciones/soluciones-cap-01.md)
- [soluciones/soluciones-cap-02.md](soluciones/soluciones-cap-02.md)
- [soluciones/soluciones-cap-03.md](soluciones/soluciones-cap-03.md)
- [soluciones/soluciones-cap-04.md](soluciones/soluciones-cap-04.md)
- [soluciones/soluciones-cap-05.md](soluciones/soluciones-cap-05.md)
- [soluciones/soluciones-cap-06.md](soluciones/soluciones-cap-06.md)
- [soluciones/soluciones-cap-07.md](soluciones/soluciones-cap-07.md)
- [soluciones/soluciones-cap-08.md](soluciones/soluciones-cap-08.md)

### Hojas de datos de los experimentos
- [hojas/hoja-Q-00-02.md](hojas/hoja-Q-00-02.md) — Primer experimento: ¿pesa lo mismo el agua con azúcar?
- [hojas/hoja-Q-01-03.md](hojas/hoja-Q-01-03.md) — Azúcar en agua fría y en agua tibia
- [hojas/hoja-Q-01-05.md](hojas/hoja-Q-01-05.md) — Cristales de sal en un plato
- [hojas/hoja-Q-04-02.md](hojas/hoja-Q-04-02.md) — El indicador de lombarda
- [hojas/hoja-Q-04-04.md](hojas/hoja-Q-04-04.md) — Bicarbonato y vinagre en la báscula
- [hojas/hoja-Q-04-08.md](hojas/hoja-Q-04-08.md) — La levadura que hace espuma
- [hojas/hoja-Q-06-06.md](hojas/hoja-Q-06-06.md) — El vinagre pierde acidez

### Instrucciones de IA
- [instrucciones-ia/instrucciones-ia-2026-11-10.md](instrucciones-ia/instrucciones-ia-2026-11-10.md)

### Programas de comprobación (Python 3.8 o posterior, sin instalar nada)
- [programas/comprobar.py](programas/comprobar.py) — comprueba tu respuesta a un reto o enseña los pasos
- [programas/contar.py](programas/contar.py) — cuenta los átomos de una fórmula o de una ecuación y dice «Ajustada» o «No ajustada»
- [programas/elementos.py](programas/elementos.py) — los 31 elementos que usan los retos, con su masa atómica (© CIAAW/IUPAC, citada)
- [programas/experimento.py](programas/experimento.py) — analiza las dos masas del experimento de la báscula
- [programas/masa.py](programas/masa.py) — masa molecular (o de la unidad fórmula, si es iónica) y masa molar de una fórmula con la tabla del libro
- [programas/modelos_quimica.py](programas/modelos_quimica.py) — los pasos de la solución de cada reto
- [programas/nombrar.py](programas/nombrar.py) — nombra un compuesto binario o da la fórmula de un nombre
- [programas/quimica.py](programas/quimica.py) — química exacta: fórmulas, ecuaciones, ajuste con fracciones, masas y nomenclatura de binarios

### Datos y otros
- [datos/retos.json](datos/retos.json): datos de cada reto, sin soluciones; los leen los programas.
- [ERRATAS.md](ERRATAS.md): erratas conocidas a la fecha de la edición.

## Cómo usar los programas
Sin Python también se puede usar todo el libro: lee la [guía para familias sin Python](GUIA-SIN-PYTHON.md), que explica además cómo instalarlo paso a paso. Cómo escribir fórmulas, cargas y ecuaciones en la consola, con ejemplos listos para copiar: [FORMULAS.md](FORMULAS.md).

1. Descarga el repositorio: botón verde **Code** → **Download ZIP**, y descomprímelo.
2. Abre una terminal en la carpeta descomprimida.
3. Escribe la orden que trae cada reto, por ejemplo:

```text
python programas/contar.py "CH4 + 2 O2 -> CO2 + 2 H2O"
python programas/masa.py "H2SO4"
python programas/nombrar.py "Fe2O3"
python programas/comprobar.py Q-05-03 "1, 5, 3, 4"
```

Cada programa explica su uso con `--ayuda`. `comprobar.py --pasos` enseña la solución: úsalo después de intentarlo.

## Masas atómicas
Las masas de `programas/elementos.py` son las de los 31 elementos que usan los retos, tomadas de © CIAAW/IUPAC, «Abridged Standard Atomic Weights 2024» (https://www.ciaaw.org/abridged-atomic-weights.htm). No es una copia de la tabla de la CIAAW. Para tablas completas, consulta la página de la CIAAW.

## Antes de usar un chat de IA
Comprueba su edad mínima y sus condiciones vigentes. Con 13 años, usa la alternativa sin chat de cada reto. No escribas nunca tu nombre, tu centro, tu dirección ni fotos de personas. Nunca preguntes a un chat si algo es seguro.

## Licencia
Los retos, las soluciones, las hojas, las instrucciones y los programas de este repositorio se publican con licencia CC BY 4.0 (texto legal completo en [LICENSE](LICENSE); cómo citar en [AVISO.md](AVISO.md); resumen en [LICENSE.md](LICENSE.md)). El texto del libro no se incluye y sigue protegido.
