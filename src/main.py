"""
Main.py

Author: Jose Lopez

	Numerical processing library prototype written in Python, with optimizations in Cython, eventually.
"""

# Standard Python Modules
import sys
import time
#from ctypes import *

# Pylint Options
# pylint: disable=W0312,C0103,W0603

"""
	Pylint Options:
		-Disabled: 	W0312: Found indentation with tabs instead of spaces
					C0103: Invalid constant name
					W0603: Using global statement

	Pylint Error Codes: (http://pylint-messages.wikidot.com/all-codes)
"""

def timer(func, *args):
	"""
	Timing function for performance gauging
	"""

	start = time.clock()
	for i in range(1000):
		func(*args)
	return time.clock() - start

def printTimer(func, *args):
	"""
	Function that prints elapsed time
	"""

	t = timer(func, *args)
	print("Time Elapsed: ", t)

printTimer(print, "test")
