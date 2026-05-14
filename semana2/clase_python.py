class Cliente:
    def __init__(self, nombre, ciudad, saldo):
        self.nombre = nombre
        self.ciudad =  ciudad
        self.saldo = saldo
        
    def clasificar(self):
        if self.saldo > 7000:
            return "VIP"
        elif self.saldo > 3000:
            return "Regular"
        else:
            return "Nuevo"
        
    def mostrar(self):
        print(f'{self.nombre} | {self.ciudad} | Saldo: ${self.saldo} | Tipo: {self.clasificar()}')
            
cliente1 = Cliente("Juan", "Queretaro", 8000)
cliente1.mostrar()
            
cliente2 = Cliente("Mario", "CDMX", 5000)
cliente2.mostrar()
            
cliente3 = Cliente("Sandra", "Monterrey", 2000)
cliente3.mostrar()