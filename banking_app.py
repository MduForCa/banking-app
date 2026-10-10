from decimal import Decimal

class Account:
    def __init__(self, balance=Decimal("0.00")):
        if not isinstance(balance, Decimal):
            raise TypeError("Balance must be a Decimal.")
        self.balance = balance

# Create the account object when the application starts
account = Account()

# Retrieve the account if it is availble
def retrieve_account():
    if account is not None:
        return account

    return None



