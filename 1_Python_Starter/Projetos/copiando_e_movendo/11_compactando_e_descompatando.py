from pathlib import Path
import shutil
import os

'''
# Compactando arquivos
pasta_atual = Path(__file__).parent
pasta_a_ser_compactada = pasta_atual
nome_arquivo = pasta_atual.parent / 'compactado'
shutil.make_archive(nome_arquivo, 'zip', pasta_a_ser_compactada)

# Movendo arquivos
caminho_arquivo = pasta_atual.parent / 'compactado.zip'
caminho_pasta_destino = pasta_atual

if  caminho_arquivo.exists():
    shutil.move(caminho_arquivo, caminho_pasta_destino)

'''

# Descompactando arquivos
pasta_atual = Path(__file__).parent
nome_arquivo = pasta_atual / 'compactado.zip'
pasta_descompactada = pasta_atual / 'descompactada'
shutil.unpack_archive(nome_arquivo,pasta_descompactada,'zip')
