import pandas as pd

df = pd.read_excel("clientes.xlsx")
filas_original = len(df)

df = df.dropna(subset=["nombre"])
print(df)

df = df.dropna(subset=["ciudad"])
print(df)

df["saldo"] = df["saldo"].fillna(0)
print(df)

df = df.drop_duplicates()
print(df)

df["nombre"] = df["nombre"].str.title()
print(df)

df["ciudad"] = df["ciudad"].str.capitalize()
print(df)
filas_final = len(df)
print(f"Filas originales: {filas_original} | Filas final: {filas_final}")

with pd.ExcelWriter("clientes_datos_limpios.xlsx") as writer:
    df.to_excel(writer, sheet_name="clientes_datos_limpios", index=False)