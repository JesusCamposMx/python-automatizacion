class Empleado:
    def __init__(self, nombre, departamento, salario):
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
        
    def categoria(self):
        if self.salario > 20000:
            return "Senior"
        elif self.salario > 12000:
            return "Mid"
        else:
            return "Junior"
        
    def mostrar(self):
        print(f'{self.nombre} | {self.departamento} | ${self.salario} | {self.categoria()}')
        
empleado1 = Empleado("Raúl", "Finanzas", 25000)
empleado1.mostrar()

empleado2 = Empleado("Sofía", "Marketing", 20000)
empleado2.mostrar()

empleado3 = Empleado("Pedro", "Logística", 15000)
empleado3.mostrar()

empleado4 = Empleado("Mónica", "Recursos Humanos", 12000)
empleado4.mostrar()