
#include "includes/Main.h"


extern int getGCD(int m, int n);
extern int getLCM(int m, int n);


int main()
{
    int a,
		b;
	
	printf("Enter two numbers: ");
	scanf("%i %i", &a, &b);
	
	int gcd = getGCD(a,b);
	printf("GCD: %i\n", gcd);
	
	int lcm = getLCM(a,b);
	printf("LCM: %i\n", lcm);
	

    return EXIT_SUCCESS;
}