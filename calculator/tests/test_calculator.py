import unittest
from ..calculator import SimpleCalculator


class AdditionTestSuite(unittest.TestCase):
	def setUp(self):
		"""
		Executed before every test case
		:return:
		"""
		self.calculator = SimpleCalculator()

	def tearDown(self):
		"""
		Executed after every test case
		:return:
		"""
		print('\ntearDown executing after every test case. Result:')

	def test_addition_two_integers(self):
		result = self.calculator.sum(5, 6)
		self.assertEqual(result, 11)

	def test_addition_integer_string(self):
		result = self.calculator.sum(5, '6')
		self.assertEqual(result, 'ERROR')

	def test_addition_negative_integers(self):
		result = self.calculator.sum(-5, -6)
		self.assertEqual(result, -11)
		self.assertNotEqual(result, 11)


class DivisionTestSuite(unittest.TestCase):
	def setUp(self):
		"""
		Executed before every test case
		:return:
		"""
		self.calculator = SimpleCalculator()

	def test_divide_by_zero_exception(self):
		with self.assertRaises(ZeroDivisionError):
			self.calculator.divide(10, 0)


if __name__ == '__main__':
	unittest.main()
