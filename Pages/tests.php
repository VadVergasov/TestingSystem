<?php
$title = "Тесты";
require("../Templates/head.php");
?>
<h2>Доступны тесты по следующим предметам:</h2>
<ol>
    <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Bel/main">Белорусский</a></li>
    <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Math/main">Математика</a></li>
    <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Rus/main">Русский</a></li>
    <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Eng/main">Анлийский</a></li>
</ol>
<?php 
require("../Templates/foot.php");
?> 