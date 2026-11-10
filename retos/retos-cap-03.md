# Retos · Capítulo 3. Formular y nombrar: iones y compuestos binarios

Retos Q-03-01 a Q-03-09. Las soluciones están en [soluciones/soluciones-cap-03.md](../soluciones/soluciones-cap-03.md). Antes de cualquier experimento, lee [SEGURIDAD.md](../SEGURIDAD.md).

## Q-03-01 · Nombres de iones

Nivel 1 · práctica guiada · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Nombra cada ion monoatómico: a) Fe²⁺; b) N³⁻; c) Cl⁻; d) Cu²⁺; e) Al³⁺; f) I⁻.

**Comprueba:** comprobar si el metal puede tener varios estados de oxidación; programa del repositorio.

```text
python programas/comprobar.py Q-03-01 "respuesta 1; respuesta 2; …"
```

## Q-03-02 · Cartas de iones

Nivel 2 · práctica guiada · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Cartas de iones: junta cada catión con su anión y escribe la fórmula del compuesto neutro (las cargas tienen que sumar cero): a) Fe²⁺ y Cl⁻; b) Cu⁺ y O²⁻; c) Pb⁴⁺ y O²⁻; d) Fe³⁺ y O²⁻.

**Comprueba:** comprobar que las cargas suman cero; programa del repositorio.

```text
python programas/comprobar.py Q-03-02 "respuesta 1; respuesta 2; …"
```

## Q-03-03 · Nombres con números romanos

Nivel 2 · práctica guiada · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Nombra cada compuesto con la nomenclatura de Stock (número romano solo si el metal puede tener varios estados de oxidación): a) CuCl₂; b) ZnI₂; c) PbO₂; d) Na₂O.

**Con IA (opcional)** (generadora de variantes, instrucción P-04, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Inventa tú tres ejercicios del mismo tipo y compruébalos en papel: cuenta átomos y cargas a cada lado, o vuelve del nombre a la fórmula con la tabla del libro.

Con chat (P-04): el chat inventa ejercicios sin mostrar las soluciones; resuélvelos y compruébalos con el programa.

**Comprueba:** volver del nombre a la fórmula; programa del repositorio, por ejemplo: python programas/nombrar.py FeCl2.

```text
python programas/comprobar.py Q-03-03 "respuesta 1; respuesta 2; …"
```

## Q-03-04 · Del nombre a la fórmula

Nivel 2 · práctica guiada · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Escribe la fórmula de cada compuesto: a) sulfuro de hierro(II); b) óxido de hierro(II); c) trióxido de azufre; d) dióxido de carbono.

**Con IA (opcional)** (pista graduada, instrucción P-01, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Pistas impresas del reto, de una en una y en orden; o un adulto que las lee.

<details><summary>Pistas impresas (léelas de una en una)</summary>

1. El número romano es el estado de oxidación del metal (en un ion monoatómico, su carga); los prefijos cuentan átomos.
2. Las cargas positivas y negativas del compuesto tienen que sumar cero.
3. ¿Has simplificado los subíndices si tenían un divisor común?

</details>

**Comprueba:** volver de la fórmula al nombre; programa del repositorio, por ejemplo: python programas/nombrar.py "cloruro de hierro(II)".

```text
python programas/comprobar.py Q-03-04 "respuesta 1; respuesta 2; …"
```

## Q-03-05 · Dominó de fórmulas y nombres

Nivel 2 · práctica guiada · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Dominó de fórmulas y nombres. Cada ficha tiene una fórmula a la izquierda y el nombre de otra sustancia a la derecha. Empieza por la ficha A y coloca detrás la ficha cuya fórmula corresponde al nombre de la anterior, hasta cerrar el círculo. Fichas: A [FeS | dióxido de nitrógeno]; B [SO₃ | pentaóxido de dinitrógeno]; C [N₂O₅ | sulfuro de hierro(II)]; D [NO₂ | cloruro de calcio]; E [CaCl₂ | cloruro de sodio]; F [NaCl | trióxido de azufre]. ¿En qué orden quedan?

**Comprueba:** comprobar que el círculo se cierra en la ficha A.

```text
python programas/comprobar.py Q-03-05 "A, …"
```

## Q-03-06 · Nombres con prefijos

Nivel 2 · práctica guiada · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Nombra cada compuesto con prefijos (mono-, di-, tri-…): a) SO₂; b) SF₆; c) NO₂; d) Fe₂O₃.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. SO₂: 1 de S y 2 de O: monóxido de diazufre.
2. SF₆: 6 átomos de F y 1 de S: hexafluoruro de azufre.
3. NO₂: 2 átomos de O y 1 de N: dióxido de nitrógeno.
4. Fe₂O₃: 3 átomos de O y 2 de Fe: trióxido de dihierro.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-03-06 "respuesta 1; respuesta 2; …"
```

## Q-03-07 · Más cartas de iones

Nivel 2 · sin ayuda (sin IA y sin pistas) · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Cartas de iones: junta cada catión con su anión y escribe la fórmula del compuesto neutro (las cargas tienen que sumar cero): a) Li⁺ y N³⁻; b) Ba²⁺ y Br⁻; c) Ag⁺ y S²⁻; d) Al³⁺ y Cl⁻.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-03-07 "respuesta 1; respuesta 2; …"
```

## Q-03-08 · Nombra sin ayuda

Nivel 2 · sin ayuda (sin IA y sin pistas) · Bloque B: Nomenclatura IUPAC: sustancias simples, iones monoatómicos y compuestos binarios (RD 217/2022)

Nombra cada compuesto con Stock si tiene un metal y con prefijos si son dos no metales: a) NaCl; b) FeO; c) SO₃; d) SO₂.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-03-08 "respuesta 1; respuesta 2; …"
```

## Q-03-09 · Repaso: dentro del átomo

Nivel 1 · sin ayuda (sin IA y sin pistas) · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

El número de arriba a la izquierda es el número másico A (protones + neutrones); el de arriba a la derecha, la carga. Con la tabla periódica del libro, di cuántos protones, neutrones y electrones tiene cada uno: a) ¹⁶O²⁻; b) ¹⁴N³⁻; c) ¹⁹F⁻; d) ³⁷Cl⁻.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-03-09 "p n e; p n e; …"
```
