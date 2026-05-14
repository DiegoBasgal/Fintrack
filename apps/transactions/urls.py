from django.urls import path
from .views import dashboard, create_transaction, transactions_api, ajax_login


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new/', create_transaction, name='new_transaction'),
    path("ajax-login/", ajax_login, name="ajax_login"),

    # API
    path('api/transactions/', transactions_api, name='transactions_api'),
]