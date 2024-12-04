from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def preencher_campo(seletor, valor):
    campo = driver.find_element(By.CSS_SELECTOR, seletor)
    campo.send_keys(valor)

def clicar_botao(seletor):
    botao = driver.find_element(By.CSS_SELECTOR, seletor)
    botao.click()

def esperar_elemento(seletor, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
        )
    except TimeoutException:
        print(f"Erro: O elemento {seletor} não apareceu após o tempo limite.")
        return None

# VERIFICAÇÃO
def verificar_arquivo(links, nome_arquivo):
    for link in links:
        if nome_arquivo in link.text:
            return True
    return False


driver = webdriver.Chrome()

try:
    # 1° ETAPA LOGIN
    driver.get("https://the-internet.herokuapp.com/login")
    print("A página de login foi acessada.")
    
    preencher_campo("#username", "tomsmith")
    preencher_campo("#password", "SuperSecretPassword!")
    
    
    clicar_botao("button[type='submit']")
    print("Botão de login clicado.")
    
    # WAIT SUCCESS
    esperar_elemento(".flash.success", 5)
    print("Login bem-sucedido.")
    
    # ACESSO A PAGE DOWNLOAD
    username = "admin"
    password = "admin"
    secure_url = f"https://{username}:{password}@the-internet.herokuapp.com/download_secure"
    

    driver.get(secure_url)
    print("A página de download seguro foi acessada com autenticação.")
    
    esperar_elemento("body", 10)
    
    # FIND FOLDERS
    links = driver.find_elements(By.PARTIAL_LINK_TEXT, ".")  
    
    # VERIFICAÇÃO
    nome_arquivo = "Write Excel Testdata2.csv"
    if verificar_arquivo(links, nome_arquivo):
        print(f"Arquivo encontrado: {nome_arquivo}")
    else:
        print("Arquivo não encontrado.")
    
   
    input("Pressione Enter para sair e fechar o navegador...")

finally:
    
    driver.quit()
