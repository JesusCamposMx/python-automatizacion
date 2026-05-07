ventas = [
    {"producto": "Teclado", "precio": 250},
    {"producto": "Monitor", "precio": 2500},
    {"producto": "Mouse", "precio": 150},
    {"producto": "Microfono", "precio": 3500},
    {"producto": "Bocinas", "precio": 1800},
]

venta_premium = 0

venta_estandar = 0

venta_economica = 0

total = 0

for venta in ventas:
    
    if venta["precio"] > 2000:
        clasificacion = "Venta Premium"
        venta_premium += 1
        
    elif venta["precio"] > 1500:
        clasificacion = "Venta Estándar"
        venta_estandar += 1
        
    else:
        clasificacion = "Venta Económica"
        venta_economica += 1
        
    print(f"Producto: {venta['producto']} | Precio: ${venta['precio']} | {clasificacion}")
    total += venta["precio"]
    
print (f"El total de la venta es: ${total}")
print(f"Venta Premium: {venta_premium}")
print(f"Venta Estándar: {venta_estandar}")
print(f"Venta Económica: {venta_economica}")