rm -r build
rm -r __pycache__
rm -r dist
pyinstaller --icon=data\icon\favico.ico --log-level=WARN --clean -y testmake.spec
rm -r build
rm -r __pycache__
rm -r dist\MakeTest\dist
rm -r dist\MakeTest\log
rm -r dist\MakeTest\build
rm -r dist\MakeTest\__pycache__
rm -r dist\MakeTest\cv2
rm -r dist\MakeTest\Include
rm -r dist\MakeTest\lib2to3
rm -r dist\MakeTest\win32com
rm -r dist\MakeTest\numpy
rm -r dist\MakeTest\docutils
rm dist\MakeTest\*.txt
rm dist\MakeTest\libopenblas.CSRRD7HKRKC3T3YXA7VY7TAZGLSWDKW6.gfortran-win_amd64.dll
rm dist\MakeTest\make.bat
rm dist\MakeTest\make.sh
rm dist\MakeTest\main.py
rm dist\MakeTest\testmake.spec