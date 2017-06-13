
#include "includes/Main.h"


__declspec (dllexport) int getGCD(int m, int n) {
	int r = m % n;
	
	while (r != 0) {
		m = n;
		n = r;
		
		r = m % n;
	}
	
	return n;
}


__declspec (dllexport) int getLCM(int m, int n) {
	int gcd = getGCD(m,n);
	
	return ((m * n) / gcd);
}


