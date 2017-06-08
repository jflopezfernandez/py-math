::@echo off

::ml /Gd /Fo ../CModules/addInt_ asm/addInt_.asm /W4
cd CModules
make

cd ..

python main.py