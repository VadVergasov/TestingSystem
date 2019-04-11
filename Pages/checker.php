<?php
require("../postgresql.php");
$title = "Результат";
require("../Templates/head.php");

$ans = getAns($_POST["Lang"], $_POST["Name"]);

$sizes = $_POST['Count'];
$not_right = 0;
$i = 0;
$pos = 0;

while ($_POST[strval($i)]) {
    $optionArray = $_POST[strval($i)];
    for ($j = 0; $j < count($optionArray); $j++) {
        if (strval($optionArray[$j]) != $ans[$pos + $j]) {
            $not_right++;
        }
    }
    $pos += $sizes[$i];
    $i++;
}

echo "<h1>" . ($pos - $not_right) / $pos * 100 . "%</h1>";

require("../Templates/foot.php");
