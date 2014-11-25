#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

def rand_int(magnitude):
	return random.randint(10**(magnitude-1), 10**magnitude-1)

def gen_pair(magnitudeA, magnituteB, operator = '%'):
	return "{0} {2} {1} ==      ".format(rand_int(magnitudeA), rand_int(magnituteB), operator)

testcases = []
for x in xrange(0, 9):
	testcases.append(gen_pair(3, 3))

testcases.append(gen_pair(1, 1, '|'))
testcases.append(gen_pair(1, 1, '|'))
testcases.append(gen_pair(1, 2, '|'))
testcases.append(gen_pair(2, 2, '|'))
testcases.append(gen_pair(2, 2, '|'))
testcases.append(gen_pair(2, 2, '|'))

width = 29
counter = 0

print "-----------------------------------------------------------------------------------------"
print "Име:_____________________________________________________________________________________"
print
print "Номер: _______                                                              Клас: _______"
print "Всички числа са в десетична бройна система. Отговорите също трябва да са в нея."
print

for each in testcases:
	sys.stdout.write(each.rjust(width))
	counter = counter + 1
	if counter % 3 == 0:
		print
