"""Improvements: 16 transactions, loans' system, uses dictionary"""
import time

class Client:
	def __init__(self, name, ID, money):
		self.name = name
		self.ID = ID
		self.money = money
		self.debt = 0
		self.instalments = 0
        
	def input_cash(self):
		print( "\nClient {} is depositing cash".format(self.name) )
		more = int(input( "How much would you like to input?\t" ))
		self.money = round(self.money + more, 2)

	def withdrawal_cash(self):
		print( "\nClient {} is withdrawing cash".format(self.name) )
		less = int(input( "How much would you like to withdraw?\t" ))
		if self.money >= less:
		    self.money = round(self.money - less, 2)
		else:
			print( "Not enough money." )

	def transfer(self, client2):
		print("\nYou're transfering money from {} to {}".format(self.name, client2.name))
		transf = int(input("How much would you like to transfer?\t"))
		if transf <= self.money:
			self.money = round(self.money - transf, 2)
			client2.money = round(client2.money + transf,2)
		else: 
			print( "Not enough money" )
       
	def bank_balance(self):
		print( "Client {} bank balance: {}".format(self.name, self.money) )
		if self.debt > 0:
			print( "Current debt: {}".format(self.debt) )
			print( "Monthly instalment: {}".format(self.instalments))
		
	def pay_debt(self, bank):
		if (self.debt):
			if self.money >= self.debt:
				self.money -= self.instalments
				bank.capital += self.instalments
				self_debt = round(self.debt - self.instalments, 2)
				
				print( "\nInstalment paid. {}$ left".format(self.debt) )
				if self.debt == 0:
					self.instalments = 0
			else:
				print( "\nNot enough money to pay! Repo man is on his way" )
		else:
			print( "\nNo debt to pay" )
        
class Bank:
    def __init__(self, name, city, capital):
        self.name = name
        self.city = city
        self.capital = capital
        self.list_clients = []
        
    def adding_clients(self, client):
        self.list_clients.append(client)

    def show_clients(self):
        for client in self.list_clients:
            print( "{}, {}, {}".format(client.name, client.ID, client.money) )
	
    def credit(self, client):
        bank_rate = 0.07
        print( "\nClient {} is taking a loan in {} bank".format(client.name, self.name) )
        how_much = int(input( "How much do you need?\t" ))
        if (how_much < self.capital) and (client in self.list_clients):
            self.capital -= how_much
            client.debt += how_much + ( how_much * bank_rate )
            client.money += how_much
            how_long = int(input( "How many months do you need to pay money back?\t" ))
            if how_long > 0:
                client.instalments += round((how_much + (how_much * bank_rate)) / how_long, 2)
            else:
                print("You have to pay some day!")
                self.credit(client)
        else:
            print( "Bank {} can't borrow such amount of money.".format(self.name))
            print( "Not enough money or you're not client of the bank" )

		
		
def main():
	print("Welcome in the bank system!")
	
	#b1 = bank1 etc...
	b1 = Bank("mBank", "Krakow", 100000)
	b2 = Bank("PKO", "Warsaw", 700000)
	b3 = Bank("ING", "Katowice", 250000)
	
	#c1 = client1 etc...
	c1 = Client("Ola", 1, 2000)
	c2 = Client("Ala", 2, 15000)
	c3 = Client("Jurek", 3, 200)
	c4 = Client("Gaba", 4, 100000)
	c5 = Client("Iza", 5, 50)
	c6 = Client("Dawid", 6, 150)
	c7 = Client("Krzysztof", 7, 1200)
	c8 = Client("Jacek", 8, 8970)
	c9 = Client("Monika", 9, 9999)
	c10 = Client("Zofia", 10, 17500)
	c11 = Client("Jola", 11, 1234)
	c12 = Client("Iwona", 12, 75300)
	
	list1 = [c7, c8, c9, c10, c1, c5]
	list2 = [c2, c3, c6]
	list3 = [c4, c11, c12]
	b1.list_clients = list1
	b2.list_clients = list2
	b3.list_clients = list3

	print("\nHere's a list of {} clients: ".format(b1.name))
	b2.show_clients()
	
	#1
	c1.input_cash()
	c1.bank_balance()
	
	#2
	c1.transfer(c2)
	c1.bank_balance()
	c2.bank_balance()
	
	#3
	c6.withdrawal_cash()
	c6.bank_balance()
	
	#4
	b2.credit(c6)
	c6.bank_balance()
	
	#5
	c6.pay_debt(b2)
	c6.bank_balance()
	
	#6
	b2.credit(c6)
	c6.bank_balance()
	
	#7
	c6.pay_debt(b2)
	c6.bank_balance()
	
	#8
	c1.transfer(c12)
	c1.bank_balance()
	c12.bank_balance()
	
	#9
	c6.transfer(c4)
	c6.bank_balance()
	c4.bank_balance()
	
	#10
	b3.credit(c11)
	c11.bank_balance()
	
	#11
	c11.pay_debt(b3)
	c11.bank_balance()
	
	#12
	c8.withdrawal_cash()
	c8.bank_balance()
	
	#13
	c7.input_cash()
	c7.bank_balance()
	
	#14
	c10.transfer(c11)
	c10.bank_balance()
	c11.bank_balance()
	
	#15 - client wants to take a loan not from his/her bank
	b2.credit(c9)
	
	#16
	c2.input_cash()
	c2.bank_balance()
	
	
	print("\nDebtors:")
	
	list_banks = [b1, b2, b3]
	for bank in list_banks:
		for client in bank.list_clients:
			credit_info = {
				"Name: " : client.name,
				"Debt: " : client.debt,
				"Instalment: " : client.instalments,
			}

			if client.debt != 0:
				for key, value in credit_info.items():
					print(key, value)
					
	time.sleep(10)
	
if __name__ == "__main__":
	main()


