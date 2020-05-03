import unittest


class SimpleTest(unittest.TestCase):
	# returns True or False
	def test(self):
		self.assertTrue(True)


class TestStringMethods(unittest.TestCase):
	def setUp(self) -> None:
		pass

	# Returns True if the string contains 4 a
	def test_strings_a(self):
		self.assertEqual('a'*4, 'aaaa')

	# Return True if the string is in upper case
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	# Returns true if the string is in upper case else return False
	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	# Returns True if the string is stripped and matches the given output
	def test_strip(self):
		s = 'helloworld'
		self.assertEqual(s.strip('hello'), 'world')

	# Returns True if the string splits and matches the given output
	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)


if __name__ == '__main__':
	unittest.main()
