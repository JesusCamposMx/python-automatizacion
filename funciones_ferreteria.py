def aplicar_iva(precio, iva):
    return precio + (precio * iva / 100)

def resumen_producto(producto, precio, iva):
    total = aplicar_iva(precio, iva)
    return f"Producto: {producto} | Precio sin IVA: ${precio} | IVA: {iva}% | Precio final: ${total}"

productos = [
    {"producto":"Martillo", "precio": 120, "iva": 16},
    {"producto":"Destornillador", "precio": 90, "iva": 16},
    {"producto":"Caja de clavos", "precio": 40, "iva": 16},
    {"producto":"Taladro", "precio": 920, "iva": 16},
    {"producto":"Cinta doble cara", "precio": 45, "iva": 16}
]

for producto in productos:
    print(resumen_producto(producto["producto"], producto["precio"], producto["iva"]))