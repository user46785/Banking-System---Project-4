import random


class Account:

    def __init__(self, name: str, account_type: str):
        self.account_number = f"{random.choice(range(1, 10000000000)):010}"
        self.name = name
        self.account_type = account_type
        self.current_balance = 0.0
        self.account_status = 'active'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        new_name = new_name.strip().lower()

        if not new_name:
            self.name = input("\nAccount Name cannot be blank, Enter Account name: ")

        elif new_name in ...:    
            self.name = input("\nAn Account already exists from this name please enter another name: ")

        else:
            self._name = new_name

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, new_account_type):
        new_account_type = new_account_type.strip().lower()

        if not new_account_type:
            self.account_type = input("\nAccount Type cannot be blank, Enter Account Type(Current/Savings): ")

        elif new_account_type not in ('savings', 'current'):
            self.account_type = input("\nPlease Enter valid Account Type(Current/Savings): ")

        else:
            self._account_type = new_account_type

    def __str__(self):
        return f"Account Number: {self.account_number}, Owner's Name: {self.name.title()}, Account Type: {self.account_type.title()}, Account Status: {self.account_status.title()}, Account Balance: ${self.current_balance}"

    @classmethod
    def get_account(cls):
        name = input("\nPlease enter your Name: ")
        account_type = input("\nPlease enter your Account Type(Current/Savings): ")

        new_account = Account(name, account_type)
        print(new_account)

        return new_account

    @classmethod
    def reuse_account(cls):
        ...
