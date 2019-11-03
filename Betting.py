#  lógica para o usuário fazer apostas
import sys


class UserAccount:

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def insert_credits(self, amount):
        self.balance += amount

    def check_credits(self):
        return self.balance

    def withdraw_credits(self, amount):
        if amount > self.balance:
            print("Error. Insuficiente credits: {}".format(self.balance))
            sys.exit(0)
        else:
            self.balance -= amount
            print("Withdraw: {}. Current balance: {}".format(amount, self.balance))


class MakeBet:
    def __init__(self, user):
        self.balance = user.get_balance()

    def make_bet(self, bet, team):
        if bet > self.balance:
            print("Insuficient founds. You have {}".format(self.balance))
            sys.exit(0)
        else:
            print("Bet of {} made with sucess on team {}".format(bet, team))