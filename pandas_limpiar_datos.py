import pandas as pd

df = pd.read_excel("ventas_sucias.xlsx")
print(df)
print(df.info())
filas_original = len(df)

df = df.dropna(subset=["producto"])
print(df)

df["precio"] = df["precio"].fillna(0)
print(df)

df["cantidad"] = df["cantidad"].fillna(0)
print(df)

df["producto"] = df["producto"].str.capitalize()
print(df)

df = df.drop_duplicates()
print(df)
filas_final = len(df)
print(f"Filas originales: {filas_original} | Filas al final: {filas_final}")

with pd.ExcelWriter("ventas_limpias.xlsx") as writer:
    df.to_excel(writer, sheet_name= "Ventas limpias", index=False)