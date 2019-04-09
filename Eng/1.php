<?php
require('../postgresql.php');
$number = basename(__FILE__, '.php');
$title = '';
$stmt = getTests('Bel');
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    if ($row['ID'] == $number) {
        $title = $row['Name'];
        break;
    }
}
require('../Templates/head.php');
?>
<form action="check.php" method="post" autocomplete="off">
    <fieldset>
        <h2>Asd</h2>
        <ol>
            <li>
                <input type="checkbox" name="0" value="Asd">A</input>
            </li>
            <li>
                <input type="checkbox" name="1" value="Asd">s</input>
            </li>
            <li>
                <input type="checkbox" name="2" value="Asd">d</input>
            </li>
        </ol>
    </fieldset>
    <input type="submit" text="send" />
    <input type='text' hidden='true' value='<?php echo $number; ?>' name='number' />
</form>
<?php
require('../Templates/foot.php');
?>