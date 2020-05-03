class SimpleCalculator:
	def __init__(self):
		pass

	def sum(self, num1, num2):
		if isinstance(num1, int) and isinstance(num2, int):
			return num1 + num2
		return 'ERROR'

	def divide(self, a, b):
		if b == 0:
			raise ZeroDivisionError
		return a / b
