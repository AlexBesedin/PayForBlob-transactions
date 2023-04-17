import requests
import random
import codecs
import os
import json

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
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
            return redirect('explorer')  # Изменено перенаправление на именованный URL 'explorer'
    else:
        form = TransactionForm()
    return render(request, 'submit_transaction.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-height')
    return render(request, 'transaction_list.html', {'transactions': transactions})


def generate_hex_strings():
    nID = codecs.encode(os.urandom(8), 'hex').decode()
    lenMsg = random.randint(0, 100)
    msg = codecs.encode(os.urandom(lenMsg), 'hex').decode()
    return nID, msg

def generated(request):
    if request.method == 'POST':
        nID, msg = generate_hex_strings()
        return render(request, 'generated.html', {'nID': nID, 'msg': msg})
    else:
        return render(request, 'generated.html')
    