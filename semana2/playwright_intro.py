from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    
    pagina.goto("https://books.toscrape.com")
    
    datos = []
    
    while True:
        elementos = pagina.locator("h3 a").all()
        
        for elemento in elementos:
            titulo = elemento.get_attribute("title")
            datos.append({"Titulo": titulo})
            
        if pagina.locator("li.next a").count() == 0:
            break
        else:    
         pagina.locator("li.next a").click()
        
    navegador.close() 
    
    df = pd.DataFrame(datos)
    df.to_excel("libros_playwright.xlsx", index=False)
    print(f'Se han exportado {len(df)} libros')