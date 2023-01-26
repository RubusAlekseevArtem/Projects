from django.db import models
from django import forms

MAX_LENGTH = 200


class Supplier(models.Model):
    """
    поставщики
    """
    name = models.CharField(max_length=MAX_LENGTH)
    is_outdated = models.BooleanField(default=False)  # устаревший

    def __str__(self):
        return f'{self.name} ({str(self.is_outdated)[0]})'


class SupplierParameter(models.Model):
    """
    параметры поставщиков
    """
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    parameter_name = models.CharField(max_length=MAX_LENGTH)
    is_outdated = models.BooleanField(default=False)  # устаревший

    def __str__(self):
        return f'{self.supplier} {self.parameter_name} ({str(self.is_outdated)[0]})'


class UserForm(forms.Form):
    INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 32)]
    todays_date = forms.CharField(max_length=MAX_LENGTH, label="What is today's date?",
                                  widget=forms.Select(choices=INTEGER_CHOICES))
