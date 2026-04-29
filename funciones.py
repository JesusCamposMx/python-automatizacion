def aplicar_descuento(precio, porcentaje):
   return precio - (precio * porcentaje / 100)
    
def resumen_prenda(producto, precio, porcentaje):
    descuento = aplicar_descuento(precio, porcentaje)
    return f"{producto} | Precio Original: ${precio} | Descuento: {porcentaje}% | Precio final: ${descuento}"

prendas = [
    {"producto": "Pantalón", "precio": 800, "descuento": 30},
    {"producto": "Zapatos", "precio": 1200, "descuento": 40},
    {"producto": "Playera", "precio": 500, "descuento": 10},
    {"producto": "Gorra", "precio": 700, "descuento": 20},
    {"producto": "Lentes", "precio": 400, "descuento": 30}
]

for prenda in prendas:
    print(resumen_prenda(prenda["producto"], prenda["precio"], prenda["descuento"]))