# Retos · Capítulo 7. Detective de la IA

Retos Q-07-01 a Q-07-07. Las soluciones están en [soluciones/soluciones-cap-07.md](../soluciones/soluciones-cap-07.md). Antes de cualquier experimento, lee [SEGURIDAD.md](../SEGURIDAD.md).

## Q-07-01 · El chat cuenta átomos

Nivel 1 · práctica guiada · Bloque A: Interpretación de información científica: criterio propio (RD 217/2022)

¿Cuántos átomos de cada elemento hay en cada fórmula? ¿Y cuántos en total? a) O₂; b) H₂SO₄; c) Mg(NO₃)₂; d) Ca₃(PO₄)₂.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. O₂: 2 de O; en total, 2 átomos.
2. H₂SO₄: 2 de H, 1 de S y 4 de O; en total, 7 átomos.
3. Mg(NO₃)₂: 1 de Mg, 1 de N y 3 de O; en total, 5 átomos.
4. Ca₃(PO₄)₂: 3 de Ca, 2 de P y 8 de O; en total, 13 átomos.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-07-01 "respuesta 1; respuesta 2; …"
```

## Q-07-02 · El chat y la tabla

Nivel 2 · práctica guiada · Bloque A: Interpretación de información científica: criterio propio (RD 217/2022)

Masas a partir de la fórmula. Con las masas atómicas de la tabla del libro, calcula en unidades de masa atómica (u) la masa molecular de cada sustancia molecular o la masa de la unidad fórmula de cada compuesto iónico (los que llevan un metal). Di cuál de las dos es. Redondea a los decimales del dato menos preciso: a) MgO; b) H₂SO₄; c) CaCO₃.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. Masa de la unidad fórmula de MgO: M(MgO) = 24,305 + 15,999 = 40,304 u.
2. Masa molecular de H₂SO₄: M(H₂SO₄) = 1,008 + 32,06 + 4 · 15,999 = 97,06 u.
3. Masa de la unidad fórmula de CaCO₃: M(CaCO₃) = 40,078 + 12,011 + 3 · 15,999 = 100,086 u.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-07-02 "respuesta 1; respuesta 2; …"
```

## Q-07-03 · El chat y los números romanos

Nivel 2 · práctica guiada · Bloque A: Interpretación de información científica: criterio propio (RD 217/2022)

Nombra cada compuesto con la nomenclatura de Stock (número romano solo si el metal puede tener varios estados de oxidación): a) MgBr₂; b) PbO₂; c) FeO; d) K₂S.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. MgBr₂: el magnesio solo actúa con +2, así que no lleva número romano: bromuro de magnesio.
2. PbO₂: el plomo lleva subíndice 1, así que actúa con +1: óxido de plomo(I).
3. FeO: 1 óxido suma −2; el átomo de hierro debe sumar +2, así que actúa con +2: óxido de hierro(II).
4. K₂S: el potasio solo actúa con +1, así que no lleva número romano: sulfuro de potasio.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-07-03 "respuesta 1; respuesta 2; …"
```

## Q-07-04 · El chat junta iones

Nivel 2 · práctica guiada · Bloque A: Interpretación de información científica: criterio propio (RD 217/2022)

Cartas de iones: junta cada catión con su anión y escribe la fórmula del compuesto neutro (las cargas tienen que sumar cero): a) Fe²⁺ y Cl⁻; b) Al³⁺ y O²⁻; c) Al³⁺ y Cl⁻; d) Mg²⁺ y N³⁻.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. Fe²⁺ con Cl⁻: uno de cada, FeCl.
2. Al³⁺ con O²⁻: hacen falta 2 Al³⁺ (+6) y 3 O²⁻ (−6) para que las cargas sumen cero: Al₂O₃.
3. Al³⁺ con Cl⁻: hacen falta 1 Al³⁺ (+3) y 3 Cl⁻ (−3) para que las cargas sumen cero: AlCl₃.
4. Mg²⁺ con N³⁻: hacen falta 3 Mg²⁺ (+6) y 2 N³⁻ (−6) para que las cargas sumen cero: Mg₃N₂.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-07-04 "respuesta 1; respuesta 2; …"
```

## Q-07-05 · El chat ajusta

Nivel 3 · práctica guiada · Bloque E: Ecuaciones químicas: ajuste y estequiometría (4.º) (RD 217/2022)

Ajusta la ecuación con los coeficientes enteros más pequeños posibles: CH₄ + O₂ → CO₂ + H₂O.

**Con IA (opcional)** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-10.md](../instrucciones-ia/instrucciones-ia-2026-11-10.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la solución del chat imaginario que trae el reto: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. Sin coeficientes: izquierda C 1, H 4, O 2; derecha C 1, H 2, O 3.
2. Coeficientes 1, 3, 1, 2: CH₄ + 3 O₂ → CO₂ + 2 H₂O.
3. Comprobación: ya está ajustada.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-07-05 "coeficientes en orden"
```

## Q-07-06 · El chat cuenta moles

Nivel 3 · sin ayuda (sin IA y sin pistas) · Bloque B: Cuantificación de la cantidad de materia: número de moles (4.º) (RD 217/2022)

Tienes 32,1 g de metano (CH₄). Calcula su masa molar con la tabla y di cuántos moles son.

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. Masa molar de CH₄: M(CH₄) = 12,011 + 4 · 1,008 = 16,043 g/mol.
2. n = m · M = 32,1 g · 16,043 g/mol = 515 mol.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-07-06 "respuesta 1; respuesta 2; …"
```

## Q-07-07 · El chat prepara una disolución

Nivel 3 · sin ayuda (sin IA y sin pistas) · Bloque B: Sistemas materiales: disoluciones (4.º) (RD 217/2022)

Disuelves 30,0 g de azúcar en agua hasta tener 500 mL de disolución. ¿Cuál es la concentración en gramos por litro (g/L)?

Solución de un chat imaginario (la ha escrito un programa con un error a propósito). Tápala hasta tener tu propia resolución. Hay un paso equivocado, y los siguientes pueden arrastrar el error. ¿Cuál es el primero? ¿Por qué?

1. V = 500 mL, que uso tal cual: V = 500.
2. c = m : V = 30,0 g : 500 mL = 0,0600 g/L.

**Comprueba:** comprobar que cada respuesta contesta a lo que se pide y que es razonable; programa del repositorio.

```text
python programas/comprobar.py Q-07-07 "respuesta 1; respuesta 2; …"
```
