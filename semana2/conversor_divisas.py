import requests

try:
    respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    datos = respuesta.json()
    rates = datos["rates"]
except:
    print("Error: no se pudo conectar a la API")
    
try:

    cantidad = float(input("¿Cuántos dólares quieres convertir?"))

    
    print(f'${cantidad:.2f} USD equivalen a:')

    mxn = cantidad * rates['MXN']
    print(f'MXN: ${mxn:.2f}')

    eur = cantidad * rates['EUR']
    print(f'EUR: ${eur:.2f}')

    cad = cantidad * rates['CAD']
    print(f'CAD: ${cad:.2f}')

except:
    print("Error: ingresa solo números. Ejemplo: 100 o 99.50")