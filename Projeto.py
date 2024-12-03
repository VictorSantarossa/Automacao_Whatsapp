# Automação de encaminhamneto de mensagens no whatsapp
# Usando a funcionalidade nativa do whatsapp de encaminhar mensagem
# Encaminhar de 5 em 5 mensagens

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip
import time

# Instalar e iniciar o WebDriver
service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)

# Abrir o WhatsApp Web
nav.get("https://web.whatsapp.com")
time.sleep(2)

mensagem = """Fala pessoal tudo bem?! estou me desenvolvendo em python!!!"""

# Enviar a mensagem para meu numero para poder depois encaminhar
lista_contatos = ["Meu Numero", "SÓ P SALVAR", "Victor (Santa Casa)", "Gabriel (Santa Casa)"]

# Clicar na lupa, rscrever Meu Numero e dar enter
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys("Meu Numero")
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.ENTER)
time.sleep(1)

# Escrever a mensagem para nós mesmos
pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

from selenium.webdriver.common.action_chains import ActionChains

qtde_contatos = len(lista_contatos)

if qtde_contatos % 5 == 0 :
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1
    
# rodar o codigo de encaminhar
for i in range(qtde_blocos):
   
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    # Selecionar a mensagem para enviar e abre a caixa de encaminhar
    lista_elementos = nav.find_element('class name', '_amlo')
    for item in lista_elementos:
        mensagem = mensagem.replace("\n","")
        texto = item.text.replace("\n","")
    if mensagem in texto:
        elemento = item
    
    # Selecionar a mensagem para enviar e abre a caixa de encaminhar

    # Selecionar a mensagem para enviar e abre a caixa de encaminhar
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', 'xyq7fz5').click()
    time.sleep(0.5)

    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[2]/span').click()
    time.sleep(1)

     # Selecionar os 5 contatos para enviar
    for nome in lista_enviar:
        
        # Escrever o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys("nome")
        time.sleep(1)

        # Dar enter
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.ENTER)
        time.sleep(1)

        # E apagar o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        
    nav.find_element('xpath' + '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3) 