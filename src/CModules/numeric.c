
/** Assembly Procedures:
 * 	1. addInt_
 *
 */

extern int addInt_(int a, int b);


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


/** ----- ----- ----- ----- TEST FUNCTIONS ----- ----- ----- ----- */

/** Test Function: Print Debug Message
 *
 * 	Note: Function returns nothing. It is used solely for the purpose
 * 	 	  of verifying the the dll export/import configuration works
 * 		  as expected.
 *
 */

void testPrintDebug() {
	printf("[NUMERIC.C] Testing... \n");
}


/** ----- ----- ----- Assembly Procedure Wrappers: ----- ----- ----- */


/** Test Function: Add Two Integers
 *
 *  Note: This function is for testing purposes only. I'm using Microsoft
 *		  Macro Assembler instead of FASM here so I'm making sure that there 
 *	 	  aren't any compatibility issues, especially because I'm compiling
 * 		  this C unit as a Unix-style shared-object library.
 *
 * 		  I'm pretty sure this C wrapper nullifies any benefit to calling an
 * 		  assembly function in the first place because now there are two pointer
 * 		  lookups as opposed to just one. On the other hand, the procedure is so
 * 		  small any latency is too small to make a difference, most likely.
 *
 */

int asm_addInt(int a, int b) {
	int result = addInt_(a,b);

	return result;
}