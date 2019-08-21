<?php
define('PROJECT_DIR', realpath('../'));
define('LOCALE_DIR', PROJECT_DIR . '\Locale');
define('DEFAULT_LOCALE', 'en');

require('../GetText/gettext.inc');

$encoding = 'UTF-8';

$locale = (isset($_GET['lang'])) ? $_GET['lang'] : DEFAULT_LOCALE;

T_setlocale(LC_MESSAGES, $locale);

T_bindtextdomain($locale, LOCALE_DIR);
T_bind_textdomain_codeset($locale, $encoding);
T_textdomain($locale);

$title = "Панель управления";
require("../Templates/head.php");
require("../postgresql.php");
?>
<script>
    function check() {
        var table = document.getElementById("main");

        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                table.innerHTML = this.responseText;
            }
        };
        xhttp.open("POST", "response.php", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("type=all");
    }

    window.setInterval(function() {
        check();
    }, 1000);
</script>
<button type="button" onclick="var x = new XMLHttpRequest();x.onreadystatechange = function() {if (this.readyState == 4 && this.status == 200) {return;}};x.open('POST', 'response.php', true);x.setRequestHeader('Content-type', 'application/x-www-form-urlencoded' ); x.send('type=clear');">Почистить историю</button>
<table id="main" style="width: 100%; font-size: 1.5em;">
    <tr>
        <th style="width: 25%; white-space: nowrap; font-weight: bold;">IP адресс компьютера</th>
        <th style="width: 40%;font-weight: bold;">Статус</th>
        <th style="font-weight: bold;">Название теста</th>
    </tr>
    <?php
    $stmt = getHistory();
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr><td>";
        echo $row['ip'];
        echo "</td><td>";
        echo $row['score'];
        echo "</td><td>";
        echo $row['test_name'];
        echo "</td></tr>";
    }
    ?>
</table>
<?php
require("../Templates/foot.php");
?>