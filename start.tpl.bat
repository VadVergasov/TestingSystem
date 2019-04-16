@echo off
if exist %realprogdir%\userdata\run.txt (
    @echo OK
) else (
    %realprogdir%\modules\database\%pg_driver%\bin\psql.exe -U postgres < %realprogdir%\domains\TestingSystem\structure.sql
    @echo 1 > %realprogdir%\userdata\run.txt
)