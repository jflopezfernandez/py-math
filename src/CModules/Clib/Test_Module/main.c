
#include "includes/Main.h"


extern int getGCD(int m, int n);


int main()
{
    int a,
		b;
	
	printf("Enter two numbers: ");
	scanf("%i %i", &a, &b);
	
	int result = getGCD(a,b);
	printf("Result: %i\n", result);
	

    return EXIT_SUCCESS;
}