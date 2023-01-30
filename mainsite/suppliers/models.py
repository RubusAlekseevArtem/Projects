from django.db import models

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
        return f'{self.supplier.name} \'{self.parameter_name}\' ({str(self.is_outdated)[0]})'


def get_suppliers(is_outdated: bool = False):
    """
    Return all Suppliers with is_outdated filter
    """
    return Supplier.objects.filter(is_outdated=is_outdated)
