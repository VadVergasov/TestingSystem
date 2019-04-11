<?php
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
    }
    require("../Templates/head.php"); ?>
    <table style="width: 100%; font-size: 1.5em;">
        <tr>
            <th style="width: 1px; white-space: nowrap; font-weight: bold;">Название теста</th>
            <th style="font-weight: bold;">Описание теста</th>
        </tr>
        <?php
        $stmt = getTests($_GET["p"]);
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            echo "<tr><th style='font-weight: lighter;'>";
            ?><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/<?php echo $_GET["p"]; ?>/<?php echo $row['id'] ?>"><?php echo $row["name"]; ?></a>
            <?php echo "</th><th style='font-weight: lighter;'>";
            echo $row["description"];
            echo "</th></tr>";
        }
        ?>
    </table>
<?php
}
?>
<?php
require("../Templates/foot.php");
?>