import unittest
import pytest
from ... import sum
from fractions import Fraction


def test_sum():
	assert sum([1, 2, 3]) == 6, 'Should be 6'


def test_sum_tuple():
	assert sum((1, 2, 3)) == 6, 'Should be 6'


def test_sum_string():
	with pytest.raises(TypeError):
		sum([1, '2', 3])


def test_sum_floats():
	assert sum([1.2, 3.5, 3.8]) == 8.5, 'Should be 8.5'


def test_sum_single_val():
	assert sum(2.5) == 'Sum requires at least 2 variables'


def test_sum_negative():
	assert sum([1, -2, 3]) == 2, 'Should be 2'


def test_sum_fractions():
	data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
	assert sum(data) == Fraction(9, 10)


class TestSum(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(sum([1, 2, 3]), 6, 'Should be 6')

	def test_sum_tuple(self):
		self.assertEqual(sum((1, 2, 3)), 6, 'Should be 6')

	def test_sum_string(self):
		with self.assertRaises(TypeError):
			sum([1, '2', 3])

	def test_sum_float(self):
		self.assertEqual(sum([1.2, 3.5, 3.8]), 8.5, 'Should be 8.5')

	def test_sum_single_val(self):
		self.assertEqual(sum(2.5), 'Sum requires at least 2 variables')

	def test_sum_negative(self):
		self.assertEqual(sum([1, -2, 3]), 2)

	def test_sum_fractions(self):
		data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
		self.assertEqual(sum(data), Fraction(9, 10))


if __name__ == '__main__':
	unittest.main()
