<?php
define('PROJECT_DIR', realpath('../'));
define('LOCALE_DIR', PROJECT_DIR . '\Locale');
define('DEFAULT_LOCALE', 'en');

require('../GetText/gettext.inc');

$encoding = 'UTF-8';

$locale = (isset($_POST['lang'])) ? $_POST['lang'] : DEFAULT_LOCALE;

T_setlocale(LC_MESSAGES, $locale);

T_bindtextdomain($locale, LOCALE_DIR);
T_bind_textdomain_codeset($locale, $encoding);
T_textdomain($locale);

require("../postgresql.php");

if ($_POST['type'] == 'all') {
    $stmt = getHistory();
    echo "<tr><th style=' width: 25%;white-space: nowrap;font-weight: bold;'>" . _("IP address") . "</th><th style='width: 40%;font-weight: bold;'>" . _("Status") . "</th><th style='font-weight: bold;'>" . _("Test name") . "</th></tr>";
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
} else if ($_POST['type'] == 'del') {
    deleteTest($_POST['sub'], $_POST['id']);
    unlink("../" . $_POST['sub'] . "/" . $id . ".php");
}
