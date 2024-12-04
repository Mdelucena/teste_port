import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# FUNCTION LOCALIZAR CAMPO DE TEXTO
def preencher_campo(seletor, valor):
    campo = driver.find_element(By.CSS_SELECTOR, seletor)
    campo.send_keys(valor)

# CLICK BUTTON
def clicar_botao(seletor):
    botao = driver.find_element(By.CSS_SELECTOR, seletor)
    botao.click()

# MEMORIA ELEMENTO
def esperar_elemento(seletor, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
        )
    except TimeoutException:
        print(f"Erro: O elemento {seletor} não apareceu após o tempo limite.")
        return None

# CONFING WEBDRIVE
driver = webdriver.Chrome()

try:
    # ACESSO
    driver.get("https://the-internet.herokuapp.com/login")
    print("A página de login foi acessada.")
    time.sleep(2) 

    # AUTOMAÇÃO 
    preencher_campo("#username", "tomsmith")
    print("Nome de usuário preenchido.")
    time.sleep(2)  

    preencher_campo("#password", "SuperSecretPassword!")
    print("Senha preenchida.")
    time.sleep(2)  
    
    # Clicar no botão de login
    clicar_botao("button[type='submit']")
    print("Botão de login clicado.")
    time.sleep(2)

    # CONFIRMAÇÃO
    success_message = esperar_elemento(".flash.success")
    if success_message:
        print(f"Login bem-sucedido! Mensagem de sucesso: {success_message.text}")
    
finally:
    # CLOSED
    print("Fechando o navegador...")
    driver.quit()


# pip install chromedriver-autoinstaller 
# dependência pip install webdriver-manager 