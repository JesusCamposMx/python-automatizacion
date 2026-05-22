from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina =  navegador.new_page()
    
    pagina.goto("https://the-internet.herokuapp.com/login")
    
    pagina.locator("#username").fill("tomsmith")
    pagina.locator("#password").fill("SuperSecretPassword!")
    pagina.locator("button.radius").click()
    
    exitoso = pagina.locator("#flash").inner_text().split("\n")[0].strip()
    print(exitoso)
    
    pagina.locator("a.secondary").click()
    
    pagina.wait_for_timeout(3000)
    navegador.close()