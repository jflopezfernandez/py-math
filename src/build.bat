::@echo off

cd asm
ml /Cx /Gd /Fo ..\CModules\addInt_.obj /c addInt_.asm /W4

cd ../CModules
make

cd ..

python main.py