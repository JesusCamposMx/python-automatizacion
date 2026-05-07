import pandas as pd

df = pd.read_excel("inventario.xlsx")
filas_original = len(df)

df = df.dropna(subset=["codigo"])
print(df)

df["stock"] = df["stock"].fillna(0)
print(df)

df["precio_unitario"] = df["precio_unitario"].fillna(0)
print(df)

df = df.drop_duplicates()
print(df)

df["codigo"] = df["codigo"].str.capitalize()
print(df)

df["producto"] = df["producto"].str.capitalize()
print(df)
filas_final = len(df)
print(f"Filas originales: {filas_original} | Filas final: {filas_final}")

with pd.ExcelWriter("inventario_datos_limpios.xlsx") as writer:
    df.to_excel(writer, sheet_name="inventario_datos_limpios", index=False)