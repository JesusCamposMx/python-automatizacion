import pandas as pd
import requests
from bs4 import BeautifulSoup

respuesta = requests.get("https://books.toscrape.com/index.html")
respuesta.encoding = "utf-8"
soup = BeautifulSoup(respuesta.text, "html.parser")

libros = soup.find_all("article", class_="product_pod")

datos = []

for libro in libros:
    titulo = libro.find("h3").find("a")["title"]
    precio = libro.find("p", class_="price_color").text
    calificacion = libro.find("p", class_="star-rating")["class"][1]
    stock = libro.find("p", class_="instock").text.strip()
    datos.append({"titulo": titulo, "precio": precio, "calificacion": calificacion, "stock": stock})
    
df = pd.DataFrame(datos)
df.to_excel("libros_completo_scraping.xlsx", index=False)
print(f'Archivo generado con {len(df)} libros')