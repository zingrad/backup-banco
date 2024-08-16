#!/bin/bash

# Define o caminho absoluto para o diretório do projeto
PROJECT_DIR="/c/xampp/htdocs/teste-backup"
PHP_PATH="/c/xampp/php/php.exe"
SCRIPT_PATH="$PROJECT_DIR/backup.php"

# Verifica se o arquivo PHP existe antes de tentar executá-lo
if [ -f "$SCRIPT_PATH" ]; then
    "$PHP_PATH" "$SCRIPT_PATH"
else
    echo "Erro: O script PHP não foi encontrado em $SCRIPT_PATH"
fi
