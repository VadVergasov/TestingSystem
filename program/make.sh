rm -r build
rm -r __pycache__
rm -r dist
pyinstaller --icon=data/icon/favico.ico --log-level=WARN --clean -y testmake.spec
rm -r build
rm -r __pycache__
rm -r dist/MakeTest/dist
rm -r dist/MakeTest/log
rm -r dist/MakeTest/build
rm -r dist/MakeTest/__pycache__
rm -r dist/MakeTest/cv2
rm -r dist/MakeTest/Include
rm -r dist/MakeTest/lib2to3
rm -r dist/MakeTest/win32com
rm -r dist/MakeTest/numpy
rm -r dist/MakeTest/docutils
rm dist/MakeTest/*.txt
rm dist/MakeTest/libopenblas.*.gfortran-win_amd64.dll
rm dist/MakeTest/make.bat
rm dist/MakeTest/make.sh
rm dist/MakeTest/main.py
rm dist/MakeTest/testmake.spec
rm dist/MakeTest/_bz2.pyd
rm dist/MakeTest/_cffi_backend.pyd
rm dist/MakeTest/*numpy*.pyd
rm dist/MakeTest/_hashlib.pyd
rm dist/MakeTest/_ssl.pyd
rm dist/MakeTest/win32ui.pyd
rm dist/MakeTest/mfc140u.dll
rm dist/MakeTest/unicodedata.pyd
rm dist/MakeTest/win32com.shell.shell.pyd
rm dist/MakeTest/api-ms-win*.dll
rm dist/MakeTest/win32file.pyd
rm dist/MakeTest/cv2.cv2.pyd
rm dist/MakeTest/win32gui.pyd
rm dist/MakeTest/win32pdh.pyd
rm dist/MakeTest/win32trace.pyd
rm dist/MakeTest/win32wnet.pyd
rm dist/MakeTest/_win32sysloader.pyd
rm dist/MakeTest/libglib-2.0-0.dll
rm dist/MakeTest/PIL._imaging.pyd
rm dist/MakeTest/libgobject-2.0-0.dll
rm dist/MakeTest/ucrtbase.dll
rm dist/MakeTest/libintl-8.dll
rm dist/MakeTest/PIL._imagingft.pyd
rm dist/MakeTest/libgstreamer-1.0-0.dll
rm dist/MakeTest/PIL._webp.pyd
rm dist/MakeTest/libtiff-5.dll
rm dist/MakeTest/libmodplug-1.dll
rm dist/MakeTest/libwebp-7.dll
rm dist/MakeTest/libFLAC-8.dll
rm dist/MakeTest/libmpg123-0.dll
rm dist/MakeTest/libvorbis-0.dll
rm dist/MakeTest/_decimal.pyd
rm dist/MakeTest/libffi-7.dll
rm dist/MakeTest/libjpeg-9.dll
rm dist/MakeTest/_elementtree.pyd
rm dist/MakeTest/libgmodule-2.0-0.dll
rm dist/MakeTest/_multiprocessing.pyd
rm dist/MakeTest/libogg-0.dll