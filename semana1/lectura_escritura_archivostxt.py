def clasificar_cliente(saldo):
    if saldo > 10000:
        return "VIP"
    elif saldo > 3000:
        return "Regular"
    else:
        return "Nuevo"
    
def reporte_cliente(nombre, ciudad, saldo):
    tipo = clasificar_cliente(saldo)
    return f"Cliente: {nombre} | Ciudad: {ciudad} | Saldo: ${saldo} | Tipo: {tipo}"
        
clientes = [
{"nombre": "Mario", "ciudad": "Ciudad de México", "saldo": 5000,},
{"nombre": "Sandra", "ciudad": "San Luis Potosí", "saldo": 12000},
{"nombre": "Pedro", "ciudad": "Guadalajara", "saldo": 2500},
{"nombre": "Juan", "ciudad": "Monterrey", "saldo": 8200},
{"nombre": "Paola", "ciudad": "Tijuana", "saldo": 1200}
]



with open("reporte_cliente.txt", "w") as archivo:
    for cliente in clientes:
     archivo.write(reporte_cliente(cliente["nombre"], cliente["ciudad"], cliente["saldo"]) + "\n")
     

with open("reporte_cliente.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)