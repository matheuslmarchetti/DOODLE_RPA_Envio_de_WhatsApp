
from datetime import datetime


nome_cliente_da_base_comunicativos = 'base_comunicativos_ref_02_2024'
nome_do_relatorio_comunicativos = fr'relatorio_de_execucao_do_robo_do_cliente_{nome_cliente_da_base_comunicativos}_{datetime.today().strftime("%d_%m_%Y")}.xlsx'
nome_do_log_comunicativos = fr'log da base {nome_cliente_da_base_comunicativos} - gerado em {datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}'


caminho_da_base_comunicativos = fr'C:\Users\mlm15\Documents\Python\RPA\DOODLE_RPA_Envio_de_WhatsApp\bases\base_comunicativos.xlsx'
caminho_do_logs_comunicativos = fr'C:\Users\mlm15\Documents\Python\RPA\DOODLE_RPA_Envio_de_WhatsApp\logs\{nome_do_log_comunicativos}'
caminho_do_relatorio_de_execucao_comunicativos = fr'C:\Users\mlm15\Documents\Python\RPA\DOODLE_RPA_Envio_de_WhatsApp\relatorio_de_execucao\{nome_do_relatorio_comunicativos}'

def nome_cliente_da_base_comunicativos_fun():
    return nome_cliente_da_base_comunicativos

def nome_do_relatorio_comunicativos_fun():
    return nome_do_relatorio_comunicativos

def nome_do_log_comunicativos_fun():
    return nome_do_log_comunicativos

def caminho_da_base_comunicativos_fun():
    return caminho_da_base_comunicativos

def caminho_do_logs_comunicativos_fun():
    return caminho_do_logs_comunicativos


def caminho_do_relatorio_de_execucao_comunicativos_fun():
    return caminho_do_relatorio_de_execucao_comunicativos

print( caminho_do_relatorio_de_execucao_comunicativos_fun())