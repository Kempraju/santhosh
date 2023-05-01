# mini project question number 05:
class Account:
    # Define an _init_ constructor method with attributes shared by all accounts:
    def _init_(self,acct_nbr,opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance=opening_deposit
    def _str_(self):
        return f'${self.balance:.2f}'
    def deposit(self,dep_amt):
        self.balance+=dep_amt
    def withdraw(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance-=wd_amt
        else:
            return 'Funds unavailable';


class Checking(Account):
    def _init_(self,acct_nbr,opening_deposit):
        super()._init_(acct_nbr,opening_deposit)
    def _str_(self):
        return f'Checking Account #{self.acct_nbr}\nBalance:{Account._str_(self)}';


class Savings(Account):
    def _init_(self,acct_nbr,opening_deposit):
        super()._init_(acct_nbr,opening_deposit)
    def _str_(self):
        return f'Savings Account #{self.acct_nbr}\nBalance: {Account._str_(self)}'

class Business(Account):
    def _init_(self,acct_nbr,opening_deposit):
        super()._init_(acct_nbr,opening_deposit)
    def _str_(self):
       return f'Business Account #{self.acct_nbr} \nBalance: {Account._str_(self)}'