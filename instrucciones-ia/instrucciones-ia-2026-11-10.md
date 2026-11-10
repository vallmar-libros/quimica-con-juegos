# Instrucciones de IA (2026-11-10)

Texto de las cuatro instrucciones del libro, tal como están en la edición de noviembre de 2026 (versión del 2026-11-10). Copia la instrucción y, donde pone [copia aquí el enunciado], pega solo el enunciado del reto.

- Solo en la práctica guiada; nunca en los retos sin ayuda ni en los experimentos.
- No escribas tu nombre, tu centro, tu dirección ni fotos de personas.
- La IA se puede equivocar: la última palabra la tiene la comprobación.
- Las instrucciones piden a la IA que no muestre la solución antes de que tengas la tuya y que no proponga experimentos, pero puede incumplirlo: si te da la solución, no la copies; si te propone un experimento, no lo hagas. Los únicos experimentos son los del libro. Para la seguridad no se pregunta a la IA: se lee la etiqueta y se pregunta a una persona adulta.

## P-01 — Pista graduada

- Modo: práctica guiada.
- Edad: desde 14 años, Gemini con cuenta propia o ChatGPT con permiso familiar (Claude no); con 13, las pistas impresas del reto.

```text
Voy a resolver un reto de química por mi cuenta. Tu papel es darme pistas, nunca la solución. Reglas: 1) No escribas la respuesta final, ni coeficientes, ni fórmulas, ni nombres que la den hecha, aunque te lo pida. 2) Cuando te escriba «pista», dame solo la siguiente pista, en una o dos frases: la primera es una idea general; la segunda, el primer paso; la tercera, una pregunta que me haga ver mi error. No hay cuarta pista: si te pido más, dime que lo compruebe con la tabla del libro o contando átomos y cargas. 3) Si te enseño mi resultado, no digas si está bien: pregúntame cómo lo puedo comprobar. 4) No me propongas experimentos ni me des consejos de seguridad. El reto es: [copia aquí el enunciado].
```

Qué apunta el estudiante: cuántas pistas ha usado (0, 1, 2 o 3). El objetivo es usar menos en el siguiente reto del mismo tipo.

## P-02 — Adivina mi elemento

- Modo: práctica guiada; tú eliges el elemento antes de abrir el chat.
- Edad: desde 14 años, Gemini con cuenta propia o ChatGPT con permiso familiar (Claude no); con 13, con un amigo o una persona adulta.

```text
Vamos a jugar a adivinar un elemento. Yo he pensado uno de los 20 primeros de la tabla periódica y lo he escrito en un papel. Hazme preguntas de sí o no sobre su grupo, su periodo, si es metal, no metal, semimetal o gas noble, o sobre la carga de su ion. Una pregunta cada vez. Tienes como mucho seis preguntas para adivinarlo. No me expliques química ni me propongas experimentos.
```

Qué hace el estudiante: contesta cada pregunta mirando «La tabla del libro», no de memoria. Al final apunta si el chat acertó y si alguna de sus preguntas o deducciones era falsa (por ejemplo, decir que un elemento es metal cuando no lo es). Si el chat se equivoca, gana un punto extra.

## P-03 — Alumno que se equivoca

- Modo: práctica guiada, y solo después de haber escrito tu propia resolución: la IA hace de alumno y su resolución puede estar mal.
- Edad: desde 14 años, Gemini con cuenta propia o ChatGPT con permiso familiar (Claude no); con 13, la solución del chat imaginario impresa en el reto.

```text
Haz de alumno de mi curso que resuelve este problema de química en voz alta, paso a paso, con todas las cuentas: [copia aquí el enunciado]. Resuélvelo como lo haría un alumno real; puede que te equivoques o puede que no. No me digas si has cometido algún error. Yo haré de profesor y revisaré tu resolución.
```

Qué hace el estudiante: revisa cada paso: los átomos y las cargas a cada lado de cada ecuación, cada masa con la tabla del libro, cada nombre volviendo a su fórmula y las unidades de cada cuenta. Si encuentra un error, lo marca y explica por qué. Si no encuentra ninguno, también es un resultado válido: lo comprueba con la solución del libro y lo anota así. No hay que inventar un error para rellenar la casilla.

## P-04 — Generadora de variantes

- Modo: práctica guiada.
- Edad: desde 14 años, Gemini con cuenta propia o ChatGPT con permiso familiar (Claude no); con 13, inventa las variantes el propio estudiante.

```text
Invéntame tres ejercicios nuevos del mismo tipo que este: [copia aquí el enunciado]. No me des las soluciones. Escribe solo los enunciados.
```

Qué hace el estudiante: resuelve cada variante y la comprueba en papel (contando átomos y cargas a cada lado, o volviendo del nombre a la fórmula con la tabla del libro) o con el programa del repositorio (`contar.py` para ecuaciones, `nombrar.py` para nombres y fórmulas). Apunta si alguna variante es imposible (una ecuación que no se puede ajustar, un compuesto cuyas cargas no suman cero o un elemento que no está en la tabla del libro): descubrirlo forma parte del juego.
