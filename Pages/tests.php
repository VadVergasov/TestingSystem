<?php
define('PROJECT_DIR', realpath('../'));
define('LOCALE_DIR', PROJECT_DIR . '/Locale');
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
    $title = _("Tests");
    require("../Templates/head.php");
    ?>
<h2><?php echo _("Tests are available in the following subjects:"); ?></h2>
<ol>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Bel&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Belarussian"); ?></a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Math&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Math"); ?></a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Rus&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Russian"); ?></a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Eng&lang=<?php echo $_GET['lang'] ?>"><?php echo _("English"); ?></a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Geo&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Geography"); ?></a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Inf&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Informatics"); ?></a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Phy&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Physics"); ?></a></li>
    <li><a href="<?php echo $_SERVER["REQUEST_URI"]; ?>?p=Bio&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Biology"); ?></a></li>
</ol>
<?php
} else {
    if ($_GET["p"] == "Bel") {
        $title = _("Belarussian");
    } else if ($_GET["p"] == "Eng") {
        $title = _("English");
    } else if ($_GET["p"] == "Rus") {
        $title = _("Russian");
    } else if ($_GET["p"] == "Math") {
        $title = _("Math");
    } else if ($_GET["p"] == "Inf") {
        $title = _("Informatics");
    } else if ($_GET["p"] == "Geo") {
        $title = _("Geography");
    } else if ($_GET["p"] == "Phy") {
        $title = _("Physics");
    } else if ($_GET["p"] == "Bio") {
        $title = _("Biology");
    }
    require("../Templates/head.php"); ?>
<table style="width: 100%; font-size: 1.5em;">
    <tr>
        <th style="width: 25%; white-space: nowrap; font-weight: bold;"><?php echo _("Test name"); ?></th>
        <th style="font-weight: bold;"><?php echo _("Test description"); ?></th>
    </tr>
    <?php
        $stmt = getTests($_GET["p"]);
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            echo "<tr><td style='font-weight: lighter;'>";
            ?><a href="http://<?php echo $site ?>/<?php echo $_GET["p"]; ?>/<?php echo $row['id'] ?>"><?php echo $row["name"]; ?></a>
    <?php echo "</td><td style='font-weight: lighter;'>";
            echo $row["description"];
            echo "</td></tr>";
        }
        ?>
</table>
<?php
}
?>
<?php
require("../Templates/foot.php");
?>