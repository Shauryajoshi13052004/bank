from rest_framework import generics
from .models import Bank, Customer, Account, Transaction, BankCustomer
from .serializers import (
    BankSerializer,
    CustomerSerializer,
    AccountSerializer,
    TransactionSerializer,
    BankCustomerSerializer,
)


class BankListCreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class BankCustomerListCreateView(generics.ListCreateAPIView):
    queryset = BankCustomer.objects.all()
    serializer_class = BankCustomerSerializer
