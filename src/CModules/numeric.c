
/** Function: Returns Greatest Common Denominator of (m,n)
 *
 *  	TODO: Need to add bounds checking to the function. There is no
 * 			  mechanism in place to deal with a divide by zero error right
 *  		  now.
 */

int getGCD(int m, int n) {
	int r = m % n;

	while (r != 0) {
		m = n;
		n = r;

		r = m % n;
	}

	return n;
}


/** Function: Returns Least Common Multiple of (m,n)
 *
 * 		TODO: Need to take care of the possibility of overflow
 *
 */

int getLCM(int m, int n) {
	int gcd = getGCD(m, n);

	return ((m * n) / gcd);
}