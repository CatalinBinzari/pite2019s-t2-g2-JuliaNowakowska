import unittest
from task import Client
from task import Bank


class TestClient(unittest.TestCase):
	print('\t\t\tPRINT 10 EVERYWHERE')
	def setUp(self):
		
		self.client_1=Client('John',123,550)
		self.client_2=Client('Marius',333,7.55)
	
	def test_input_cash(self):
		self.client_1.input_cash()
		self.client_2.input_cash()
		self.assertEqual(self.client_1.money,560)#input(10)
		self.assertEqual('Client {} is depositing cash'.format(self.client_1.name),
			'Client John is depositing cash')
		self.assertEqual('Client {} is depositing cash'.format(self.client_2.name),
			'Client Marius is depositing cash')
		self.assertIsInstance(self.client_1.name,str)
		self.assertEqual(self.client_2.money,17.55)
		

	def test_withdrawal_cash(self):
		self.client_1.withdrawal_cash()
		self.assertEqual(self.client_1.money,540)
		self.client_2.withdrawal_cash()
		self.assertEqual(self.client_2.money,7.55)
	def test_transfer(self):

		self.client_1.transfer(self.client_2)
		self.assertEqual(self.client_1.money,540)
		self.assertEqual(self.client_2.money,17.55)
		self.assertIsInstance(self.client_1,Client)
		self.assertIsInstance(self.client_2,Client)

	def test_bank_balance(self):
		self.client_1.bank_balance()
		self.assertEqual("Client {} bank balance: {}".format(self.client_1.name, self.client_1.money) ,"Client John bank balance: 550")

	def test_pay_debt(self):
		pass
class TestBank(unittest.TestCase):
	def setUp(self):
		self.client_1=Client('John',123,550)
		self.client_2=Client('Marius',333,7.55)
		self.b1 = Bank("mBank", "Krakow", 100000)
		self.b2 = Bank("PKO", "Warsaw", 700000)
		self.b3 = Bank("ING", "Katowice", 250000)
	def test__init__(self):
		self.assertIsInstance(self.b1,Bank)
		self.assertIsInstance(self.b1,Bank)
		self.assertIsInstance(self.b1,Bank)

		self.assertEqual(self.b1.name,'mBank')
		self.assertEqual(self.b2.city,'Warsaw')
		self.assertEqual(self.b3.capital,250000)
	def test_adding_clients(self):
		
		self.b1.adding_clients(self.client_1)
		
		self.b1.adding_clients(self.client_1)
		self.assertEqual(len(self.b1.list_clients),2)
	def test_show_clients(self):
		self.b1.show_clients()
		self.assertEqual("{}, {}, {}".format(self.client_1.name,self.client_1.ID,self.client_1.money),"John, 123, 550")
		self.assertEqual("{}, {}, {}".format(self.client_2.name,self.client_2.ID,self.client_2.money),"Marius, 333, 7.55")




if __name__ == '__main__':
	unittest.main()
