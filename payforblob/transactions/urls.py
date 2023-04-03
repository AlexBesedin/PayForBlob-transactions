from django.urls import path
from . import views

urlpatterns = [
    path('submit_transaction/', views.submit_transaction, name='submit_transaction'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('about/', views.about, name='about'),
    path('how_to_use/', views.how_to_use, name='how_to_use')
]

