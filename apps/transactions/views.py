from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .models import Transaction
from .selectors import get_user_transactions
from .services import calculate_summary, generate_insights


@login_required
def dashboard(request):
    transactions = get_user_transactions(request.user)

    summary = calculate_summary(transactions)
    insights = generate_insights(transactions)

    return render(request, 'transactions/dashboard.html', {
        'transactions': transactions,
        'summary': summary,
        'insights': insights
    })


@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()

    return render(request, 'transactions/form.html', {'form': form})