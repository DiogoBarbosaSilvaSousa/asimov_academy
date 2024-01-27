from pathlib import Path
import os


def retorna_tamanho_dos_diretorios(caminho, profundidade = 1):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():            
           print('{} - {}'.format(arquivo.name,os.path.getsize(arquivo)))

caminho = Path.cwd()

retorna_tamanho_dos_diretorios(caminho)