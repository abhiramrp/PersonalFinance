from django import forms
from django.forms import widgets, Textarea
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from .models import *

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'all_money']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'raccount', 'description','price','important','category', 'transfer_account']
        widgets = {
            'price': forms.NumberInput(attrs={'placeholder':'Negative for expenses'})
        }
        labels = {
            'raccount': _('Account'),
            'transfer_account': _('OPTIONAL - Transfer to another account: ')
        }

        