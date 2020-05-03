import unittest
from .. import square


class TestSquare(unittest.TestCase):
	def test_area(self):
		# Testing the method Square.Area()
		sq = square.Square(2)  # create a square of side 2 units

		# test if the area pf the above square is 4 units, display an error message if its not.
		self.assertEqual(sq.area(), 4, f'Area is shown {sq.area()} for side = {sq.side} units.')

	def test_area_negative(self):
		sq = square.Square(-3)
		self.assertEqual(sq.area(), -1, f'Area is shown {sq.area()} for side = {sq.side} units.')

	def test_perimeter(self):
		sq = square.Square(5)
		self.assertEqual(sq.perimeter(), 20, f'Perimeter is {sq.perimeter()} rather than 20')

	def test_perimeter_negative(self):
		sq = square.Square(-6)
		self.assertEqual(sq.perimeter(), -1, f'Perimeter is {sq.perimeter()} rather than -1')

if __name__ == '__main__':
	unittest.main()
