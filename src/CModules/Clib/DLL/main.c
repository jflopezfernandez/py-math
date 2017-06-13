
#include <stdio.h>
#include <stdlib.h>


__declspec(dllexport) void __cdecl testPrint() {
    printf("testing DLL function...\n");
}