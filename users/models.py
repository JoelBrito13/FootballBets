import binascii
import os

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from django.conf import settings


class Person(AbstractUser):
    description = models.TextField(blank=True)
    balance = models.FloatField(
        null=False,
        default=0
    )

    def insert_credits(self, amount):
        self.balance += amount
        self.save()

    def withdraw_credits(self, amount):
        if amount > self.balance:
            return Exception("Error. Insufficient credits: {}".format(self.balance))
        else:
            self.balance -= amount
            print("Withdraw: {}. Current balance: {}".format(amount, self.balance))
            self.save()

    def __str__(self):
        return "User: {}".format(self.username)


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(Person,
                                on_delete=models.CASCADE, verbose_name="User"
                                )
    created = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
