from datetime import datetime

meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

hoy = datetime.now()

mes_espanol = meses[hoy.month]

print(hoy.strftime("%d/%m/%Y"))
print(hoy.strftime("%d-%m-%Y"))
print(f"Reporte del mes de {mes_espanol} {hoy.year}")
print(f"reporte_{hoy.strftime("%d_%m_%Y")}.xlsx")