"""
	Number class

"""

# Standard Python Imports
import ctypes

_numeric = ctypes.CDLL('libnum.dll');

_numeric.getGCD.argtypes = (ctypes.c_int, ctypes.c_int)
_numeric.getLCM.argtypes = (ctypes.c_int, ctypes.c_int)

_numeric.asm_addInt.argtypes = (ctypes.c_int, ctypes.c_int)


def getGCD_Wrapper(number1, number2):
	global _numeric

	result = _numeric.getGCD(ctypes.c_int(number1), ctypes.c_int(number2))

	return int(result)

def getLCM_Wrapper(number1, number2):
	global _numeric

	result = _numeric.getLCM(ctypes.c_int(number1), ctypes.c_int(number2))

	return int(result)

def asm_addInt_Wrapper(number1, number2):
	global _numeric

	result = _numeric.asm_addInt(ctypes.c_int(number1), ctypes.c_int(number2))

	return int(result)

class Fraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator;
		self.denominator = denominator;

	def __str__(self):
		self.simplify();

		if (self.denominator == 0):
			print("[Error] Invalid number!");
		else:
			if (self.denominator == 1):
				return '{self.numerator}'.format(self=self);
			elif (self.numerator == 0):
				return '0';
			else:
				return '{self.numerator}/{self.denominator}'.format(self=self);

	def __add__(self, other):
		
		if (self.denominator == other.denominator):
			return Fraction(self.numerator + other.numerator, self.denominator);
		else:
			result_denominator = self.denominator * other.denominator;
			result_numerator = (self.numerator * other.denominator) + (self.denominator * other.numerator);

			result = Fraction(result_numerator, result_denominator);
			result.simplify();

			return result;

	def simplify(self):
		gcd = getGCD_Wrapper(self.numerator, self.denominator);

		if (gcd > 1):
			self.numerator = int(self.numerator / gcd);
			self.denominator = int(self.denominator / gcd);
