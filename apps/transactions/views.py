from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .forms import TransactionForm
from .models import Transaction, Category
from .selectors import get_user_transactions
from .services import calculate_summary, generate_insights
from .serializers import TransactionSerializer


@login_required
def dashboard(request):
    transactions = get_user_transactions(request.user)
    chart_transactions = Transaction.objects.filter(user=request.user)

    summary = calculate_summary(transactions)
    insights = generate_insights(transactions)

    # gráfico 1: gastos por categoria
    category_data = (
        chart_transactions
        .filter(type='expense')
        .values('category__name')
        .annotate(total=Sum('amount'))
    )
    
    category_labels = [x['category__name'] for x in category_data]
    category_values = [float(x['total']) for x in category_data]

    # gráfico 2: evolução mensal
    monthly_data = (
        transactions
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    month_labels = [x['month'].strftime("%b/%Y") for x in monthly_data]
    month_values = [float(x['total']) for x in monthly_data]

    return render(request, 'transactions/dashboard.html', {
        'transactions': transactions,
        'summary': summary,
        'insights': insights,

        'category_labels': category_labels,
        'category_values': category_values,

        'month_labels': month_labels,
        'month_values': month_values,

        'categories': Category.objects.all()
        
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

    return render(request, 'transactions/new_transaction.html', {'form': form})

@require_POST
def ajax_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)
        return JsonResponse({
            "success": True,
            "redirect": "/"
        })

    return JsonResponse({
        "success": False,
        "message": "Usuário ou senha inválidos"
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transactions_api(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Usuário não autenticado'}, status=401)
    
    transactions = get_user_transactions(request.user)

    serializer = TransactionSerializer(transactions, many=True)

    return Response(serializer.data)