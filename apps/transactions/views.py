from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .models import Transaction


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    return render(request, 'transactions/dashboard.html', {
        'transactions': transactions
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