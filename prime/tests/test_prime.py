import unittest
from ..primes import is_prime


class PrimesTestCase(unittest.TestCase):
	"""
	Tests for primes
	"""
	def test_is_five_prime(self):
		"""
		Is five correctly determined to be prime
		:return:
		"""
		self.assertTrue(is_prime(5))

	def test_is_string_prime(self):
		"""
		Is an error raised when string is passed
		:return:
		"""
		self.assertEqual(is_prime('hey'), 'IsPrime only takes integer parameters.')

	def test_is_zero_non_prime(self):
		"""
		Is five correctly determined to be prime
		:return:
		"""
		self.assertFalse(is_prime(0))

	def test_is_four_non_prime(self):
		"""
		Is four correctly determined not to be prime
		"""
		self.assertFalse(is_prime(4), msg='Four is not prime.')

	def test_negative_number(self):
		"""
		Is a negative number correctly determined not to be prime
		:return:
		"""
		self.assertFalse(is_prime(-3))


if __name__ == '__main__':
	unittest.main()
