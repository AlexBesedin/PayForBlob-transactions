from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .forms import TransactionForm
from .models import Transaction
import requests

import json


import requests
import json
from django.shortcuts import render, redirect  # Изменено импортирование redirect

from .forms import TransactionForm
from .models import Transaction

def submit_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            namespace_id = form.cleaned_data['namespace_id']
            data = form.cleaned_data['data']
            gas_limit = form.cleaned_data['gas_limit']
            fee = form.cleaned_data['fee']

            # Отправляем POST запрос
            post_data = {
                "namespace_id": namespace_id,
                "data": data,
                "gas_limit": gas_limit,
                "fee": fee
            }
            response = requests.post('http://localhost:26659/submit_pfb', data=json.dumps(post_data))
            response_dict = json.loads(response.text)

            # Сохраняем транзакцию в базе данных
            transaction = form.save(commit=False)
            transaction.height = response_dict.get('height')
            transaction.txhash = response_dict.get('txhash')
            transaction.save()

            # Перенаправляем пользователя на страницу со списком транзакций
            return redirect('transaction_list')  # Изменено перенаправление на именованный URL 'transaction_list'
    else:
        form = TransactionForm()
    return render(request, 'submit_transaction.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-height')
    return render(request, 'transaction_list.html', {'transactions': transactions})


def how_to_use(request):
    return render(request, 'how_to_use.html')

def about(request):
    return render(request, 'about.html')