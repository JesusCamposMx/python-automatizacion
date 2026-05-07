def clasificar_venta(precio):
    if precio > 2000:
        return "Premium"
    elif precio > 1500:
        return "Estándar"
    else:
        return "Económica"
    
def resumen_venta(producto, precio):
    clasificacion = clasificar_venta(precio)
    return f"{producto} | ${precio} | {clasificacion}"
    
ventas = [
    {"producto": "Teclado", "precio": 250},
    {"producto": "Monitor", "precio": 2500},
    {"producto": "Mouse", "precio": 150},
    {"producto": "Microfono", "precio": 3500},
    {"producto": "Bocinas", "precio": 1800},
]

for venta in ventas:
    print(resumen_venta(venta["producto"], venta["precio"]))
     
    