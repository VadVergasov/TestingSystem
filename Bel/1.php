<?php
require('../postgresql.php');
$number = basename(__FILE__, '.php');
$title = '';
$stmt = getTests('Bel');
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    if ($row['id'] == $number) {
        $title = $row['name'];
        break;
    }
}
require('../Templates/head.php');
?>
<form action="../Pages/checker.php" method="post" autocomplete="off">    <input type="hidden" name="Lang" value="Bel"></input>    <input type="hidden" name="Name" value="Test"></input>    <fieldset>        <input type="hidden" name="Count[]" value="2"></input>        <h2>Русский работает?</h2>        <ol>            <li>                <input type="checkbox" name="0[]" value="1">Да</input>            </li>            <li>                <input type="checkbox" name="0[]" value="1">Нет</input>            </li>        </ol>    </fieldset>    <fieldset>        <input type="hidden" name="Count[]" value="3"></input>        <h2>ADS</h2>        <ol>            <li>                <input type="checkbox" name="1[]" value="1">A</input>            </li>            <li>                <input type="checkbox" name="1[]" value="1">D</input>            </li>            <li>                <input type="checkbox" name="1[]" value="1">S</input>            </li>        </ol>    </fieldset>    <input type="submit" text="send" /></form>
<?php
require('../Templates/foot.php');
?>