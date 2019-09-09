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

$title = "Error 403";
require("../Templates/head.php");
?>
<h1><?php echo _("You are denied access to this part of the system."); ?></h1>
<?php
require("../Templates/foot.php");
?>