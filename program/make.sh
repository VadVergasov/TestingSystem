rm -r build
rm -r __pycache__
rm -r dist
pyinstaller --log-level WARN --onefile --noupx --clean -y testmake.spec
rm -r build
rm -r __pycache__
rmdir dist/log
cp -r locale dist/
mkdir dist/tests
