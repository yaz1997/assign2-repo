class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

    def __del__(self):
        print(f"Account {self.account_number} destroyed.")


class Customer:
    def __init__(self, name, age, address, account_number, balance, account_type):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(account_number, balance, account_type)

    def display_customer_info(self):
        print("Customer Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print("Account Information:")
        print(f"Account Number: {self.bank_account.account_number}")
        print(f"Account Type: {self.bank_account.account_type}")

    def __del__(self):
        print(f"Customer {self.name} destroyed.")


if __name__ == "__main__":
    customer1 = Customer("Gunjan", 22, "Sorhakhutte", "123456", 1000, "Savings")
    customer2 = Customer("Rojesh", 23, "Sorhakhutte", "789012", 2000, "Checking")

    customer1.bank_account.deposit(500)
    customer2.bank_account.withdraw(1000)

    customer1.display_customer_info()
    customer2.display_customer_info()

    del customer1
    del customer2
