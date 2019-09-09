<?php
define('PROJECT_DIR', realpath('../'));
define('LOCALE_DIR', PROJECT_DIR . '\Locale');
define('DEFAULT_LOCALE', 'en');

require('../GetText/gettext.inc');

$encoding = 'UTF-8';

$locale = (isset($_COOKIE['lang'])) ? $_COOKIE['lang'] : DEFAULT_LOCALE;

T_setlocale(LC_MESSAGES, $locale);

T_bindtextdomain($locale, LOCALE_DIR);
T_bind_textdomain_codeset($locale, $encoding);
T_textdomain($locale);

$title = "Error 401";
require("../Templates/head.php");
?>
<h1><?php echo _("To access this page, authentication is required. Reload the page or ask for help."); ?></h1>
<?php
require("../Templates/foot.php");
?>