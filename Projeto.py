# Automação de encaminhamneto de mensagens no whatsapp
# Usando a funcionalidade nativa do whatsapp de encaminhar mensagem
# Encaminhar de 5 em 5 mensagens

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")
