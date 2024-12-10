from django.urls import path
from .views import (
    BankListCreateView,
    CustomerListCreateView,
    AccountListCreateView,
    TransactionListCreateView,
    BankCustomerListCreateView,
)

urlpatterns = [
    path('banks/', BankListCreateView.as_view(), name='bank-list-create'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('bank-customers/', BankCustomerListCreateView.as_view(), name='bankcustomer-list-create'),
]
