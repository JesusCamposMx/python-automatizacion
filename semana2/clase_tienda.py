class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def disponibilidad(self):
        if self.stock > 0:
            return "Disponible"
        else:
            return "Agotado"
        
    def mostrar(self):
        print(f'{self.nombre} | ${self.precio} | Stock: {self.stock} | {self.disponibilidad()}')
        
producto1 = Producto("Pepsi", 20, 30)
producto1.mostrar()

producto2 = Producto("Pan Bimbo", 40, 10)
producto2.mostrar()

producto3 = Producto("Sabritas Naturales", 18, 0)
producto3.mostrar()

producto4 = Producto("Tortillas Tía Rosa", 32, 5)
producto4.mostrar()