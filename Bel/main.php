<?php
$title = "Белорусский язык";
require("../Templates/head.php");
require("../mysql.php");
?>
<table style="width: 100%; font-size: 1.5em;">
    <tr>
        <th style="width: 1px; white-space: nowrap; font-weight: bold;">Название теста</th>
        <th style="font-weight: bold;">Описание теста</th>
    </tr>
    <?php
    $stmt = getTests("Bel");
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr><th style='font-weight: lighter;'>";
        echo $row["Name"];
        echo "</th><th style='font-weight: lighter;'>";
        echo $row["Description"];
        echo "</th></tr>";
    }
    ?>
</table>
<?php
require("../Templates/foot.php");
?> 