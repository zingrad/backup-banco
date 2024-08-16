import os
import datetime
import subprocess
import json
import sys

# Caminho para o arquivo PHP de configuração
config_php = r'C:\xampp\htdocs\teste-backup\banco.php'

# Caminho para o executável PHP
php_path = r'C:\xampp\php\php.exe'

# Executa o arquivo PHP e captura a saída
def get_php_config():
    result = subprocess.run([php_path, config_php], capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        print("Erro ao ler o arquivo de configuração PHP.")
        print(result.stderr)
        sys.exit(1)

# Obtém as configurações do banco de dados do arquivo PHP
config = get_php_config()

# Configurações do banco de dados
host = config['host']
user = config['user']
password = config['password']
db = config['database']

# Diretório do projeto
project_dir = os.path.dirname(os.path.abspath(__file__))

# Nome do arquivo de backup com data e hora
backup_file = os.path.join(project_dir, 'backup', f'backup_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}_{db}.sql')

# Verifica se o diretório de backup existe, senão, cria-o
backup_dir = os.path.dirname(backup_file)
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Comando para gerar o backup usando mysqldump
command = [
    r'C:\xampp\mysql\bin\mysqldump.exe',  # Caminho para mysqldump
    '--host=' + host,
    '--user=' + user,
    '--password=' + password,
    db
]

# Executa o comando
with open(backup_file, 'wb') as f:
    result = subprocess.run(command, stdout=f, stderr=subprocess.PIPE)

# Verifica se o backup foi criado com sucesso
if result.returncode == 0:
    print(f"Backup criado com sucesso em: {backup_file}")
else:
    print(f"Erro ao criar o backup. Código de retorno: {result.returncode}")
    print("Saída do comando:")
    print(result.stderr.decode())
