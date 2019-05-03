<?php
require("../postgresql.php");

if ($_POST['type'] == 'all') {
    $stmt = getHistory();
    echo "<tr><th style=' width: 25%;white-space: nowrap;font-weight: bold;'>IP адресс компьютера</th><th style='width: 40%;font-weight: bold;'>Статус</th><th style='font-weight: bold;'>Название теста</th></tr>";
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr><td>";
        echo $row['ip'];
        echo "</td><td>";
        echo $row['score'];
        echo "</td><td>";
        echo $row['test_name'];
        echo "</td></tr>";
    }
} else if ($_POST['type'] == 'clear') {
    clearHistory();
    echo "OK!";
}
