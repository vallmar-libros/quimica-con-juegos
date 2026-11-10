# Retos · Capítulo 6. El mol, las disoluciones y la estequiometría (4.º)

Retos Q-06-01 a Q-06-09. Las soluciones están en [soluciones/soluciones-cap-06.md](../soluciones/soluciones-cap-06.md). Antes de cualquier experimento, lee [SEGURIDAD.md](../SEGURIDAD.md).

## Q-06-01 · De gramos a moles

Nivel 3 · práctica guiada · Bloque B: Cuantificación de la cantidad de materia: número de moles (4.º) (RD 217/2022)

Tienes 4,20 g de bicarbonato de sodio (NaHCO₃). Calcula su masa molar con la tabla y di cuántos moles son.

**Comprueba:** comprobar que g : (g/mol) da mol; programa del repositorio.

```text
python programas/comprobar.py Q-06-01 "respuesta 1; respuesta 2; …"
```

## Q-06-02 · ¿Cuántas moléculas?

Nivel 3 · práctica guiada · Bloque B: Cuantificación de la cantidad de materia: número de moles (4.º) (RD 217/2022)

Tienes 8,00 g de metano (CH₄). Calcula su masa molar con la tabla y di cuántos moles son. ¿Cuántas moléculas hay? Usa 6,022 · 10²³ partículas por mol.

**Con IA (opcional)** (pista graduada, instrucción P-01, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Pistas impresas del reto, de una en una y en orden; o un adulto que las lee.

<details><summary>Pistas impresas (léelas de una en una)</summary>

1. Primero la masa molar: suma las masas de la tabla de todos los átomos.
2. El número de moles es la masa dividida entre la masa molar.
3. ¿Tus unidades dan mol? g : (g/mol) = mol.

</details>

**Comprueba:** comprobar que g : (g/mol) da mol; programa del repositorio.

```text
python programas/comprobar.py Q-06-02 "respuesta 1; respuesta 2; …"
```

## Q-06-03 · Una disolución en g/L

Nivel 3 · práctica guiada · Bloque B: Sistemas materiales: disoluciones (4.º) (RD 217/2022)

Disuelves 20,0 g de sal en agua hasta tener 500 mL de disolución. ¿Cuál es la concentración en gramos por litro (g/L)?

**Comprueba:** comprobar que el volumen está en litros; programa del repositorio.

```text
python programas/comprobar.py Q-06-03 "respuesta 1; respuesta 2; …"
```

## Q-06-04 · Receta química

Nivel 3 · práctica guiada · Bloque E: Ecuaciones químicas: ajuste y estequiometría (4.º) (RD 217/2022)

Receta química: C₃H₈ + O₂ → CO₂ + H₂O. Ajusta la ecuación. Si reaccionan por completo 44,1 g de propano, ¿cuántos gramos de agua se forman? Usa las masas de la tabla.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. Ecuación ajustada: C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O.
2. Masa molar de C₃H₈: M(C₃H₈) = 3 · 12,011 + 8 · 1,008 = 44,097 g/mol.
3. n(C₃H₈) = 44,1 g : 44,097 g/mol = 1,000 mol.
4. Por cada mol de C₃H₈ sale un mol de H₂O: n(H₂O) = 1,000 mol.
5. Masa molar de H₂O: M(H₂O) = 2 · 1,008 + 15,999 = 18,015 g/mol.
6. m(H₂O) = 1,000 mol · 18,015 g/mol = 18,0 g.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-06-04 "respuesta 1; respuesta 2; …"
```

## Q-06-05 · El gas del bicarbonato

Nivel 3 · práctica guiada · Bloque E: Ecuaciones químicas: ajuste y estequiometría (4.º) (RD 217/2022)

Receta química: NaHCO₃ + CH₃COOH → CH₃COONa + H₂O + CO₂. Ajusta la ecuación. Si reaccionan por completo 8,40 g de bicarbonato de sodio, ¿cuántos gramos de dióxido de carbono se forman? Usa las masas de la tabla.

**Comprueba:** comprobar la ecuación con el contador y las unidades de cada paso; programa del repositorio.

```text
python programas/comprobar.py Q-06-05 "respuesta 1; respuesta 2; …"
```

## Q-06-06 · El vinagre pierde acidez

Nivel 3 · práctica guiada · Bloque E: Reacciones de combustión y neutralización (4.º) (RD 217/2022)

El vinagre pone rosa el agua de lombarda. ¿Qué pasa si le añades bicarbonato poco a poco? Predice cómo cambiará el color y cuenta cuántas veces hay que añadir ¼ de cucharadita para que deje de ser rosa. ¿Qué te dice ese color: que la mezcla es menos ácida o que ya no queda nada de ácido?

**Antes de empezar (seguridad)**

- Con una persona adulta delante.
- Material: agua de lombarda, vinagre, bicarbonato, vaso, cuchara de medir, cucharilla, gafas.
- Riesgo: Salen burbujas y puede salpicar: gafas, vaso grande y sin taparlo nunca. Solo estos materiales de cocina: nunca productos de limpieza. Nada de lo preparado se come ni se bebe.
- Límite: vaso grande y abierto; ¼ de cucharadita de bicarbonato cada vez y 8 veces como mucho (2 cucharaditas en total); sin calentar nada.
- Gafas: Puede salpicar: ponte gafas de protección y no te frotes los ojos. Sin gafas, este experimento no se hace.
- Si algo salpica, te pica la piel o huele raro, para, lávate con agua y avisa a la persona adulta.

**Material:** agua de lombarda ya fría (la prepara la persona adulta como en el reto Q-04-02); vinagre; bicarbonato; un vaso transparente grande; una cuchara de medir de ¼ de cucharadita; una cucharilla; gafas de protección.

**Pasos:**

1. Echa en el vaso medio vaso de agua de lombarda y una cucharada de vinagre: se pone rosa.
2. Escribe tu predicción: ¿cómo cambiará el color al añadir bicarbonato poco a poco? ¿Cuántas veces habrá que añadir?
3. Con las gafas puestas, añade ¼ de cucharadita de bicarbonato. Espera a que paren las burbujas, remueve y apunta el color.
4. Repite, ¼ de cucharadita cada vez, hasta que el color deje de ser rosa, y como mucho 8 veces (2 cucharaditas en total). Cuenta cuántas veces has añadido.
5. Si después de 8 veces el color no ha cambiado, para: no añadas más. Apúntalo y avisa a la persona adulta. Al acabar, se tira todo por el fregadero con agua.

Hoja de datos: [hojas/hoja-Q-06-06.md](../hojas/hoja-Q-06-06.md)

**Comprueba:** comparar los colores y las veces que has añadido bicarbonato con tu predicción.

## Q-06-07 · Moles sin ayuda

Nivel 3 · sin ayuda (sin IA y sin pistas) · Bloque B: Cuantificación de la cantidad de materia: número de moles (4.º) (RD 217/2022)

Tienes 58,4 g de cloruro de sodio (NaCl). Calcula su masa molar con la tabla y di cuántos moles son. ¿Cuántas unidades hay? Usa 6,022 · 10²³ partículas por mol.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-06-07 "respuesta 1; respuesta 2; …"
```

## Q-06-08 · Estequiometría sin ayuda

Nivel 3 · sin ayuda (sin IA y sin pistas) · Bloque E: Ecuaciones químicas: ajuste y estequiometría (4.º) (RD 217/2022)

Receta química: C₆H₁₂O₆ + O₂ → CO₂ + H₂O. Ajusta la ecuación. Si reaccionan por completo 45,0 g de glucosa, ¿cuántos gramos de dióxido de carbono se forman? Usa las masas de la tabla.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-06-08 "respuesta 1; respuesta 2; …"
```

## Q-06-09 · Repaso: masas a partir de la fórmula

Nivel 2 · sin ayuda (sin IA y sin pistas) · Bloque B: Principales compuestos químicos: masa atómica y masa molecular (RD 217/2022)

Masas a partir de la fórmula. Con las masas atómicas de la tabla del libro, calcula en unidades de masa atómica (u) la masa molecular de cada sustancia molecular o la masa de la unidad fórmula de cada compuesto iónico (los que llevan un metal). Di cuál de las dos es. Redondea a los decimales del dato menos preciso: a) NH₃; b) H₂SO₄; c) Al₂(SO₄)₃; d) CaCO₃.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-06-09 "respuesta 1; respuesta 2; …"
```
