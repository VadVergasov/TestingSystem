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

$title = "Error 404";
require("../Templates/head.php");
?>
<h1>Вы обратились по несуществющему адресу. Вернитесь назад или обратитесь к администратору.</h1>
<?php
require("../Templates/foot.php");
?>