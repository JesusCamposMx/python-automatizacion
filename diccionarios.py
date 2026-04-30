cliente = {"nombre": "Jesús", "ciudad": "CDMX", "saldo":4000}

print(cliente["saldo"])

cliente["ciudad"] = "Queretaro"

cliente["vip"] = False

if cliente["saldo"] > 5000:
    cliente["vip"] = True
    
print(cliente)