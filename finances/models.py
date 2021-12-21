from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.db.models.base import Model
from django.db.models.enums import Choices

# Create your models here.

class User(AbstractUser):
    all_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Account(models.Model):
    ruser = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    name = models.CharField(max_length=64)
    all_money = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)
        self.ruser.all_money += self.all_money
        self.ruser.save()

    def other_save(self, p, *args, **kwargs):
        self.ruser.all_money += p
        self.ruser.save()
        super(Account, self).save(*args, **kwargs)
    
    def delete(self):
        self.ruser.all_money -= self.all_money
        self.ruser.save()
        super(Account, self).delete()
    


class Transaction(models.Model):
    ruser = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    raccount = models.ForeignKey(Account, on_delete=models.CASCADE)

    transfer_account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="transfer")

    CASH = 'Cash'
    CREDIT = 'Credit'
    FAMILY = 'Family'
    FOOD = 'Food'
    FRIENDS = 'Friends'
    GAS = 'Gas'
    GROCERIES = 'Groceries'
    SHOPPING = 'Shopping'
    SAVINGS = 'Savings'
    SCHOOL = 'School'
    WORK = 'Work'
    OTHER = 'Other'

    CHOICES = [
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
        (FAMILY, 'Family'),
        (FOOD, 'Food'),
        (FRIENDS, 'Friends'),
        (GAS, 'Gas'), 
        (GROCERIES, 'Groceries'), 
        (SHOPPING, 'Shopping'),
        (SAVINGS, 'Savings'),
        (SCHOOL, 'School'), 
        (WORK, 'Work'), 
        (OTHER, 'Other')
    ]
    

    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=True)
    category = models.CharField(max_length=12, choices=CHOICES, default=OTHER)

    def __str__(self):
        return f"{self.name} : {self.price}"

    def save(self,*args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)
        self.raccount.all_money += self.price
        self.raccount.other_save(p=self.price)

    def delete(self):
        self.raccount.all_money -= self.price
        self.raccount.other_save(p= -(self.price))
        super(Transaction, self).delete()



# python3 manage.py makemigrations finances
# python3 manage.py migrate