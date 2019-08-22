<?php
$site = $_SERVER['SERVER_NAME'];
if ($_SERVER['SERVER_PORT'] != 80) {
    $site .= ":" . $_SERVER['SERVER_PORT'];
}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title><?php echo ($title); ?></title>
    <link rel="shortcut icon" href="../images/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="http://<?php echo $site; ?>/css/main.css" />
    <script src="http://<?php echo $site; ?>/js/jquery.js"></script>
    <script>
        $(window).on('load', function() {
            setTimeout(function() {
                $preloader = $('.loader');
                $preloader.hide();
                $site = $('#site');
                $site.removeAttr("hidden");
            }, 500);
        });
    </script>
</head>

<body>
    <div class="loader">
        <div class="lds-roller">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>
    <div id="site" hidden>
        <nav id="nav">
            <ul>
                <li id="logo"><a href="http://<?php echo $site; ?>/?lang=<?php echo $_GET['lang'] ?>" style="padding: 0;"><img alt="Logo" src="../images/logo.png"></a></li>
                <li><a href="http://<?php echo $site; ?>/?lang=<?php echo $_GET['lang'] ?>" class="nava"><?php echo _("Main"); ?></a></li>
                <li><a href="http://<?php echo $site; ?>/Pages/tests?lang=<?php echo $_GET['lang'] ?>" class="nava"><?php echo _("Tests"); ?></a>
                    <ul>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Bel&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Belarussian"); ?></a></li>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Math&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Math"); ?></a></li>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Rus&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Russian"); ?></a></li>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Eng&lang=<?php echo $_GET['lang'] ?>"><?php echo _("English"); ?></a></li>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Geo&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Geography"); ?></a></li>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Inf&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Informatics"); ?></a></li>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Phy&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Physics"); ?></a></li>
                        <li><a href="http://<?php echo $site; ?>/Pages/tests?p=Bio&lang=<?php echo $_GET['lang'] ?>"><?php echo _("Biology"); ?></a></li>
                    </ul>
                </li>
                <li style="float: right;"><a href="?lang=be" class="lang"><img src="http://<?php echo $site; ?>/Images/belarus.png" height="50em" alt="Belarussian"></a></li>
                <li style="float: right;"><a href="?lang=ru" class="lang"><img src="http://<?php echo $site; ?>/Images/russia.jpg" height="50em" alt="Russian"></a></li>
                <li style="float: right;"><a href="?lang=en" class="lang"><img src="http://<?php echo $site; ?>/Images/english.png" height="50em" alt="English"></a></li>
                <li style="float: right;"><a href="http://<?php echo $site; ?>/Pages/about?lang=<?php echo $_GET['lang'] ?>" class="nava"><?php echo _("About"); ?></a></li>
            </ul>
        </nav>
        <div id="content">