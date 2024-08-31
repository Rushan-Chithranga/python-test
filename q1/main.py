from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount, description):
        self.date = datetime.now().strftime("%d/%m/%Y")
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description

    def __str__(self):
        sign = '+' if self.transaction_type == 'Income' else '-'
        return f"{self.date}: {self.description}: {sign} Rs.{self.amount}"

class Budget:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0

    def add_transaction(self, transaction_type, amount, description):
        transaction = Transaction(transaction_type, amount, description)
        self.transactions.append(transaction)
        if transaction_type == 'Income':
            self.balance += amount
        else:
            self.balance -= amount

    def display_summary(self):
        income = sum(t.amount for t in self.transactions if t.transaction_type == 'Income')
        expenses = sum(t.amount for t in self.transactions if t.transaction_type != 'Income')
        summary = (
            f"Monthly Budget Summary:\n"
            f"Date: {datetime.now().strftime('%d/%m/%Y')}\n"
            f"Income: +Rs.{income}\n"
            f"Expenses: -Rs.{expenses}\n"
            f"Current Balance: Rs.{self.balance}\n"
            f"\nTransactions:"
        )
        print(summary)
        for transaction in self.transactions:
            print(transaction)

budget = Budget()

budget.add_transaction('Income', 100000, 'Deposit')
budget.add_transaction('Expense', 25000, 'Withdrawal')
budget.add_transaction('Expense', 35000, 'Transfer to Savings')
budget.add_transaction('Expense', 6000, 'Paid Electricity')
budget.add_transaction('Expense', 2500, 'Paid Water')
budget.add_transaction('Expense', 18000, 'Paid taxes')

budget.display_summary()
