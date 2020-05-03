from fractions import Fraction
from json import load


def sum(arg):
	total = 0
	if isinstance(arg, int) or isinstance(arg, float):
		return 'Sum requires at least 2 variables'
	for val in arg:
		if isinstance(val, int) or isinstance(val, float) or isinstance(val, Fraction):
			total += val
		else:
			raise TypeError
	return total


class App:
	def __init__(self, database):
		self.customers = database['customers']

	def get_customer(self, id):
		for customer in self.customers:
			if customer['id'] == id:
				return customer
