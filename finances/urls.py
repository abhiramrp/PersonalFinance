from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    
    path('add_transaction', views.add_transaction, name="add_transaction"),
    path('all_transactions', views.all_transactions, name="all_transactions"),

    path('add_account', views.add_account, name="add_account"),
    path('account/<int:account_num>', views.account_trans, name="account_trans"), 
    path('del_account/<int:account_num>', views.delete_account, name="delete_account"), 
    
    path('<str:cat>', views.category_trans, name="category_trans"),

    # API Routes

    path("del_trans/<int:trans_num>", views.delete_transaction, name="delete_transaction")

]