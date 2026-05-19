import requests

respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
print(respuesta.status_code)
print(respuesta.json())

datos = respuesta.json()
rates = datos["rates"]

print(f"USD a MXN: {rates['MXN']}")
print(f"USD a EUR: {rates['EUR']}")
print(f"USD a CAD: {rates['CAD']}")