from django.urls import path
from .views import dashboard, create_transaction

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new/', create_transaction, name='new_transaction'),
]