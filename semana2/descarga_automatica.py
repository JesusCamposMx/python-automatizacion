from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context(accept_downloads=True)
    pagina = contexto.new_page()
    
    pagina.goto("https://the-internet.herokuapp.com/download")
        
    elementos = pagina.locator(".example a").all()
        
    for elemento in elementos:
        nombre = elemento.inner_text()
        with pagina.expect_download() as descarga_info:
            elemento.click()
    
        descarga = descarga_info.value
        descarga.save_as(f"descargas/{nombre}")
    navegador.close()