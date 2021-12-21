import operator

from .models import *


def check_opposite(cur, oth):

    if oth == None:
        return False

    if cur.price != (-1 * oth.price):
        return False

    if cur.raccount != oth.transfer_account:
        return False
    
    if cur.transfer_account != oth.raccount:
        return False
    

    return True

def get_negs(acc):
    ac = Transaction.objects.filter(raccount = acc, price__lt=0)

    d = {}

    for a in ac:
        if a.category in d:
            d[str(a.category)] += float(a.price)
        else:
            d[str(a.category)] = float(a.price)

    sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1)))
    return sorted_dict

def get_pos(acc):
    ac = Transaction.objects.filter(raccount = acc, price__gt=0)

    d = {}

    for a in ac:
        if a.category in d:
            d[str(a.category)] += float(a.price)
        else:
            d[str(a.category)] = float(a.price)

    sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_dict

def get_cat_sum(trans):

    sum = 0.00

    for t in trans:
        sum += float(t.price)

    return round(sum, 2)

def get_main_expenses(user):
    trans = Transaction.objects.filter(ruser=user, price__lt=0, transfer_account=None)

    d = {}

    for t in trans:
        if t.category in d:
            d[str(t.category)] += float(t.price)
        else:
            d[str(t.category)] = float(t.price)

    sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1)))
    return sorted_dict

def get_main_income(user):
    trans = Transaction.objects.filter(ruser=user, price__gt=0, transfer_account=None)

    d = {}

    for t in trans:
        if t.category in d:
            d[str(t.category)] += float(t.price)
        else:
            d[str(t.category)] = float(t.price)

    sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_dict

def get_waste_expense(user):
    trans = Transaction.objects.filter(ruser=user, price__lt=0, transfer_account=None, important=False)

    d = {}

    for t in trans:
        if t.category in d:
            d[str(t.category)] += float(t.price)
        else:
            d[str(t.category)] = float(t.price)

    sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1)))
    return sorted_dict
