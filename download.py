import os
import requests

from bs4 import BeautifulSoup

# URL base
base_url = 'http://200.152.38.155/CNPJ/'

# DiretÃ³rio para salvar os arquivos
directory = 'dados-publicos-zip'

# Cria a pasta dados se ela nÃ£o existir
if not os.path.exists(directory):
    os.makedirs(directory)

# Faz a requisiÃ§Ã£o e o parsing do HTML
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Percorre todos os links da pÃ¡gina
for link in soup.find_all('a'):

    # ObtÃ©m o caminho e nome do arquivo
    url = link.get('href')
    if url.endswith('.zip'):

        # Monta a URL completa
        if not url.startswith('http'):
            url = base_url + url

        # Faz o download do arquivo
        print(f'Download: {url}')
        response = requests.get(url)

        # Salva o arquivo na pasta dados
        filename = url.split('/')[-1]
        with open(os.path.join(directory, filename), 'wb') as f:
            f.write(response.content)
