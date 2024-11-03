# Create a file that simulates a bank account that contains a account name, number, amount and interest rate
# Account can have money deposited and withdrawn as well as the interest rate adjusted.

class BankAcct():
    def __init__(self, name, account_number, initial_amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = initial_amount
        self.interest_rate = interest_rate

    # Method to adjust interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Method to deposit into account
    def deposit(self, amount):
        if amount >= 0:
            self.amount += amount
        else:
            print("Deposit amount must be greater than 0.")

    # Method to withdraw from account
    def withdraw(self, amount):
        if amount >= 0:
            if amount <= self.amount:
                self.amount -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Withdraw amount must be greater than 0.")

    # Method to retrieve current balance
    def get_balance(self):
        return self.amount

    # Calculate interest
    def calculate_interest(self, days):
        if days < 0:
            print("Number of days must be greater than or equal to 0.")
            return 0
        daily_interest_rate = self.interest_rate / 100 / 365
        interest = self.amount * daily_interest_rate * days
        return interest

    # Create a __str__ method to alter what is displayed when print(account) is run.
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2f}%")

def test_bank_acct():
    # Creating a bank account
    account = BankAcct("Avery Jones", "123456789", 3000.00, 6.0)

    # Displaying initial state
    print(account)

    # Testing deposit
    account.deposit(250)
    print("\nAfter depositing $250:")
    print(account)

    # Testing withdrawal
    account.withdraw(150)
    print("\nAfter withdrawing $150:")
    print(account)

    # Adjusting interest rate
    account.adjust_interest_rate(7.0)
    print("\nAfter adjusting interest rate to 7.0%:")
    print(account)

    # Calculating interest for 30 days
    interest = account.calculate_interest(30)
    print(f"\nInterest earned over 30 days: ${interest:.2f}")

# Run the test function
test_bank_acct()