"""
Main.py

Author: Jose Lopez

		Numerical processing library prototype written in Python, with some optimizations in Cython, eventually.
"""

def getGCD(m, n):
	r = m % n;

	while (r != 0):
		m = n;
		n = r;

		r = m % n

	return n


class Fraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator;
		self.denominator = denominator;

	def __str__(self):
		self.simplify();
		return '{self.numerator}/{self.denominator}'.format(self=self);

	def simplify(self):
		gcd = getGCD(self.numerator, self.denominator);

		if (gcd > 1):
			self.numerator = int(self.numerator / gcd);
			self.denominator = int(self.denominator / gcd);


a = Fraction(6,8);
print(a)