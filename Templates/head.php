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
                $preloader.attr("hidden", true);
                $site = $('#site');
                $site.removeAttr("hidden");
            }, 300);
        });
    </script>
</head>

<body>
    <div class="loader">
        <div class="loader-inner">
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
            <div class="loader-line-wrap">
                <div class="loader-line"></div>
            </div>
        </div>
    </div>
    <div id="site" hidden>
        <nav id="nav">
            <ul>
                <li id="logo"><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>" style="padding: 0;"><img alt="Logo" src="../images/logo.png"></a></li>
                <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>" class="nava">Главная</a></li>
                <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/tests" class="nava">Тесты</a>
                    <ul>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Bel/main">Белорусский</a></li>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Math/main">Математика</a></li>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Rus/main">Русский</a></li>
                        <li><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Eng/main">Английский</a></li>
                    </ul>
                </li>
                <li style="float: right;"><a href="http://<?php echo $_SERVER['SERVER_NAME']; ?>/Pages/about" class="nava">Про систему</a></li>
            </ul>
        </nav>
        <div id="content"> 