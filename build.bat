xcopy /S/E /Q /Y %~dp0css %~dp0build\domains\TestingSystem\css\
xcopy /S/E /Q /Y %~dp0GetText %~dp0build\domains\TestingSystem\GetText\
xcopy /S/E /Q /Y %~dp0Images %~dp0build\domains\TestingSystem\Images\
xcopy /S/E /Q /Y %~dp0js %~dp0build\domains\TestingSystem\js\
xcopy /S/E /Q /Y %~dp0Locale %~dp0build\domains\TestingSystem\Locale\
xcopy /S/E /Q /Y %~dp0Pages %~dp0build\domains\TestingSystem\Pages\
xcopy /S/E /Q /Y %~dp0program\dist %~dp0build\domains\TestingSystem\program\dist\
xcopy /S/E /Q /Y %~dp0Templates %~dp0build\domains\TestingSystem\Templates\
copy /Y %~dp0index.php %~dp0build\domains\TestingSystem\index.php
copy /Y %~dp0postgresql.php %~dp0build\domains\TestingSystem\postgresql.php
copy /Y %~dp0start.bat %~dp0build\start.bat
mkdir %~dp0build\userdata
copy /Y %~dp0start.tpl.bat %~dp0build\userdata\start.tpl.bat
copy /Y %~dp0structure.sql %~dp0build\domains\TestingSystem\structure.sql
copy /Y %~dp0.htaccess %~dp0build\domains\TestingSystem\.htaccess
copy /Y %~dp0.htpasswd %~dp0build\domains\TestingSystem\.htpasswd
mkdir %~dp0build\domains\TestingSystem\Bel
mkdir %~dp0build\domains\TestingSystem\Eng
mkdir %~dp0build\domains\TestingSystem\Geo
mkdir %~dp0build\domains\TestingSystem\Inf
mkdir %~dp0build\domains\TestingSystem\Math
mkdir %~dp0build\domains\TestingSystem\Phy
mkdir %~dp0build\domains\TestingSystem\Rus
