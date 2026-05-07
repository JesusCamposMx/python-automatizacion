import pandas as pd

df = pd.read_excel("ventas.xlsx")

print(df["producto"])        # una sola columna
print(df["precio"].sum())    # suma de todos los precios
print(df["precio"].mean())   # promedio
print(len(df))               # cuántas filas tiene

caros = df[df["precio"] > 500]
print(caros)

df["total"] = df["precio"] * df["cantidad"]
print(df)

with pd.ExcelWriter("reporte_ventas.xlsx") as writer:
    df.to_excel(writer, sheet_name="Ventas", index=False)
    caros.to_excel(writer, sheet_name="Solo caros", index=False)