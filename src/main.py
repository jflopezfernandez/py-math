"""
Main.py

Author: Jose Lopez

		Numerical processing library prototype written in Python, with some optimizations in Cython, eventually.
"""

# Euclid's Algorithm to determine the Greatest Common Divisor

def getGCD(m, n):
	r = m % n;

	while (r != 0):
		m = n;
		n = r;

		r = m % n;

	return n;


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
		gcd = getGCD(self.numerator, self.denominator);

		if (gcd > 1):
			self.numerator = int(self.numerator / gcd);
			self.denominator = int(self.denominator / gcd);


a = Fraction(4,6);
b = Fraction(6,9);

print(a);
print(b);

c = a + b;

print(c);