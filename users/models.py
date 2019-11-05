from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    description = models.TextField(blank=True)
    balance = models.FloatField(
        null=False,
        default=0
    )

    def insert_credits(self, amount):
        self.balance += amount

    def withdraw_credits(self, amount):
        if amount > self.balance:
            return Exception("Error. Insufficient credits: {}".format(self.balance))
        else:
            self.balance -= amount
            print("Withdraw: {}. Current balance: {}".format(amount, self.balance))

    def get_balance(self):
        return self.balance

    def __str__(self):
        return "User: {}".format(self.username)
