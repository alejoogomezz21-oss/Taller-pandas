import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)
    ventas_por_mes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    # TODO 8: calcular e imprimir los ingresos por categoría y la categoría que más ingresa.
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\n[P1] Ingresos por categoría:")
    print(ingresos)
    print(f"→ La categoría que más ingresa es {ingresos.index[0]} (${ingresos.iloc[0]:,.0f}).")


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    # TODO 9: calcular e imprimir ventas e ingresos por canal.
    canales = df.groupby("canal").agg(ventas=("id_venta", "count"), ingresos=("total", "sum"))
    print("\n[P2] Ventas e ingresos por canal:")
    print(canales)
    print(f"→ Por cantidad de ventas: {canales['ventas'].idxmax()} | Por ingresos: {canales['ingresos'].idxmax()}.")


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    # TODO 10: calcular e imprimir compras y gasto promedio por cliente según segmento_cliente.
    seg = df.groupby("segmento_cliente").agg(
        clientes=("id_cliente", "nunique"),
        compras=("id_venta", "count"),
        gasto_total=("total", "sum"),
    )
    seg["compras_por_cliente"] = seg["compras"] / seg["clientes"]
    seg["gasto_por_cliente"] = seg["gasto_total"] / seg["clientes"]
    print("\n[P3] VIP vs Regular (promedios por cliente):")
    print(seg)
    print(f"→ Más compras por cliente: {seg['compras_por_cliente'].idxmax()} | Más gasto por cliente: {seg['gasto_por_cliente'].idxmax()}.")


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    # TODO 11: calcular e imprimir el conteo por método de pago y cuál es el más usado.
    metodos = df["metodo_pago"].value_counts()
    print("\n[P4] Uso por método de pago:")
    print(metodos)
    print(f"→ El método más usado es {metodos.index[0]} ({metodos.iloc[0]} ventas).")


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    # TODO 12: calcular e imprimir el top 5.
    top = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .sort_values(["compras", "gasto_total"], ascending=False)
        .head(5)
    )
    print("\n[P5] Top 5 clientes con más compras:")
    print(top)

def ventas_por_mes(df):
    # BONUS
    por_mes = df.groupby(df["fecha_venta"].dt.to_period("M"))["total"].sum()
    print("\n[Bonus] Ventas por mes:")
    print(por_mes)
    print(f"→ El mes que más vendió fue {por_mes.idxmax()}.")
