import random


class Account:

    def __init__(self, name: str, account_type: str):
        self.account_number = f"{random.choice(range(1, 10000000000)):010}"
        self.name = name
        self.account_type = account_type
        self.current_balance = 0.0
        self.account_status = 'active'

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, new_account_number):
        if new_account_number in ...:
            self.account_number = f"{random.choice(range(1, 10000000000)):010}"
            
        else:
            self._account_number = new_account_number

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
    def create_account(cls) -> object:
        """
        Creates a new account object.

        :return: New object.
        """
        name = input("\nPlease enter your Name: ")
        account_type = input("\nPlease enter your Account Type(Current/Savings): ")

        new_account = Account(name, account_type)
        print(new_account)

        return new_account

    @classmethod
    def reuse_account(cls, account_number, name, account_type, current_balance, account_status) -> object:
        """
        Allows the user to reuse an account object without initializing.

        :return: Reusable object.
        """
        account = cls.__new__(cls)

        account.account_number = account_number
        account._name = name
        account._account_type = account_type
        account.current_balance = current_balance
        account.account_status = account_status

        return account

    def withdraw_from_account(self) -> None:
        """
        Decreases current balance amount.
        """
        if not self.account_status == 'active':
            print("\nThe account is freezed, Unfreeze account to withdraw.")

        else:
            while True:
                try:
                    amount = float(input("\nEnter ammount to withdraw in dollars: "))

                    if not amount:
                        print("\nNo amount entered.")

                    elif amount > self.current_balance:
                        print("\nInsufficient balance.")

                    else:
                        self.current_balance -= amount
                        print(f"\n${amount} withdrawn from account, remaining balance ${self.current_balance}")
                        break

                except ValueError:
                    print("\nPlease enter a valid amount.")

    def deposit_from_account(self) -> None:
        """
        Increases current balance amount.
        """
        if not self.account_status == 'active':
            print("\nThe account is freezed, Unfreeze account to deposit.")
        
        else:
            while True:
                try:
                    amount = float(input("\nEnter ammount to deposit in dollars: "))

                    if not amount:
                        print("\nNo amount entered.")

                    else:
                        self.current_balance += amount
                        print(f"\n${amount} deposited to account, new balance ${self.current_balance}")
                        break

                except ValueError:
                    print("\nPlease enter a valid amount.")

    def freeze_account(self) -> None:
        """
        Sets account status to unactive.
        """
        if not self.account_status == 'active':
            print("\nThe account is already freezed.")

        else:
            while True:
                confirmation = input("\nAre you sure you want to freeze your account?(Yes/No): ").strip().lower()

                if confirmation == 'yes':
                    self.account_status = 'unactive'
                    print("\nAccount Freezed.")
                    break 

                elif confirmation == 'no':
                    print("\nAccount will remain Active.")
                    break

                else:
                    print("\nPlease enter Yes or No.")

    def reactivate_account(self) -> None:
        """
        Sets account status to active.
        """
        if self.account_status == 'active':
            print("\nThe account is already Active.")
        
        else:
            while True:
                confirmation = input("\nAre you sure you want to Activate your account?(Yes/No): ").strip().lower()

                if confirmation == 'yes':
                    self.account_status = 'active'
                    print("\nAccount Activated.")
                    break 

                elif confirmation == 'no':
                    print("\nAccount will remain Freezed.")
                    break

                else:
                    print("\nPlease enter Yes or No.")
