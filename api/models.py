from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Account(models.Model):
    class AccountType(models.TextChoices):
        SAVINGS = 'SAVINGS', 'Savings'
        CURRENT = 'CURRENT', 'Current'
        FIXED = 'FIXED', 'Fixed'

    account_type = models.CharField(max_length=50, choices=AccountType.choices)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="accounts")

    def __str__(self):
        return f"{self.account_type} - {self.id}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    ]
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="transactions")

    def __str__(self):
        return f"Transaction {self.id} - {self.transaction_type} on {self.transaction_date}"

class BankCustomer(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bank} - {self.customer}"

    class Meta:
        unique_together = ('bank', 'customer')
        verbose_name = "Bank Customer"
        verbose_name_plural = "Bank Customers"
