# Taller práctico: análisis de datos con Pandas

Programa de consola que lee datos de ventas y clientes, los limpia, los une y los analiza. Se ejecuta desde un menú en la terminal, y cada opción corresponde a un módulo que vas a completar paso a paso.

Recuerda consultar la guía adjunta en PDF donde se te dará el paso a paso del trabajo.

## Requisitos

- Python 3.10 o superior
- Git (para clonar el repositorio)
- Conocimientos básicos de variables, listas y funciones

## Cómo empezar

1. Clona el repositorio y entra a la carpeta del proyecto:

   ```
   git clone <URL-DEL-REPOSITORIO>
   cd <NOMBRE-DE-LA-CARPETA>
   ```

2. Crea y activa un ambiente virtual. Las instrucciones completas, para Windows y Mac/Linux, están en `LEEME_ambiente.txt`.

3. Instala las librerías:

   ```
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```
   python main.py
   ```

Ejecuta siempre los comandos desde la carpeta del proyecto. Los módulos buscan los archivos a partir de su ubicación.

## Estructura del proyecto

```
├── main.py            Menú principal. No lo modifiques.
├── carga.py           Lee los CSV. Ya está completo.
├── limpieza.py        Limpia clientes y ventas. TODO 1 a 5.
├── merge.py           Valida y une las tablas. TODO 6 y 7.
├── analisis.py        Responde las preguntas de negocio. TODO 8 a 12.
├── graficos.py        Dibuja dos gráficos sencillos. TODO 13 y 14.
├── exploracion.py     Ejemplos de indexación, .loc, .iloc y concat. Se ejecuta por separado.
├── requirements.txt   Versiones de las librerías.
├── LEEME_ambiente.txt Pasos para crear el ambiente virtual.
└── Data/
    ├── raw/           Datos originales (cliente.csv, ventas.csv). No los modifiques.
    └── processed/     Resultados que genera el programa.
```

## Menú

| Opción | Qué hace |
|---|---|
| 1 | Carga los archivos CSV |
| 2 | Limpia los datos |
| 3 | Valida y une las tablas con merge |
| 4 | Muestra el análisis y las respuestas del desafío |
| 5 | Dibuja los gráficos de introducción |
| 6 | Sale del programa |

Las opciones se usan en orden: primero cargar (1), luego limpiar (2), después unir (3) y finalmente analizar (4) o graficar (5).

## Cómo completar el taller

1. Abre el archivo indicado en cada TODO. Cada función tiene un docstring con pistas.
2. Completa el TODO y ejecuta `python main.py` para probar la opción correspondiente.
3. Usa `exploracion.py` para practicar indexación, `.loc`, `.iloc` y `concat()` antes de aplicarlos en tu código.

Las funciones que aún no completaste no dan error: devuelven los datos sin cambios, así que el menú siempre funciona.

## Entregables

Consulta el documento del taller (`guia_Taller_Pandas.pdf`) para ver el detalle de cada entregable y la rúbrica. En resumen:

- Entregable 0: pantallazo del ambiente virtual activo y de la instalación.
- Entregable 1: pantallazos de `.shape`, `.info()` y `.describe()`, y salida de `exploracion.py`.
- Entregable 2: limpieza, con pantallazos antes y después y explicación.
- Entregable 3: validación, merge y análisis, con pantallazos de las opciones 3 y 4.
- Entregable 4: los dos gráficos (`.png`) y el código de `graficos.py`.
- Desafío final: respuestas a las cinco preguntas, con el criterio usado en cada una.

Para entregar, agrega al final de este `README.md` una sección con tu nombre y tus respuestas a las preguntas del desafío. Sube tus cambios al repositorio y envía el enlace por el formulario de entrega. La entrega es individual.

## Preguntas de negocio

1. ¿Qué categoría genera más ingresos?
2. ¿Qué canal vende más?
3. ¿Los clientes VIP compran más que los Regulares?
4. ¿Qué método de pago es el más usado?
5. ¿Cuáles son los cinco clientes con más compras?


Alejandro Gomez Jimenez:

Evidencias
Los pantallazos están en la carpeta `images/`, una subcarpeta por entregable:
- `images/Entregable 0`: ambiente virtual e instalación
- `images/Entregable 1`: exploración
- `images/Entregable 2`: limpieza
- `images/Entregable 3`: merge y análisis
- `images/Entregable 4`: gráficos



Entregable 1: exploración

¿Por qué `.iloc[2, 6]` devuelve el total de la venta V003?
Después de `set_index("id_venta")`, `id_venta` deja de ser una columna y pasa a ser el índice. Contando desde 0, las columnas quedan: id_cliente (0), fecha_venta (1), producto (2), categoria (3), cantidad (4), precio_unitario (5) y total (6). La fila 2 es la tercera venta, V003. Por eso `.iloc[2, 6]` es el total de V003.

Entregable 2: limpieza

En `ventas.csv` encontré 1 valor nulo en la columna `producto` (venta V004). No usé `dropna()` porque esa venta tiene un total real de $780.000, y eliminarla alteraría los ingresos y el análisis. Por eso lo rellené con `fillna("Sin especificar")`.
No encontré filas duplicadas ni espacios sobrantes en ninguna de las dos tablas, pero dejé el código que los trata (`str.strip()`, `drop_duplicates()`). La columna `fecha_venta` venía como texto y la convertí a `datetime` con `pd.to_datetime(format="%Y-%m-%d")`. En `clientes.csv` apliqué `str.title()` a la ciudad.

Entregable 3: merge

¿Por qué el merge tiene 14 columnas?
`ventas` tiene 10 columnas y `clientes` tiene 5. Al unir queda 10 + 5 − 1 = 14, porque `id_cliente` está en las dos tablas y es la columna de unión, así que se conserva una sola vez. Las filas se mantienen en 68 (igual que ventas) porque usé `how="left"`, que conserva todas las ventas.


Desafío final

1. ¿Qué categoría genera más ingresos?

categoria
Tecnologia    14290000
Hogar          3653000
Papeleria       749000
Accesorios      484000
Name: total, dtype: int64

Respuesta: Tecnologia es la categoría que más ingresa, con $14.290.000.
Criterio: suma de la columna `total` por categoría, ordenada de mayor a menor.

### 2. ¿Qué canal vende más?
          ventas  ingresos
canal
Online      35  14669000
Tienda      33   4507000

Respuesta: el canal Online vende más.
Criterio: gana con los dos criterios, por cantidad de ventas (35 contra 33) y por ingresos ($14.669.000 contra $4.507.000).

3. ¿Los clientes VIP compran más que los Regulares?

clientes              compras  gasto_total  compras_por_cliente  gasto_por_cliente segmento_cliente
Regular                 36       39     11110000             1.083333      308611.111111
VIP                     24       29      8066000             1.208333      336083.333333

Respuesta: sí, los VIP compran un poco más por cliente: 1,21 compras y $336.083 de gasto, contra 1,08 compras y $308.611 de los Regulares.
Criterio: comparé el promedio por cliente y no los totales, porque hay 36 clientes Regulares y solo 24 VIP, y los totales no serían comparables.

4. ¿Qué método de pago es el más usado?

metodo_pago
Efectivo         30
Tarjeta          25
Transferencia    13
Name: count, dtype: int64

Respuesta: Efectivo es el método más usado, con 30 ventas.
Criterio: conteo de ventas por método de pago (`value_counts()`).

5. ¿Cuáles son los cinco clientes con más compras?

id_cliente nombre_cliente        compras  gasto_total

21         Nicolas Cardona         2      2515000
35         Matias Rodriguez        2      1278000
52         Mia Quintero            2      1090000
58         Luna Montoya            2      1007000
3          Luis Perez              2       730000

Respuesta: Nicolas Cardona, Matias Rodriguez, Mia Quintero, Luna Montoya y Luis Perez.
Criterio: ordené por número de compras y, como varios clientes empatan con 2 compras, usé el gasto total como desempate.

Bonus: ventas por mes

fecha_venta
2026-04    18234000
2026-05      942000
Freq: M, Name: total, dtype: int64

Respuesta: abril de 2026 fue el mes que más vendió, con $18.234.000