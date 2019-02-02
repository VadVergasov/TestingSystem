rm -r build
rm -r __pycache__
rm -r dist
pyinstaller --icon data/icon/favico.ico --log-level=WARN --clean -y testmake.spec
rm -r build
rm -r __pycache__
rmdir dist/MakeTest/Crypto /s /Q
rmdir dist/MakeTest/cv2 /s /Q
rmdir dist/MakeTest/docutils /s /Q
rmdir dist/MakeTest/lib2to3 /s /Q
rmdir dist/MakeTest/numpy /s /Q
rmdir dist/MakeTest/PIL /s /Q
rmdir dist/MakeTest/scipy /s /Q
rmdir dist/MakeTest/win32com /s /Q
rmdir dist/MakeTest/Include /s /Q
rm dist/MakeTest/LICENSE*.txt
rm dist/MakeTest/lib*.*.dll
rm dist/MakeTest/api*.dll
rm dist/MakeTest/m*.dll
rm dist/MakeTest/win32*e*.pyd
rm dist/MakeTest/win32*u*.pyd
rm dist/MakeTest/_*l*.pyd
rm dist/MakeTest/_*b*.pyd
rm dist/MakeTest/_ctypes.pyd
rm dist/MakeTest/lib*i*.dll
rm dist/MakeTest/win32pdh.pyd
rm dist/MakeTest/unicodedata.pyd
rm dist/MakeTest/lib*p*g*.dll
rm dist/MakeTest/libFLAC-8.dll
rm dist/MakeTest/VCRUNTIME140.dll
rm dist/MakeTest/ucrtbase.dll
rm dist/MakeTest/libwebp-7.dll
rm dist/MakeTest/libogg-0.dll