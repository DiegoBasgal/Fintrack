from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .models import Transaction
from .selectors import get_user_transactions
from .services import calculate_summary, generate_insights
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import TransactionSerializer


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transactions_api(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Usuário não autenticado'}, status=401)
    
    transactions = get_user_transactions(request.user)

    serializer = TransactionSerializer(transactions, many=True)

    return Response(serializer.data)