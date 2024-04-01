from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import time
import pandas as pd
import os
import openpyxl
import logging
import pyautogui
from datetime import datetime
import script_relatorios
import script_caminhos

pyautogui.alert("""
    Bem-Vindo ao Doodle

    (RPA de Envio de Mensagens para WhatsApp)
                
        Este Módulo é para envio de mensgens das bases do comunicativos de:
                
                - Demanda de Ultrapassagem
                - Energia Reativa
                - Período Teste
                - Rural
                - Sazonal

    Ao final do processo você será avisado.


   Doodle 1.0.0v - Desenvolvido por Matheus L. Marchetti
""")

logging.basicConfig(level=logging.INFO, filename=script_caminhos.caminho_do_logs_comunicativos_fun(), format="%(asctime)s - %(levelname)s - %(message)s")
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--start-maximized")
caminho_drive = Service(os.path.abspath("drivechrome/msedgedriver.exe"))

navegador = webdriver.Edge(service=caminho_drive, options=edge_options)
navegador.get("https://web.whatsapp.com/")


# # esperar WhatsApp carregar
while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)
time.sleep(5)

# O WhatsApp já carregou
tabela = pd.read_excel(script_caminhos.caminho_da_base_comunicativos_fun())
time.sleep(2)



for linha in tabela.index:
    # enviar uma mensagem para a pessoa
    uc = tabela.loc[linha, "UC"]
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]
    tipo = tabela.loc[linha, "Tipo"]

    texto = mensagem.replace("fulano", nome)
    texto = urllib.parse.quote(texto)

    # enviar a mensagem
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
    time.sleep(2)

    navegador.get(link)
    # esperar a tela do WhatsApp carregar
    while len(navegador.find_elements(By.ID, 'app')) < 1:
        time.sleep(1)
    time.sleep(15)
    # verificar número válido e gera log
    time.sleep(20)
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) >= 1:
        #--------------------------------------------GERA LOG--------------------------------------------
        logging.info(f'O cliente: {nome} do tipo {tipo}, possui um telefone invalido, segue numero: {telefone}')
        #--------------------------------------------GERA LOG--------------------------------------------

        #--------------------------------------------GERA RELATÓRIO--------------------------------------------
        script_relatorios.gera_relatorio_comunicativos(nome, uc, tipo, telefone, 'Não Enviado', 'Telefone Inválido')
        #--------------------------------------------GERA RELATÓRIO--------------------------------------------
    time.sleep(20)

    # verificar número válido segue fluxo
    time.sleep(15)
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        # enviar a mensagem
        time.sleep(20)
        navegador.find_element(By.XPATH,
                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(
            Keys.ENTER)
        time.sleep(10)
        if arquivo != "N":
            caminho_completo = os.path.abspath(f"arquivos/{arquivo}")
            time.sleep(10)
            navegador.find_element(By.XPATH,
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/div/div/span').click()
            time.sleep(10)
            navegador.find_element(By.XPATH,
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li/div/input').send_keys(
                caminho_completo)
            time.sleep(10)
            navegador.find_element(By.XPATH,
                                   '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p').send_keys(
                Keys.ENTER)
        #--------------------------------------------GERA LOG--------------------------------------------
        logging.info(f'O cliente: {nome} do tipo {tipo} teve a mensagem encaminhada com sucesso!')
        #--------------------------------------------GERA LOG--------------------------------------------

        #--------------------------------------------GERA RELATÓRIO--------------------------------------------
        script_relatorios.gera_relatorio_comunicativos(nome, uc, tipo, telefone, 'Enviado', 'Telefone Válido')
        #--------------------------------------------GERA RELATÓRIO--------------------------------------------

        time.sleep(15)
navegador.close()
navegador.quit()
pyautogui.alert("""
    Processo de Automação Concluído!
""")