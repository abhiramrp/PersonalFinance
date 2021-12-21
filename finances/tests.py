from django.test import TestCase

from .models import *

# Create your tests here.


class AccountTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create_user(username='a', email='a@mail.com', password='a')
        u1.all_money = 10
        u1.save()

        a1 = Account.objects.create(name='c', all_money=1, ruser=User.objects.get(username='a'))

    def test_counting(self):
        u2 = User.objects.get(username='a')
        a2 = Account.objects.get(ruser=u2)
        self.assertEqual(u2.all_money, 11)

    def test_counting_delete(self):
        u2 = User.objects.get(username='a')
        a2 = Account.objects.create(name='d', all_money=10, ruser=u2)
        a2.delete()
        self.assertEqual(u2.all_money, 11)

class TransactionTestCase(TestCase):
    def setUp(self):
        u10 = User.objects.create_user(username='a', email='a@mail.com', password='a')
        u10.all_money = 100
        u10.save()


        a10 = Account.objects.create(name='a10', all_money=10, ruser=User.objects.get(username='a'))

        print(u10.all_money)
  
        t10 = Transaction.objects.create(name ='t10', price = 1, ruser=u10, raccount=a10)
        t20 = Transaction.objects.create(name ='t20', price = -3, ruser=u10, raccount=a10)


    def test_count_account(self):
        u2 = User.objects.get(username='a')
        a2 = Account.objects.get(ruser=u2)

        self.assertEqual(a2.all_money, 8)
    
    def test_count_user(self):
        u2 = User.objects.get(username='a')

        self.assertEqual(u2.all_money, 108)
    
    def test_delete_account(self):
        ua = User.objects.get(username='a')
        a = Account.objects.create(name='a', all_money=20, ruser=User.objects.get(username='a'))
        a.delete()
        self.assertEqual(ua.all_money, 108)

    def test_delete_user(self):
        ua = User.objects.get(username='a')
        t = Transaction.objects.get(name = 't20')
        t.delete()
        self.assertEqual(ua.all_money, 108)
    





