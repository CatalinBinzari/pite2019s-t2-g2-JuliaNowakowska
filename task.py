class Client:
    def __init__(self, name, ID, money):
        self.name = name
        self.ID = ID
        self.money = money

    def input_cash(self, money):
        more = int(input("How much money would you like to input?"))
        self.money += more

    def withdrawal_cash(self, money):
        less = int(input("How much money would you like to withdraw?"))
        self.money -= less

    def transfer(self, client2):
        print("You're transfering money from first Client to the second")
        transf = int(input("How much would you like to transfer?"))
        self.money = self.money - transf
        client2.money = client2.money + transf
        
class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.list_clients = []

    def adding_clients(self, client):
        self.list_clients.append(client)

    def show_clients(self, list_clients):
        for client in list_clients:
            print(client.name)
            print(client.ID)
            print(client.money)


#new clients
client1 = Client("Ola", 1, 2000)
client2 = Client("Ala", 2, 15000)
client3 = Client("Jurek", 3, 200)

#new bank
bank1 = Bank("mBank", "Krakow")

bank1.adding_clients(client1)
bank1.adding_clients(client2)
bank1.adding_clients(client3)

bank1.show_clients(bank1.list_clients)



