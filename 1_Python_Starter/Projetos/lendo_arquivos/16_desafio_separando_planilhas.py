from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

'''
tabela_clientes_dict = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx', sheet_name=None)

def separando_planilhas(caminho_planilha):    
    for nome_aba, tabela in tabela_clientes_dict.items():
        tabela.to_excel(caminho_planilha / f'{nome_aba}.xlsx', index=False)

pasta_separadas = pasta_atual / 'planilhas' / 'planilhas_separadas'
separando_planilhas(pasta_separadas)
'''

def consolidando_planilhas(caminho_planilha,planilhas_separadas):
    with pd.ExcelWriter(caminho_planilha) as consolidada:    
        for arquivo in Path(planilhas_separadas).glob('*.xlsx'):
            tabela = pd.read_excel(arquivo)
            tabela.to_excel(consolidada, sheet_name=arquivo.stem,index=False)

pasta_separadas = pasta_atual / 'planilhas' / 'planilhas_separadas'
planilha_consolidada = pasta_atual / 'planilhas' / 'planilha_consolidada' / 'clientes.xlsx'
consolidando_planilhas(planilha_consolidada,pasta_separadas)
