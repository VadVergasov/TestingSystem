rmdir build /s /Q
rmdir __pycache__ /s /Q
rmdir dist /s /Q
set PYTHONOPTIMIZE=1
pyinstaller --log-level WARN --onefile --noupx --clean -y testmake.spec
rmdir build /s /Q
rmdir __pycache__ /s /Q
rmdir dist\log /s /Q
taskkill /F /IM explorer.exe
del %UserProfile%\AppData\Local\Microsoft\Windows\Explorer\iconcache*
start explorer.exe
xcopy /S /Q /Y %~dp0locale %~dp0dist\locale\
mkdir %~dp0dist\tests
