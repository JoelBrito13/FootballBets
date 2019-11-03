from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    description = models.TextField(blank=True)
    balance = models.FloatField()

    def __str__(self):
        return "User(<{}>)".format(self.username)

#  lógica para o usuário fazer apostas


    def get_balance(self):
        return self.balance

    def insert_credits(self, amount):
        self.balance += amount

        def check_credits(self):
            return self.balance

        def withdraw_credits(self, amount):
            if amount > self.balance:
                return Exception("Error. Insuficiente credits: {}".format(self.balance))
            else:
                self.balance -= amount
                print("Withdraw: {}. Current balance: {}".format(amount, self.balance))

class MakeBet:
    def __init__(self, user):
        self.balance = user.get_balance()

    def make_bet(self, bet, team):
        if bet > self.balance:
            return Exception("Insuficient founds. You have {}".format(self.balance))
        else:
            print("Bet of {} made with sucess on team {}".format(bet, team))
