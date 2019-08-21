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

$title = "Error 401";
require("../Templates/head.php");
?>
<h1>Для доступа к данной странице необходима аунтефикация. Перезагрузице страницу или обратитесь за помощью.</h1>
<?php
require("../Templates/foot.php");
?>