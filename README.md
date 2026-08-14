Project 4 — Banking System

# Data to Store
- Accounts -> Account class

*Each account should contain:* -> Attributes for the Account class

Account Number
Name
Account Type (Current/Savings)
Current Balance
Status (Active/Frozen)
Transactions

*Methods*

Create an account -> method of Account class
Deposit money -> method of Account class
Withdraw money -> method of Account class (Prevent overdrafts)
Freeze an account -> method of Account class
Reactivate an account -> method of Account class
Generate a bank statement -> method of Account class
Show total deposits -> method of Account class
Show total withdrawals -> method of Account class
View transaction history -> method of Account class
View the last 10 transactions -> method of Account class


- Transaction -> Transaction class

*Each transaction should contain:* -> Attributes for the Transaction class

Transaction ID
Senders Account
Receivers Account
Date
Type
Amount
Balance After Transaction

# Features

Create an account -> method of Account class
Deposit money -> method of Account class
Withdraw money -> method of Account class (Prevent overdrafts)
Transfer money between accounts
Freeze an account -> method of Account class
Reactivate an account -> method of Account class
View transaction history -> method of Account class
View the last 10 transactions -> method of Account class
Show total deposits -> method of Account class
Show total withdrawals -> method of Account class
Generate a bank statement -> method of Account class
Every balance change must create a transaction record.
The balance should never be changed silently without a corresponding transaction being recorded.
