rmdir build /s /Q
rmdir __pycache__ /s /Q
rmdir dist /s /Q
set PYTHONOPTIMIZE=1
pyinstaller -i data\icon\favico.ico --log-level=WARN --clean -y --key=TestingSystem testmake.spec
rmdir build /s /Q
rmdir __pycache__ /s /Q
rmdir dist\MakeTest\Crypto /s /Q
rmdir dist\MakeTest\cv2 /s /Q
rmdir dist\MakeTest\docutils /s /Q
rmdir dist\MakeTest\lib2to3 /s /Q
rmdir dist\MakeTest\numpy /s /Q
rmdir dist\MakeTest\PIL /s /Q
rmdir dist\MakeTest\scipy /s /Q
rmdir dist\MakeTest\win32com /s /Q
rmdir dist\MakeTest\Include /s /Q
del dist\MakeTest\LICENSE*.txt
del dist\MakeTest\lib*.*.dll
del dist\MakeTest\api*.dll
del dist\MakeTest\m*.dll
del dist\MakeTest\win32*e*.pyd
del dist\MakeTest\win32*u*.pyd
del dist\MakeTest\_*l*.pyd
del dist\MakeTest\_*b*.pyd
del dist\MakeTest\_ctypes.pyd
del dist\MakeTest\lib*i*.dll
del dist\MakeTest\win32pdh.pyd
del dist\MakeTest\unicodedata.pyd
del dist\MakeTest\lib*p*g*.dll
del dist\MakeTest\libFLAC-8.dll
del dist\MakeTest\VCRUNTIME140.dll
del dist\MakeTest\ucrtbase.dll
del dist\MakeTest\libwebp-7.dll
del dist\MakeTest\libogg-0.dll