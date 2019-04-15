<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title><?php echo ($title); ?></title>
    <link rel="shortcut icon" href="../images/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/css/main.css" />
    <script src="http://<?php echo $_SERVER['SERVER_NAME']; ?>/js/jquery.js"></script>
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
                <li id="logo"><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>" style="padding: 0;"><img alt="Logo" src="../images/logo.png"></a></li>
                <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>" class="nava">Главная</a></li>
                <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/tests" class="nava">Тесты</a>
                    <ul>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/tests?p=Bel">Белорусский</a></li>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/tests?p=Math">Математика</a></li>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/tests?p=Rus">Русский</a></li>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/tests?p=Eng">Английский</a></li>
                    </ul>
                </li>
                <li style="float: right;"><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/about" class="nava">Про систему</a></li>
            </ul>
        </nav>
        <div id="content">