from django.urls import path
from .views import dashboard, create_transaction, transactions_api


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new/', create_transaction, name='new_transaction'),

    # API
    path('api/transactions/', transactions_api, name='transactions_api'),
]