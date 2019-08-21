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

require("../postgresql.php");
if ($_GET["p"] == "") {
    $title = "Тесты";
    require("../Templates/head.php");
    ?>
<h2>Доступны тесты по следующим предметам:</h2>
<ol>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Bel">Белорусский</a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Math">Математика</a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Rus">Русский</a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Eng">Анлийский</a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Geo">География</a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Inf">Информатика</a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Phy">Физика</a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Bio">Биология</a></li>
</ol>
<?php
} else {
    if ($_GET["p"] == "Bel") {
        $title = "Белорусский язык";
    } else if ($_GET["p"] == "Eng") {
        $title = "Английский язык";
    } else if ($_GET["p"] == "Rus") {
        $title = "Русский язык";
    } else if ($_GET["p"] == "Math") {
        $title = "Математика";
    } else if ($_GET["p"] == "Inf") {
        $title = "Информатика";
    } else if ($_GET["p"] == "Geo") {
        $title = "География";
    } else if ($_GET["p"] == "Phy") {
        $title = "Физика";
    } else if ($_GET["p"] == "Bio") {
        $title = "Биология";
    }
    require("../Templates/head.php"); ?>
<script>
    function deleteTest(id) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                location.reload();
            }
        };
        xhttp.open("POST", "response.php", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("type=del&id=" + id.toString(10) + "&sub=<?php echo $_GET["p"]; ?>");
    }
</script>
<table style="width: 100%; font-size: 1.5em;">
    <tr>
        <th style="width: 25%; white-space: nowrap; font-weight: bold;">Название теста</th>
        <th style="width: 70%; font-weight: bold;">Описание теста</th>
        <th style="width: 5%; font-weight: bold;">Удаление теста</th>
    </tr>
    <?php
        $stmt = getTests($_GET["p"]);
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            echo "<tr><td style='font-weight: lighter;'>";
            ?><a href="http://<?php echo $site ?>/<?php echo $_GET["p"]; ?>/<?php echo $row['id'] ?>"><?php echo $row["name"]; ?></a>
    <?php echo "</td><td style='font-weight: lighter;'>";
            echo $row["description"];
            echo "</td><td><div style='text-align: center;'><input height=50 type='image' onclick='deleteTest(" . $row['id'] . ");' src='http://" . $site . "/Images/Delete.png'/></div></td></tr>";
        }
        ?>
</table>
<?php
}
?>
<?php
require("../Templates/foot.php");
?>