rmdir build /s /Q
rmdir __pycache__ /s /Q
rmdir dist /s /Q
pyinstaller --icon=data\icon\favico.ico --log-level=WARN --clean -y testmake.spec
rmdir build /s /Q
rmdir __pycache__ /s /Q
rmdir dist\MakeTest\dist /s /Q
rmdir dist\MakeTest\log /s /Q
rmdir dist\MakeTest\build /s /Q
rmdir dist\MakeTest\__pycache__ /s /Q
rmdir dist\MakeTest\cv2 /s /Q
rmdir dist\MakeTest\Include /s /Q
rmdir dist\MakeTest\lib2to3 /s /Q
rmdir dist\MakeTest\win32com /s /Q
rmdir dist\MakeTest\numpy /s /Q
rmdir dist\MakeTest\docutils /s /Q
del dist\MakeTest\*.txt /s /Q
del dist\MakeTest\libopenblas.CSRRD7HKRKC3T3YXA7VY7TAZGLSWDKW6.gfortran-win_amd64.dll /Q
del dist\MakeTest\make.bat
del dist\MakeTest\main.py
del dist\MakeTest\testmake.spec