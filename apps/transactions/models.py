from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    TYPE_CHOICES = [
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    ]

    name = models.CharField(max_length=100, unique=True)

    category_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 👈 indústria

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.type})"