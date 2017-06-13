@echo off

IF "%1" == "-B" (
    cd DLL
    make -B

    cd ..\Test_Module\
    make -B
) ELSE (
    cd DLL
    echo "[Building DLL]"
    make


    cd ..\Test_Module\
    echo "[Building Test Module Executable]"
    make

    cd ..
    echo "[Done.]"
)
