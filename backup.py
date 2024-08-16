import os
import subprocess
from datetime import datetime

# Configurações do banco de dados
host = 'localhost'
db = 'local_banco'

# Diretório do projeto
project_dir = os.path.dirname(os.path.abspath(__file__))

# Nome do arquivo de backup com data e hora
backup_file = os.path.join(project_dir, 'backup', f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.sql')

# Cria o diretório de backup se não existir
os.makedirs(os.path.dirname(backup_file), exist_ok=True)

# Comando para gerar o backup usando mysqldump
mysqldump_command = [
    'C:\\xampp\\mysql\\bin\\mysqldump.exe',
    f'--host={host}',
    f'--user={user}',
    f'--password={password}',
    db
]

# Redireciona a saída do comando para o arquivo de backup
with open(backup_file, 'wb') as f:
    process = subprocess.Popen(mysqldump_command, stdout=f, stderr=subprocess.PIPE)
    _, stderr = process.communicate()

# Verifica se o backup foi criado com sucesso
if process.returncode == 0:
    print(f"Backup criado com sucesso em: {backup_file}")
else:
    print(f"Erro ao criar o backup. Código de retorno: {process.returncode}")
    print(f"Saída de erro:\n{stderr.decode()}")