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
