# Retos · Capítulo 2. Átomos y tabla periódica

Retos Q-02-01 a Q-02-08. Las soluciones están en [soluciones/soluciones-cap-02.md](../soluciones/soluciones-cap-02.md). Antes de cualquier experimento, lee [SEGURIDAD.md](../SEGURIDAD.md).

## Q-02-01 · Dentro del átomo

Nivel 1 · práctica guiada · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

El número de arriba a la izquierda es el número másico A (protones + neutrones); el de arriba a la derecha, la carga. Con la tabla periódica del libro, di cuántos protones, neutrones y electrones tiene cada uno: a) ²⁷Al; b) ¹⁶O; c) ¹⁴N; d) ³⁹K.

**Comprueba:** comprobar que protones + neutrones da el número másico; programa del repositorio.

```text
python programas/comprobar.py Q-02-01 "p n e; p n e; …"
```

## Q-02-02 · Batalla naval de la tabla periódica

Nivel 1 · práctica guiada · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

Batalla naval de la tabla periódica. Juega con alguien: cada uno marca en su tabla, sin que el otro la vea, tres elementos de los periodos 1 a 3. Por turnos, «disparad» diciendo grupo y periodo; si hay un elemento marcado, el otro dice su nombre y su símbolo. Para entrenar, solo: ¿qué elemento hay en cada casilla? a) grupo 1, periodo 3; b) grupo 2, periodo 2; c) grupo 18, periodo 3; d) grupo 1, periodo 2; e) grupo 13, periodo 2. Di también si es metal, no metal, semimetal o gas noble.

**Comprueba:** mirar la tabla periódica del libro.

```text
python programas/comprobar.py Q-02-02 "símbolo 1; símbolo 2; …"
```

## Q-02-03 · Iones e isótopos

Nivel 2 · práctica guiada · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

El número de arriba a la izquierda es el número másico A (protones + neutrones); el de arriba a la derecha, la carga. Con la tabla periódica del libro, di cuántos protones, neutrones y electrones tiene cada uno: a) ³H; b) ¹⁸O; c) ³⁹K⁺; d) ³⁵Cl⁻.

**Con IA (opcional)** (pista graduada, instrucción P-01, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Pistas impresas del reto, de una en una y en orden; o un adulto que las lee.

<details><summary>Pistas impresas (léelas de una en una)</summary>

1. Los protones los da el número atómico Z, que está en la tabla.
2. Neutrones = número másico − protones.
3. ¿Un ion positivo tiene más o menos electrones que el átomo neutro?

</details>

**Comprueba:** comprobar que protones + neutrones da el número másico; programa del repositorio.

```text
python programas/comprobar.py Q-02-03 "p n e; p n e; …"
```

## Q-02-04 · ¿Quién soy?

Nivel 2 · práctica guiada · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

¿Quién soy? Cada acertijo es un elemento de número atómico 2 a 20 (del helio al calcio), y las pistas dejan un solo candidato: a) Estoy en el grupo 13. Tengo más de 11 protones. b) Tengo más de 10 protones. Estoy en el grupo 15. c) Estoy en el periodo 2. Mi ion más común tiene carga 1+.

**Con IA (opcional)** (rival, instrucción P-02, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Juega con un amigo o con un adulto: uno piensa un elemento y el otro lo adivina con preguntas de sí o no.

Con chat (P-02): tú piensas el elemento y el chat pregunta; contesta mirando la tabla.

**Comprueba:** comprobar que el elemento cumple todas las pistas y que ningún otro las cumple.

```text
python programas/comprobar.py Q-02-04 "símbolo 1; símbolo 2; …"
```

## Q-02-05 · Iones con carga

Nivel 2 · práctica guiada · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

El número de arriba a la izquierda es el número másico A (protones + neutrones); el de arriba a la derecha, la carga. Con la tabla periódica del libro, di cuántos protones, neutrones y electrones tiene cada uno: a) ²⁴Mg²⁺; b) ²³Na⁺; c) ³⁵Cl⁻; d) ²⁷Al³⁺.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. ²⁴Mg²⁺: Z = 12, así que 12 protones; neutrones = 24 − 12 = 12; electrones = 12 + 2 = 14.
2. ²³Na⁺: Z = 11, así que 11 protones; neutrones = 23 − 11 = 12; electrones = 11 − 1 = 10.
3. ³⁵Cl⁻: Z = 17, así que 17 protones; neutrones = 35 − 17 = 18; electrones = 17 + 1 = 18.
4. ²⁷Al³⁺: Z = 13, así que 13 protones; neutrones = 27 − 13 = 14; electrones = 13 − 3 = 10.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-02-05 "p n e; p n e; …"
```

## Q-02-06 · Tres elementos escondidos

Nivel 2 · sin ayuda (sin IA y sin pistas) · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

¿Quién soy? Cada acertijo es un elemento de número atómico 2 a 20 (del helio al calcio), y las pistas dejan un solo candidato: a) Tengo más de 13 protones. Estoy en el grupo 15. b) Tengo más de 15 protones. Soy un gas noble. c) Mi ion más común tiene carga 1+. Estoy en el periodo 2.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-02-06 "símbolo 1; símbolo 2; …"
```

## Q-02-07 · Protones, neutrones y electrones

Nivel 1 · sin ayuda (sin IA y sin pistas) · Bloque B: Estructura atómica: isótopos y tabla periódica (RD 217/2022)

El número de arriba a la izquierda es el número másico A (protones + neutrones); el de arriba a la derecha, la carga. Con la tabla periódica del libro, di cuántos protones, neutrones y electrones tiene cada uno: a) ³⁵Cl; b) ¹H; c) ⁵⁶Fe; d) ³⁹K.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-02-07 "p n e; p n e; …"
```

## Q-02-08 · Repaso: clasificar materiales

Nivel 1 · sin ayuda (sin IA y sin pistas) · Bloque B: Sistemas materiales: propiedades, composición y clasificación (RD 217/2022)

Clasifica cada material: elemento, compuesto, mezcla homogénea o mezcla heterogénea. a) oxígeno; b) arena con agua; c) agua destilada; d) vinagre; e) diamante (carbono); f) agua con aceite.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-02-08 "respuesta 1; respuesta 2; …"
```
