<?php
require("../mysql.php");
$number = basename(__FILE__, '.php');
$title = "";
$stmt = getTests("Bel");
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    if ($row["ID"] == $number) {
        $title = $row["Name"];
        break;
    }
}
require("../Templates/head.php");
?>
<?php
require("../Templates/foot.php");
?> 