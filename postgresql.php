<?php
function init()
{
    try {
        $db = 'Tests';
        $host = 'localhost';
        $username = 'TestingSystem';
        $password = 'postgresql';
        $dsn = "pgsql:host=$host;dbname=$db";
        $opt = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];
        $db = new PDO($dsn, $username, $password, $opt);
        return $db;
    } catch (PDOException $e) {
        echo $e->getMessage();
    }
}

function getTests($lang)
{
    $db = init();
    $sql = 'SELECT * FROM %s';
    $stmt = $db->prepare(sprintf($sql, $lang));
    $stmt->execute();
    return $stmt;
}
