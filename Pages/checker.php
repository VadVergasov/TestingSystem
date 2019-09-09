<?php
define('PROJECT_DIR', realpath('../'));
define('LOCALE_DIR', PROJECT_DIR . '\Locale');
define('DEFAULT_LOCALE', 'en');

require('../GetText/gettext.inc');

$encoding = 'UTF-8';

$locale = (isset($_COOKIE['lang'])) ? $_COOKIE['lang'] : DEFAULT_LOCALE;

T_setlocale(LC_MESSAGES, $locale);

T_bindtextdomain($locale, LOCALE_DIR);
T_bind_textdomain_codeset($locale, $encoding);
T_textdomain($locale);

require("../postgresql.php");
$title = "Результат";
require("../Templates/head.php");

$ans = getAns($_POST["Lang"], $_POST["Name"]);

$all = substr_count($ans, "1");
$sizes = $_POST['Count'];
$right = 0;
$not_right = 0;
$i = 0;
$pos = 0;

while ($_POST[strval($i)]) {
    $optionArray = $_POST[strval($i)];
    for ($j = 0; $j < count($optionArray); $j++) {
        if ($ans[$pos + $optionArray[$j]] == "1") {
            $right++;
        } else if ($ans[$pos + $optionArray[$j]] == "0") {
            $not_right++;
        }
    }
    $pos += $sizes[$i];
    $i++;
}

$score = max(0, $right) / $all * 100;

addToHistory($_SERVER["REMOTE_ADDR"], "Правильных:" . $right . " из " . $all . " Не правильных: " . $not_right, $_POST['Name']);
echo "<h1>Правильных ответов: " . $right . " из " . $all . "</h1>";
echo "<h1>Не правильных ответов: " . $not_right . "</h1>";

require("../Templates/foot.php");
