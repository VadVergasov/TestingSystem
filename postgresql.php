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
    $sql = 'SELECT id, name, description FROM %s';
    $stmt = $db->prepare(sprintf($sql, $lang));
    $stmt->execute();
    return $stmt;
}

function getAns($lang, $testname)
{
    $db = init();
    $sql = 'SELECT answer FROM %1$s WHERE name=\'%2$s\'';
    $stmt = $db->prepare(sprintf($sql, $lang, $testname));
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC)["answer"];
}

function clearHistory()
{
    $db = init();
    $sql = 'TRUNCATE TABLE history';
    $stmt = $db->prepare($sql);
    $stmt->execute();
}

function getHistory()
{
    $db = init();
    $sql = 'SELECT * FROM history';
    $stmt = $db->prepare($sql);
    $stmt->execute();
    return $stmt;
}

function addToHistory($ip, $score)
{
    $db = init();
    $sql = 'INSERT INTO history("ip", "score") values (\'%1$s\', \'%2$s\')';
    $stmt = $db->prepare(sprintf($sql, $ip, $score));
    $stmt->execute();
}
