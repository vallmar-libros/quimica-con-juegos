# Cómo escribir fórmulas y ecuaciones en la consola

Los programas leen lo que escribes con el teclado normal. Cuatro reglas:

1. **Números normales**, sin subíndices ni superíndices: `H2O`, no `H₂O` (si lo pegas con subíndices, también lo entiende).
2. **Cada símbolo empieza por mayúscula**: `CO` es carbono y oxígeno; `Co` sería el cobalto, que no está en la tabla del libro.
3. **Paréntesis** tal cual: `Ca(OH)2`, `Al2(SO4)3`.
4. **Cargas al final**: con carga 1+ o 1− detrás de un símbolo basta el signo (`Na+`, `Cl-`); en los demás casos, `^`, el número y el signo (`Fe^3+`, `SO4^2-`, `NH4^+`). `Fe3+` no vale: no se sabe si el 3 es un subíndice o la carga.

Escribe siempre la fórmula o la ecuación **entre comillas**. Ejemplos listos para copiar (desde la carpeta del repositorio):

- Una fórmula: números normales, sin subíndices:

```text
python programas/contar.py "H2O"
```

- Con paréntesis: el número de detrás multiplica todo lo de dentro:

```text
python programas/contar.py "Ca(OH)2"
```

- Con paréntesis, en una masa:

```text
python programas/masa.py "Al2(SO4)3"
```

- Un ion con carga 1+ o 1−: el signo al final:

```text
python programas/contar.py "Na+"
```

- Un ion con carga 2+, 3+, 2−…: ^, el número y el signo:

```text
python programas/contar.py "Fe^3+"
```

- Un ion de varios átomos:

```text
python programas/contar.py "SO4^2-"
```

- Un ion que acaba en número: siempre con ^:

```text
python programas/contar.py "NH4^+"
```

- Una ecuación: coeficiente, espacio, fórmula; + entre sustancias; -> como flecha:

```text
python programas/contar.py "2 H2 + O2 -> 2 H2O"
```

- Una ecuación con iones:

```text
python programas/contar.py "Cu + 2 Ag^+ -> Cu^2+ + 2 Ag"
```

- Del nombre a la fórmula:

```text
python programas/nombrar.py "óxido de hierro(III)"
```

- De la fórmula al nombre:

```text
python programas/nombrar.py "CuCl2"
```

Si el programa contesta «No lo entiendo», te dice por qué (por ejemplo, que falta el `^` de la carga).

Vuelve al [README](README.md).
