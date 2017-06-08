"""
Main.py

Author: Jose Lopez

		Numerical processing library prototype written in Python, with some optimizations in Cython, eventually.
"""

# Euclid's Algorithm to determine the Greatest Common Divisor
# Standard Python Modules
import sys


# Application Files
import number


# Parse command line arguments
if (len(sys.argv) > 1):
	print("Parsing command line options... ")
	
	if (len(sys.argv) == 3):
		m = int(sys.argv[1])
		n = int(sys.argv[2])

		g = number.getGCD_Wrapper(m,n);

		print("GCD(", m, ",", n, ") = ", g)
else:
	print("[No arguments passed in]")

