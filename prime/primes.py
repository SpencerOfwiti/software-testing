import math


def is_prime(a):
	"""
	Return True if number is prime
	:param a:
	:return:
	"""
	if isinstance(a, int):
		if a <= 1:
			return False
		for i in range(2, math.floor(math.sqrt(a) + 1)):
			if a % i == 0:
				return False
		return True
	return 'IsPrime only takes integer parameters.'


def print_next_prime(a):
	"""
	Print the closest prime number larger than number
	:param a:
	:return:
	"""
	index = a
	while True:
		index += 1
		if is_prime(index):
			return index


def sum_of_primes(arg):
	"""
	Print sum of prime numbers in parameter
	:param arg:
	:return:
	"""
	return sum([x for x in arg if is_prime(x)])
