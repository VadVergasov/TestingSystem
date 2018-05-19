<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title><?php echo($title);?></title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" media="screen" href="http://<?php echo $_SERVER['SERVER_NAME'];?>/css/main.css"/>
        <script src="http://<?php echo $_SERVER['SERVER_NAME'];?>/js/jquery.js"></script>
        <script>
            $(window).on('load', function(){
                setTimeout(function(){
                    $preloader = $('.loader');
                    $preloader.attr("hidden", true);
                    $site = $('#site');
                    $site.removeAttr("hidden");
                }, 1000);
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
                    <li><a href="http://<?php echo $_SERVER['SERVER_NAME'];?>">Главная</a></li>
                    <li><a href="http://<?php echo $_SERVER['SERVER_NAME'];?>/Pages/tests.php">Тесты</a>
                        <ul>
                            <li><a href="http://<?php echo $_SERVER['SERVER_NAME'];?>/Bel/main.php">Белорусский</a></li>
                            <li><a href="">Математика</a></li>        
                            <li><a href="">Русский</a></li>
                        </ul>
                    </li>
                    <li style="float: right;"><a href="http://<?php echo $_SERVER['SERVER_NAME'];?>/Pages/about.php">Про систему</a></li>
                </ul>
            </nav>
            <div id="content" style="width:100%;">