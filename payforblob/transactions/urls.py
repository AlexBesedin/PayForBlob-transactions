from django.urls import path
from . import views

urlpatterns = [
    path('submit_transaction/', views.submit_transaction, name='submit_transaction'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('about/', views.about, name='about'),
]

