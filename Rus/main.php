<?php
$title = "Русский язык";
require("../Templates/head.php");
require("../postgresql.php");
?>
<table style="width: 100%; font-size: 1.5em;">
    <tr>
        <th style="width: 1px; white-space: nowrap; font-weight: bold;">Название теста</th>
        <th style="font-weight: bold;">Описание теста</th>
    </tr>
    <?php
    $stmt = getTests("Rus");
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr><th style='font-weight: lighter;'>";
        ?><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Rus/<?php echo $row['id'] ?>"><?php echo $row["name"]; ?></a>
        <?php echo "</th><th style='font-weight: lighter;'>";
        echo $row["description"];
        echo "</th></tr>";
    }
    ?>
</table>
<?php
require("../Templates/foot.php");
?>