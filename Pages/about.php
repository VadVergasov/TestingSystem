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

$title = _("About");
require("../Templates/head.php");
?>
<h1><?php echo _("This test system was developed by Vadim Vergasov (VadVergasov), specially for the gymnasium №29 of Minsk. This test system can be used in other schools with the agreement of the author. Also a condition for use in other school is a link to the developer and the gymnasium."); ?>
</h1>
<?php
require("../Templates/foot.php");
?>