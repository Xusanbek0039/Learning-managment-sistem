from django.db import models
from django.conf import settings
import json


class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.FloatField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    payment_complete = models.BooleanField(default=False)
    invoice_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.user}"


class TestClass(models.Model):
    array = models.TextField(default='[]', blank=True, null=True)

    def get_array(self):
        try:
            return json.loads(self.array)
        except Exception:
            return []

    def set_array(self, arr):
        self.array = json.dumps(arr)

    def __str__(self):
        return f"TestClass #{self.id}"
