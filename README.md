# Automação de Backup para Projetos XAMPP

Este script em Python automatiza o processo de backup para bancos de dados MySQL em projetos que utilizam o XAMPP. Ele extrai as configurações do banco de dados diretamente de um arquivo PHP (`banco.php`), gerando um arquivo `.sql` no diretório especificado.

---

## Funcionalidades

- Lê configurações do banco de dados diretamente de um arquivo PHP.
- Gera backups automáticos utilizando o `mysqldump`.
- Organiza os backups em uma pasta configurável.
- Nomeia os arquivos de backup com base na data e hora para facilitar o gerenciamento.

---

## Pré-requisitos

1. **XAMPP** instalado em sua máquina.
2. **Python 3.x** configurado.
3. Caminho do executável do **PHP** e do **mysqldump** corretamente configurados.

---

## Configuração

### 1. Crie o arquivo PHP de configuração do banco de dados

Salve o código abaixo como `banco.php` em um diretório acessível pelo XAMPP:

```php
<?php
header('Content-Type: application/json');

// Configurações do banco de dados
$config = [
    'host' => 'localhost',
    'user' => 'root',
    'password' => '',
    'database' => 'local_banco',
];

// Retorna as configurações em formato JSON
echo json_encode($config);
?>
```
### Uso

#### Navegue até o diretório do script:

#### cd caminho/para/o/diretorio
#### Execute o script:


#### python backup.py ou py backup.py
##### O backup será gerado na pasta backup, dentro do mesmo diretório do script.

### Resultado

##### Um arquivo .sql será gerado no seguinte formato:

##### producao_YYYYMMDD_HHMMSS_nome_do_banco.sql

### Exemplo:

##### producao_20241120_153045_local_banco.sql
