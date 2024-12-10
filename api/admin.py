from django.contrib import admin
from .models import Bank, Customer, Account, Transaction, BankCustomer

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank_name', 'location')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'contact_info')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_type', 'balance', 'customer', 'bank')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_date', 'transaction_type', 'amount', 'account', 'bank')

@admin.register(BankCustomer)
class BankCustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'customer')
