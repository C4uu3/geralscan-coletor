from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extrair_numero():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.tipminer.com/br/historico/pragmatic/auto-roleta")

    elemento = driver.find_element("css selector", ".cell__result")
    numero = int(elemento.text.strip())

    driver.quit()
    return numero
