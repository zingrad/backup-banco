<?php
// Configurações do banco de dados
$host = 'localhost';
$db = 'local_banco';
// Deixe $user e $pass vazios se não houver autenticação, ou coloque as credenciais corretas
$user = 'erickgomes123'; // Ou o nome de usuário do MySQL, se houver
$pass = 'zingradgomes123'; // Ou a senha do MySQL, se houver

// Diretório do projeto
$projectDir = __DIR__;

// Nome do arquivo de backup com data e hora
$backupFile = $projectDir . '/backup/backup_' . date('Ymd_His') . '.sql';

// Verifica se o diretório de backup existe, senão, cria-o
if (!is_dir($projectDir . '/backup')) {
    mkdir($projectDir . '/backup', 0777, true);
}

// Comando para gerar o backup usando mysqldump
// Note que a opção --password está vazia se não houver senha
$command = "\"C:\\xampp\\mysql\\bin\\mysqldump.exe\" --host={$host} --user={$user} --password={$pass} {$db} > \"{$backupFile}\"";

// Executa o comando
exec($command . " 2>&1", $output, $return_var);

// Verifica se o backup foi criado com sucesso
if ($return_var === 0) {
    echo "Backup criado com sucesso em: {$backupFile}\n";
} else {
    echo "Erro ao criar o backup. Código de retorno: $return_var\n";
    echo "Saída do comando:\n" . implode("\n", $output) . "\n";
}
?>
