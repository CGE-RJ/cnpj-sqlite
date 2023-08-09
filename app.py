import subprocess

# Chama o arquivo download.py
subprocess.run(["python", "download.py"])

# Chama o arquivo dados_cnpj_para_sqlite.py após o download.py terminar
subprocess.run(["python", "dados_cnpj_para_sqlite.py"])

# Chama o arquivo rede_cria_tabela.py após o dados_cnpj_para_sqlite.py terminar
subprocess.run(["python", "rede_cria_tabela.py"])

# Chama o arquivo cnpj_normaliza_enderecos.py após o rede_cria_tabela.py terminar
subprocess.run(["python", "cnpj_normaliza_enderecos.py"])
