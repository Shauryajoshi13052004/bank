from rest_framework import serializers
from .models import Bank, Customer, Account, Transaction, BankCustomer


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_date', 'transaction_type', 'amount', 'account', 'bank']


class AccountSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)  # Use the related_name 'transactions'

    class Meta:
        model = Account
        fields = ['id', 'account_type', 'balance', 'customer', 'bank', 'transactions']


class BankCustomerSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    bank = serializers.StringRelatedField()

    class Meta:
        model = BankCustomer
        fields = ['id', 'bank', 'customer']


class CustomerSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True)  # Use the related_name 'accounts'

    class Meta:
        model = Customer
        fields = ['id', 'customer_name', 'contact_info', 'accounts']


class BankSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True)  # Use the related_name 'accounts'
    transactions = TransactionSerializer(many=True, read_only=True)  # Use the related_name 'transactions'

    class Meta:
        model = Bank
        fields = ['id', 'bank_name', 'location', 'accounts', 'transactions']
