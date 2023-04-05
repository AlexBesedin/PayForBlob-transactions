from django.urls import path
from . import views

urlpatterns = [
    path('submit_pfb/', views.submit_transaction, name='submit_pfb'),
    path('explorer/', views.transaction_list, name='explorer'),
    path('how_to_use/', views.how_to_use, name='how_to_use')
]

