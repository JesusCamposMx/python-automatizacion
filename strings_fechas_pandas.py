import pandas as pd
from datetime import datetime

df = pd.read_excel("ventas.xlsx")
hoy = datetime.now()

df["total"] = df["precio"] * df["cantidad"]

nombre_archivo = f'reporte_ventas_{hoy.strftime("%d_%m_%Y")}.xlsx'

with pd.ExcelWriter(nombre_archivo) as writer:
    df.to_excel(writer, sheet_name="Reporte ventas", index=False)
    
print(f'Reporte generado: {nombre_archivo}')