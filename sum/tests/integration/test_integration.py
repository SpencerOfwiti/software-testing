import unittest
from ....sum import App

json_body = {
	"customers": [
		{
			"id": 1,
			"name": "Spencer",
			"address": "Kalimoni"
		},
		{
			"id": 2,
			"name": "Ofwiti",
			"address": "Juja"
		}
	]
}


class TestBasic(unittest.TestCase):
	def setUp(self):
		self.app = App(database=json_body)

	def test_customer_count(self):
		self.assertEqual(len(self.app.customers), 2)

	def test_existance_of_customer(self):
		customer = self.app.get_customer(id=2)
		self.assertEqual(customer['name'], "Ofwiti")
		self.assertEqual(customer['address'], "Juja")


if __name__ == '__main__':
	unittest.main()
