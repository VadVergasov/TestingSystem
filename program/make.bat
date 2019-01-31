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
del dist\MakeTest\libopenblas.*.gfortran-win_amd64.dll /Q
del dist\MakeTest\make.bat
del dist\MakeTest\make.sh
del dist\MakeTest\main.py
del dist\MakeTest\testmake.spec
del dist\MakeTest\_bz2.pyd
del dist\MakeTest\_cffi_backend.pyd
del dist\MakeTest\*numpy*.pyd
del dist\MakeTest\_hashlib.pyd
del dist\MakeTest\_ssl.pyd
del dist\MakeTest\win32ui.pyd
del dist\MakeTest\mfc140u.dll
del dist\MakeTest\unicodedata.pyd
del dist\MakeTest\win32com.shell.shell.pyd
del dist\MakeTest\api-ms-win*.dll
del dist\MakeTest\win32file.pyd
del dist\MakeTest\cv2.cv2.pyd
del dist\MakeTest\win32gui.pyd
del dist\MakeTest\win32pdh.pyd
del dist\MakeTest\win32trace.pyd
del dist\MakeTest\win32wnet.pyd
del dist\MakeTest\_win32sysloader.pyd
del dist\MakeTest\libglib-2.0-0.dll
del dist\MakeTest\PIL._imaging.pyd
del dist\MakeTest\libgobject-2.0-0.dll
del dist\MakeTest\ucrtbase.dll
del dist\MakeTest\libintl-8.dll
del dist\MakeTest\PIL._imagingft.pyd
del dist\MakeTest\libgstreamer-1.0-0.dll
del dist\MakeTest\PIL._webp.pyd
del dist\MakeTest\libtiff-5.dll
del dist\MakeTest\libmodplug-1.dll
del dist\MakeTest\libwebp-7.dll
del dist\MakeTest\libFLAC-8.dll
del dist\MakeTest\libmpg123-0.dll
del dist\MakeTest\libvorbis-0.dll
del dist\MakeTest\_decimal.pyd
del dist\MakeTest\libffi-7.dll
del dist\MakeTest\libjpeg-9.dll
del dist\MakeTest\_elementtree.pyd
del dist\MakeTest\libgmodule-2.0-0.dll
del dist\MakeTest\_multiprocessing.pyd
del dist\MakeTest\libogg-0.dll