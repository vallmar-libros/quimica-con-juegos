# Retos · Capítulo 4. Cambios químicos y química de la cocina

Retos Q-04-01 a Q-04-12. Las soluciones están en [soluciones/soluciones-cap-04.md](../soluciones/soluciones-cap-04.md). Antes de cualquier experimento, lee [SEGURIDAD.md](../SEGURIDAD.md).

## Q-04-01 · ¿Cambio físico o químico?

Nivel 1 · práctica guiada · Bloque E: Los sistemas materiales: tipos de cambios (RD 217/2022)

¿Cambio físico o cambio químico? a) empañarse el espejo en la ducha; b) cocer un huevo; c) doblar un clip; d) digerir los alimentos; e) salir burbujas al echar bicarbonato en vinagre; f) secarse un charco.

**Comprueba:** preguntarse si aparece una sustancia nueva.

```text
python programas/comprobar.py Q-04-01 "respuesta 1; respuesta 2; …"
```

## Q-04-02 · El indicador de lombarda

Nivel 1 · práctica guiada · Bloque E: Interpretación macroscópica y microscópica de las reacciones químicas (RD 217/2022)

El agua de lombarda cambia de color según lo que le eches. Predice el color de cada vaso: con vinagre, con bicarbonato, con sal, con azúcar y el vaso testigo, sin nada.

**Antes de empezar (seguridad)**

- Con una persona adulta delante.
- Material: lombarda, agua del grifo, bol, colador, vasos, vinagre, bicarbonato, sal, azúcar, rotulador, termómetro de cocina, gafas.
- Riesgo: El vinagre escuece en los ojos: ponte las gafas y no te frotes los ojos. La lombarda mancha la ropa. Solo estos materiales de cocina: nunca productos de limpieza. Nada de lo preparado se come ni se bebe. Al acabar, se tira todo por el fregadero con agua.
- Límite: agua del grifo a 45 °C como máximo, medida por la persona adulta (si pasa, se mezcla con agua fría y se vuelve a medir); sin calentar nada.
- Gafas: Puede salpicar: ponte gafas de protección y no te frotes los ojos. Sin gafas, este experimento no se hace.
- Si algo salpica, te pica la piel o huele raro, para, lávate con agua y avisa a la persona adulta.

**Material:** dos hojas de lombarda (col roja); agua del grifo tibia, 45 °C como mucho (la mide la persona adulta); un bol; un colador; cinco vasos transparentes; vinagre; bicarbonato; sal; azúcar; un rotulador; un termómetro de cocina; gafas de protección.

**Pasos:**

1. La persona adulta trocea con las manos las hojas de lombarda en el bol, las cubre con agua tibia del grifo (45 °C como mucho), espera 15 minutos y cuela el agua, que sale morada.
2. Escribe en cada vaso con el rotulador: vinagre, bicarbonato, sal, azúcar y «testigo». Echa en cada uno un poco de agua de lombarda.
3. Escribe tu predicción: ¿de qué color se pondrá cada vaso?
4. Con las gafas puestas, añade a cada vaso una cucharadita de lo que dice su etiqueta; el testigo se queda como está, para comparar. Remueve y apunta el color.

Hoja de datos: [hojas/hoja-Q-04-02.md](../hojas/hoja-Q-04-02.md)

**Comprueba:** comparar cada color con tu predicción.

## Q-04-03 · La masa que se escapa

Nivel 1 · práctica guiada · Bloque E: Ley de conservación de la masa y ley de las proporciones definidas (RD 217/2022)

En un vaso abierto sobre una báscula se mezclan bicarbonato y vinagre. Antes de mezclar, todo marca 387,9 g. Cuando dejan de salir burbujas, marca 385,7 g. ¿Cuánta masa falta? ¿Adónde ha ido?

**Comprueba:** comprobar que la masa de los productos es igual a la de los reactivos.

```text
python programas/comprobar.py Q-04-03 "respuesta 1; respuesta 2; …"
```

## Q-04-04 · Bicarbonato y vinagre en la báscula

Nivel 2 · práctica guiada · Bloque E: Ley de conservación de la masa y ley de las proporciones definidas (RD 217/2022)

Mezclas bicarbonato y vinagre en un vaso abierto encima de la báscula. Datos de ejemplo: antes, 312,4 g; después, 311,1 g. ¿Se ha destruido masa? Predice qué marcará tu báscula y compruébalo.

**Antes de empezar (seguridad)**

- Con una persona adulta delante.
- Material: vaso de plástico, vinagre, bicarbonato, plato, bandeja, báscula de cocina, gafas.
- Riesgo: Hace espuma y puede salpicar: gafas, vaso ancho y bandeja debajo. No tapes nunca el vaso ni lo cierres: el gas tiene que salir. Nada de lo preparado se come ni se bebe.
- Límite: vaso abierto, nunca tapado; una cucharadita de bicarbonato y medio vaso de vinagre como mucho; sin calentar nada.
- Gafas: Puede salpicar: ponte gafas de protección y no te frotes los ojos. Sin gafas, este experimento no se hace.
- Si algo salpica, te pica la piel o huele raro, para, lávate con agua y avisa a la persona adulta.

**Material:** un vaso ancho de plástico con medio vaso de vinagre; una cucharadita de bicarbonato en un plato pequeño; una bandeja; una báscula de cocina; gafas de protección.

**Pasos:**

1. Escribe tu predicción: al mezclar, ¿la báscula marcará más, menos o lo mismo? ¿Por qué?
2. Pon la bandeja en la báscula y, encima, el vaso con el vinagre y el plato con el bicarbonato. Apunta la masa.
3. Con las gafas puestas, echa el bicarbonato en el vaso. Salen burbujas: deja el vaso abierto, sin taparlo.
4. Cuando dejen de salir burbujas, apunta lo que marca la báscula con todo encima (vaso, plato y bandeja). La diferencia esperada es pequeña, de 1 a 2 g: una báscula de cocina puede variar 1 g arriba o abajo.

Hoja de datos: [hojas/hoja-Q-04-04.md](../hojas/hoja-Q-04-04.md)

**Comprueba:** programa del repositorio con tus dos masas.

```text
python programas/experimento.py Q-04-04 "masa antes" "masa después"
```

## Q-04-05 · Masas a partir de la fórmula

Nivel 2 · práctica guiada · Bloque B: Principales compuestos químicos: masa atómica y masa molecular (RD 217/2022)

Masas a partir de la fórmula. Con las masas atómicas de la tabla del libro, calcula en unidades de masa atómica (u) la masa molecular de cada sustancia molecular o la masa de la unidad fórmula de cada compuesto iónico (los que llevan un metal). Di cuál de las dos es. Redondea a los decimales del dato menos preciso: a) H₂O; b) Al₂(SO₄)₃; c) C₆H₁₂O₆; d) H₂SO₄.

**Comprueba:** repetir la suma con la tabla; programa del repositorio, por ejemplo: python programas/masa.py "Mg(NO3)2".

```text
python programas/comprobar.py Q-04-05 "respuesta 1; respuesta 2; …"
```

## Q-04-06 · ¿Está ajustada?

Nivel 2 · práctica guiada · Bloque E: Ley de conservación de la masa y ley de las proporciones definidas (RD 217/2022)

Cuenta los átomos de cada elemento a cada lado de la flecha y di si cada ecuación está ajustada (sí o no). No hace falta ajustarlas: a) 2 CH₄ + 2 O₂ → CO₂ + 2 H₂O; b) CaCO₃ + 3 HCl → CaCl₂ + H₂O + CO₂; c) 2 HNO₃ + Mg(OH)₂ → Mg(NO₃)₂ + 2 H₂O; d) 2 Mg + O₂ → 3 MgO.

**Con IA (opcional)** (pista graduada, instrucción P-01, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Pistas impresas del reto, de una en una y en orden; o un adulto que las lee.

<details><summary>Pistas impresas (léelas de una en una)</summary>

1. Cuenta los átomos de cada elemento a la izquierda y a la derecha de la flecha.
2. El coeficiente multiplica toda la fórmula; el subíndice, solo al átomo que tiene delante.
3. ¿Has contado el oxígeno en todas las sustancias en las que aparece?

</details>

**Comprueba:** contador del repositorio, por ejemplo: python programas/contar.py "Cu + 2 Ag^+ -> Cu^2+ + 2 Ag".

```text
python programas/comprobar.py Q-04-06 "respuesta 1; respuesta 2; …"
```

## Q-04-07 · Siempre en la misma proporción

Nivel 2 · práctica guiada · Bloque E: Ley de conservación de la masa y ley de las proporciones definidas (RD 217/2022)

Ley de las proporciones definidas: en el cloruro de sodio (NaCl), los elementos siempre se combinan en la misma proporción de masa. Si reaccionan por completo 11,5 g de sodio, ¿cuántos gramos de cloro se combinan con ellos? ¿Cuánto cloruro de sodio se forma? Usa las masas atómicas de la tabla.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. En NaCl hay 22,990 u de Na por cada 35,45 u de Cl.
2. Proporción Cl : Na = 22,990 : 35,45 = 0,6485.
3. Con 11,5 g de Na se combinan 11,5 g · 0,6485 = 7,46 g de Cl.
4. Se forman 11,5 g + 7,46 g = 19,0 g de NaCl (la masa se conserva).

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-04-07 "respuesta 1; respuesta 2; …"
```

## Q-04-08 · La levadura que hace espuma

Nivel 2 · práctica guiada · Bloque E: Factores que afectan a las reacciones químicas (RD 217/2022)

La levadura de panadería con azúcar y agua hace espuma. ¿Qué la hace ir más deprisa: el agua tibia, el azúcar o las dos cosas? Predice por escrito y compruébalo con tres vasos.

**Antes de empezar (seguridad)**

- Con una persona adulta delante.
- Material: vasos, levadura de panadería, azúcar, agua del grifo, termómetro de cocina, cucharilla, rotulador, regla.
- Riesgo: Agua tibia, nunca más de 40 °C: la mide la persona adulta. Nada de lo preparado se come ni se bebe. Al acabar, se tira por el fregadero y se lavan los vasos.
- Límite: agua del grifo a 40 °C como máximo, medida por la persona adulta (si pasa, se mezcla con agua fría y se vuelve a medir); sin calentar nada.
- Si algo salpica, te pica la piel o huele raro, para, lávate con agua y avisa a la persona adulta.

**Material:** tres vasos transparentes iguales; un sobre de levadura de panadería; azúcar; agua del grifo fría; agua del grifo tibia, 40 °C como mucho (la mide la persona adulta); un termómetro de cocina; una cucharilla; un rotulador; una regla.

**Pasos:**

1. Escribe tu predicción: ¿en qué vaso saldrá más espuma? ¿Por qué?
2. La persona adulta prepara el agua tibia del grifo y comprueba con el termómetro que no pasa de 40 °C.
3. Vaso A: medio vaso de agua tibia, una cucharilla de azúcar y una de levadura. Vaso B: igual, pero con agua fría. Vaso C: agua tibia y levadura, sin azúcar. Remueve los tres.
4. Cada 5 minutos, marca con el rotulador hasta dónde llega la espuma, durante 20 minutos. Los vasos se quedan abiertos.

Hoja de datos: [hojas/hoja-Q-04-08.md](../hojas/hoja-Q-04-08.md)

**Comprueba:** comparar las alturas de espuma con tu predicción.

## Q-04-09 · El clavo en el tarro cerrado

Nivel 2 · práctica guiada · Bloque E: Ley de conservación de la masa y ley de las proporciones definidas (RD 217/2022)

En un tarro de cristal bien cerrado, con aire dentro, un clavo de hierro se oxida durante semanas. ¿Qué pasa con la masa de todo el tarro? Lucía: «Baja, porque el hierro se gasta.» Hugo: «Sube, porque aparece óxido nuevo.» Sara: «No cambia: el oxígeno del aire pasa al óxido sin salir del tarro.» ¿Quién tiene razón? Escribe tu predicción y por qué antes de mirar la solución.

**Comprueba:** contrastar cada frase con el modelo de partículas y con la conservación de la masa.

```text
python programas/comprobar.py Q-04-09 "nombre"
```

## Q-04-10 · Cambios en la cocina

Nivel 1 · sin ayuda (sin IA y sin pistas) · Bloque E: Los sistemas materiales: tipos de cambios (RD 217/2022)

¿Cambio físico o cambio químico? a) salir burbujas al echar bicarbonato en vinagre; b) congelar un zumo; c) fundirse un cubito de hielo; d) ponerse marrón una manzana cortada; e) oxidarse un clavo; f) triturar azúcar hasta hacerla polvo.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-04-10 "respuesta 1; respuesta 2; …"
```

## Q-04-11 · La masa de los productos

Nivel 2 · sin ayuda (sin IA y sin pistas) · Bloque E: Ley de conservación de la masa y ley de las proporciones definidas (RD 217/2022)

En un recipiente cerrado reaccionan por completo 16,0 g de metano con 64,0 g de oxígeno. Se forman 44,0 g de dióxido de carbono y algo de agua. ¿Cuántos gramos de agua se forman?

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-04-11 "respuesta 1; respuesta 2; …"
```

## Q-04-12 · Repaso: cartas de iones

Nivel 2 · sin ayuda (sin IA y sin pistas) · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Cartas de iones: junta cada catión con su anión y escribe la fórmula del compuesto neutro (las cargas tienen que sumar cero): a) Mg²⁺ y N³⁻; b) Ag⁺ y S²⁻; c) Pb⁴⁺ y O²⁻; d) Zn²⁺ y I⁻.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-04-12 "respuesta 1; respuesta 2; …"
```
