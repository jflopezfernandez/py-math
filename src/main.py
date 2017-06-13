"""
Main.py

Author: Jose Lopez

	Numerical processing library prototype written in Python, with optimizations in Cython, eventually.
"""

# Standard Python Modules
import sys
from ctypes import *

# Pylint Options
# pylint: disable=W0312,C0103,W0603

"""
	Pylint Options:
		-Disabled: 	W0312: Found indentation with tabs instead of spaces
					C0103: Invalid constant name
					W0603: Using global statement

	Pylint Error Codes: (http://pylint-messages.wikidot.com/all-codes)
"""



# Application Files
# import number

print(windll.libnum)

#numeric.getGCD.argtypes = (ctypes.c_int, ctypes.c_int)
#numeric.getLCM.argtypes = (ctypes.c_int, ctypes.c_int)

#numeric.asm_addInt.argtypes = (ctypes.c_int, ctypes.c_int)


def getGCD_Wrapper(number1, number2):
	"""
	Function calls C/assembly library to find GCD of the two passed-in
	parameters.
	"""

	global numeric

	#result = numeric.getGCD(ctypes.c_int(number1), ctypes.c_int(number2))

	#return int(result)

def getLCM_Wrapper(number1, number2):
	"""
	Function calls C/assembly library to get LCM of the two passed-in
	parameters. Function includes a call to getGCD.
	"""

	global numeric

	#result = numeric.getLCM(ctypes.c_int(number1), ctypes.c_int(number2))

	#return int(result)

def asm_addInt_Wrapper(number1, number2):
	"""
	Function makes a call to the C wrapper, which in turn calls the assembly function
	in the libnum.dll library.
	"""
	global numeric

	#result = numeric.asm_addInt(ctypes.c_int(number1), ctypes.c_int(number2))

	#return int(result)

class Fraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		self.simplify()

		if self.denominator == 0:
			print("[Error] Invalid number!")
		else:
			if self.denominator == 1:
				return '{self.numerator}'.format(self=self)
			elif self.numerator == 0:
				return '0'
			else:
				return '{self.numerator}/{self.denominator}'.format(self=self)

	def __add__(self, other):

		if self.denominator == other.denominator:
			return Fraction(self.numerator + other.numerator, self.denominator)
		else:
			result_denominator = self.denominator * other.denominator
			result_numerator = (self.numerator * other.denominator) + (self.denominator * other.numerator)

			result = Fraction(result_numerator, result_denominator)
			result.simplify()

			return result

	def simplify(self):
		"""
		Reduces the fraction if gcd(numerator,denominator) > 1
		"""

		#gcd = getGCD_Wrapper(self.numerator, self.denominator)

		"""
		if gcd > 1:
			self.numerator = int(self.numerator / gcd)
			self.denominator = int(self.denominator / gcd)
		"""

# Parse command line arguments
if len(sys.argv) > 1:
	print("Parsing command line options... ")

	if len(sys.argv) == 3:
		m = int(sys.argv[1])
		n = int(sys.argv[2])

		#g = numeric.getGCD_Wrapper(m, n)
		#l = numeric.getLCM_Wrapper(m, n)
		#a = numeric.asm_addInt_Wrapper(m, n)

		#print("GCD(", m, ",", n, ") = ", g)
		#print("LCM(", m, ",", n, ") = ", l)

		#print(m, " + ", n, " = ", a)

else:
	print("[No arguments passed in]")
