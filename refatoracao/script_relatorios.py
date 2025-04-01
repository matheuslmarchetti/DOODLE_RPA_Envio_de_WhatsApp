from datetime import datetime
import script_caminhos
import pandas as pd


def gera_relatorio_comunicativos(CLIENTE, UC, TIPO, TELEFONE, ENVIO, RESULTADO):
    try:
        df = pd.read_excel(script_caminhos.caminho_do_relatorio_de_execucao_comunicativos_fun())
        lista = []
    except Exception as e:
        print(e)
        colunas =['DATA_DE_EXECUCAO', 'CLIENTE', 'UC', 'TIPO', 'TELEFONE', 'ENVIO', 'RESULTADO']
        lista = []
        df = pd.DataFrame(columns = colunas)


    relatorio_do_robo = [datetime.today(), CLIENTE, UC, TIPO, TELEFONE, ENVIO, RESULTADO]
    lista.append(relatorio_do_robo)
    df = df._append(pd.DataFrame(lista, columns =df.columns), ignore_index=True)
    df.to_excel(script_caminhos.caminho_do_relatorio_de_execucao_comunicativos_fun(), index=False)