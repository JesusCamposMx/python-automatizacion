def dividir(a,b):
    try:
        resultado = a/b
        return f"{a} / {b} = {resultado}"
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
    
    

valores = [
    {"a": 10, "b": 2},
    {"a": 8, "b": 0},
    {"a": 5.5, "b": 2.5}
]

for valor in valores:
    print(dividir(valor["a"],valor["b"]))
    