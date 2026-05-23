import pandas as pd
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    
    pagina.goto("https://books.toscrape.com/")
    
    datos = []
    
    while True:
        elementos = pagina.locator("article.product_pod").all()
        
        for elemento in elementos:
            titulo = elemento.locator("h3 a").get_attribute("title")
            precio = elemento.locator("p.price_color").inner_text()
            calificacion = elemento.locator("p.star-rating").get_attribute("class").split(" ")[1]
            datos.append({"Titulo": titulo, "Precio": precio, "Calificación": calificacion})
            
        if pagina.locator("li.next a").count() == 0:
            break
        else:
            pagina.locator("li.next a").click()
    navegador.close()
    
    df = pd.DataFrame(datos)
    df.to_excel("catalogo_libros_completo.xlsx", index=False)
    print(f'Se han exportado {len(df)} libros')