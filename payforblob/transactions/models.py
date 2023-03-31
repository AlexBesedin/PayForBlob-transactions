from django.db import models

class Transaction(models.Model):
    namespace_id = models.CharField(max_length=100)
    data = models.CharField(max_length=1000)
    gas_limit = models.IntegerField()
    fee = models.IntegerField()
    height = models.IntegerField(blank=True, null=True)
    txhash = models.CharField(max_length=100, blank=True, null=True)

