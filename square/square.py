class Square:
	def __init__(self, side):
		"""
		Creates a square having the given side
		:param side:
		"""
		self.side = side

	def area(self):
		"""
		Returns area of the square
		:return:
		"""
		if self.side < 0:
			return -1
		return self.side**2

	def perimeter(self):
		"""
		Returns perimeter of the square
		:return:
		"""
		if self.side < 0:
			return -1
		return 4 * self.side

	def __repr__(self):
		"""
		declares how square object should be printed
		:return:
		"""
		s = f'Square with side : {self.side} \nArea : {self.area()} \nPerimeter : {self.perimeter()}'
		return s


if __name__ == '__main__':
	# read input from user
	side = int(input('Enter the side length to create a square: '))

	# create a square with the provided side
	square = Square(side)

	# print the created square
	print(square)
