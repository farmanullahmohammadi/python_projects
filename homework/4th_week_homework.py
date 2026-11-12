class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class Account:

    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance")

        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount}")

    def show_balance(self):
        print("Balance:", self.balance)

    def save_transactions(self):
        with open("transactions.txt", "w", encoding="utf-8") as file:
            for transaction in self.transactions:
                file.write(transaction + "\n")


account = Account(1000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "4":
        break

    try:
        if choice == "1":
            amount = float(input("Enter amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.show_balance()
            continue

        else:
            print("Invalid menu option")
            continue

    except ValueError:
        print("Please enter a numeric amount")

    except InvalidAmountError as error:
        print(error)

    except InsufficientFundsError as error:
        print(error)

    else:
        print("Transaction successful")

    finally:
        print("Transaction attempt completed")

        try:
            account.save_transactions()
        except OSError:
            print("Could not save transaction records")

    account.show_balance()