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
backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup')

# Nome do arquivo de backup com data
backup_filename = f'producao_{datetime.datetime.now().strftime("%Y%m%d")}_{db}.sql'
backup_sql_file = os.path.join(backup_dir, backup_filename)

# Verifica se o diretório de backup existe, senão, cria-o
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

# Substitui o backup do mesmo dia, se já existir
if os.path.exists(backup_sql_file):
    print(f"Backup já existe para o dia de hoje: {backup_sql_file}. Será substituído.")

# Executa o comando
with open(backup_sql_file, 'wb') as backup_file:
    result = subprocess.run(command, stdout=backup_file, stderr=subprocess.PIPE)

# Verifica se o backup foi criado com sucesso
if result.returncode == 0:
    print(f"Backup criado com sucesso em: {backup_sql_file}")
else:
    print(f"Erro ao criar o backup. Código de retorno: {result.returncode}")
    print("Saída do comando:")
    print(result.stderr.decode())
