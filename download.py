import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# URL base
base_url = 'http://200.152.38.155/CNPJ/'

# Diretório para salvar os arquivos
directory = 'dados-publicos-zip'

# Cria a pasta dados se ela não existir
if not os.path.exists(directory):
    os.makedirs(directory)

# Faz a requisição e o parsing do HTML
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra todos os links que terminam com .zip
zip_links = [link.get('href') for link in soup.find_all('a') if link.get('href').endswith('.zip')]

# Inicializa a barra de progresso global
total_bar = tqdm(total=len(zip_links), desc="Total Progresso")

for url in zip_links:
    if not url.startswith('http'):
        url = base_url + url
    filename = url.split('/')[-1]
    file_path = os.path.join(directory, filename)

    # Verifica se o arquivo já existe localmente
    if os.path.exists(file_path):
        total_bar.update(1)
        continue

    response = requests.head(url)
    total_length = int(response.headers.get('content-length', 0))

    # Inicializa a barra de progresso individual com o tamanho total do arquivo
    file_bar = tqdm(total=total_length, position=1, desc=f"Download: {filename}", unit="B", leave=False)

    with open(file_path, 'wb') as f:
        response = requests.get(url, stream=True)
        for data in response.iter_content(chunk_size=4096):
            f.write(data)
            file_bar.update(len(data))
    
    file_bar.close()
    total_bar.update(1)

total_bar.close()
print("Download concluído.")
