from .models import Transaction
from datetime import date

def get_user_transactions(user):
    return (
        Transaction.objects
        .filter(user=user)
        .select_related('category')
        .order_by('-date')
    )


def get_user_expenses(user):
    return Transaction.objects.filter(user=user, type='expense')


def get_user_incomes(user):
    return Transaction.objects.filter(user=user, type='income')


def get_current_month_transactions(user):
    today = date.today()
    return Transaction.objects.filter(
        user=user,
        date__month=today.month,
        date__year=today.year
    )