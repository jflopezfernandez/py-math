"""
Main.py

Author: Jose Lopez

		Numerical processing library prototype written in Python, with some optimizations in Cython, eventually.
"""

# Euclid's Algorithm to determine the Greatest Common Divisor
# Standard Python Modules
import ctypes


# Application Files
import number


_gcd = ctypes.CDLL('libnum.so');
_gcd.getGCD.argtypes = (ctypes.c_int, ctypes.c_int)

print("Please enter two numbers: ")

a = int(input("m: "))
b = int(input("n: "))

def our_function(number1, number2):
	global _gcd

	result = _gcd.getGCD(ctypes.c_int(number1), ctypes.c_int(number2))

	return int(result)

g = our_function(a, b)
print("gcd = ", g)