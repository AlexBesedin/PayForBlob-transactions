from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('namespace_id', 'data', 'gas_limit', 'fee')
        widgets = {
            'gas_limit': forms.TextInput(attrs={'value': '80000'}),
            'fee': forms.TextInput(attrs={'value': '2000'}),
        }