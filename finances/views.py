import os
import json 

from django.contrib.auth import authenticate, login, logout
from django.core import paginator
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import EmptyPage, Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *
from .utils import *

pag_count = 20

# Create your views here.

def index(request):
    context = {}

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)

        accs = Account.objects.filter(ruser=user)

        n = get_main_expenses(user)
        p = get_main_income(user)
        w = get_waste_expense(user)

        nlabels = list(n.keys())
        ndata = list(n.values())
        plabels = list(p.keys())
        pdata = list(p.values())

        wlabels = list(w.keys())
        wdata = list(w.values())

        context['accs'] = accs

        context['nlabels'] = nlabels
        context['ndata'] = ndata
        context['plabels'] = plabels
        context['pdata'] = pdata

        context['wlabels'] = wlabels
        context['wdata'] = wdata


    return render(request, "finances/index.html", context)



@login_required
def add_account(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        form = AccountForm(request.POST)

        if form.is_valid():
            account = form.save(commit=False)
            account.ruser = user
            account.save()


            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "finances/add_account.html", {"form": form})
    else:
        return render(request, "finances/add_account.html", {"form": AccountForm()})


@login_required
def add_transaction(request):
    user = User.objects.get(username=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.ruser = user

            transaction.save()

   

            if transaction.transfer_account == transaction.raccount:

                transaction.transfer_account = None
                transaction.save()
            
            if transaction.transfer_account != None:

                temp_trans = Transaction(
                    ruser = user, 
                    raccount = transaction.transfer_account,
                    transfer_account = transaction.raccount,

                    name = transaction.name, 
                    price = -1 * transaction.price, 
                    description = transaction.description,
                    important = transaction.important,
                    category = transaction.category
                    
                )

                temp_trans.save()

            return HttpResponseRedirect(reverse("all_transactions"))
        else:
            return render(request, "finances/add_transaction.html", {"form": form})
    else:
        return render(request, "finances/add_transaction.html", {"form": TransactionForm()})


@login_required
def delete_transaction(request, trans_num):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if not is_ajax:
        return HttpResponseBadRequest('Invalid request')

    if request.method != "DELETE":
        return JsonResponse({'status': 'Invalid request'}, status=400)

    user = User.objects.get(username=request.user)

    transaction = Transaction.objects.get(ruser=user, id=trans_num)

    if transaction.transfer_account != None:

        
        try:
            prev = Transaction.objects.get(ruser=user, id=trans_num-1)
        except ObjectDoesNotExist:
            prev = None

        if(check_opposite(transaction, prev)):
            prev.delete()
        else:
            nex = Transaction.objects.get(ruser=user, id=trans_num+1)
            nex.delete()

    transaction.delete()

    return JsonResponse({'status': 'Object deleted!'})



@login_required
def all_transactions(request):
    user = User.objects.get(username=request.user)

    transactions = Transaction.objects.filter(ruser=user).order_by('-time')

    p = Paginator(transactions, pag_count)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, "finances/all_transactions.html", {'transactions': page})

@login_required
def account_trans(request, account_num):
    user = User.objects.get(username=request.user)

    account = Account.objects.get(id=account_num, ruser=user)

    account_graph_pos = get_pos(account)
    account_graph_neg = get_negs(account)

    plabels = list(account_graph_pos.keys())
    pdata = list(account_graph_pos.values())

    nlabels = list(account_graph_neg.keys())
    ndata = list(account_graph_neg.values())


    transactions = Transaction.objects.filter(raccount=account).order_by('-time')

    p = Paginator(transactions, pag_count)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, "finances/account.html", {'transactions': page, 'account': account, 'plabels': plabels, 'pdata': pdata, 'nlabels': nlabels, 'ndata': ndata})

@login_required
def delete_account(request, account_num):
    user = User.objects.get(username=request.user)

    account = Account.objects.get(id=account_num, ruser=user)

    account.delete()

    return HttpResponseRedirect(reverse("index"))

    

@login_required
def category_trans(request, cat):
    user = User.objects.get(username=request.user)
    
    transactions = Transaction.objects.filter(ruser=user, category=cat).order_by('-time')

    cat_sum = get_cat_sum(transactions)

    p = Paginator(transactions, pag_count)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, "finances/category.html", {'transactions': page, 'cat': cat, 'cat_sum': cat_sum})







def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "finances/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "finances/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "finances/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "finances/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "finances/login.html")