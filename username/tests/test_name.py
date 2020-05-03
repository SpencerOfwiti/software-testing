import unittest
from ..names import formatted_name


class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		result = formatted_name('spencer', 'ofwiti')
		self.assertEqual(result, 'Spencer Ofwiti')

	def test_first_middle_last_name(self):
		result = formatted_name('raymond', 'reddington', 'red')
		self.assertEqual(result, 'Raymond Red Reddington')


if __name__ == '__main__':
	unittest.main()
