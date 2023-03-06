import unittest

from django.test import TestCase

from .models import Supplier, SupplierParameter


class SupplierModelTests(TestCase):
    name = 'name'
    is_outdated = False
    test_supplier: Supplier

    def setUp(self) -> None:
        self.test_supplier = Supplier.objects.create(name=self.name,
                                                     is_outdated=self.is_outdated)

    def tearDown(self) -> None:
        self.test_supplier.delete()

    def test_creation(self):
        self.assertEqual(str(self.test_supplier), f'{self.name} ({str(self.is_outdated)[0]})')


class SupplierParameterModelTests(TestCase):
    name = 'name'
    parameter_name = 'parameter_name'
    is_outdated = False
    test_supplier: Supplier
    test_supplier_parameter: SupplierParameter

    def setUp(self) -> None:
        self.test_supplier = Supplier.objects.create(name=self.name,
                                                     is_outdated=self.is_outdated)
        self.test_supplier_parameter = SupplierParameter.objects.create(supplier=self.test_supplier,
                                                                        parameter_name=self.parameter_name,
                                                                        is_outdated=self.is_outdated)

    def tearDown(self) -> None:
        self.test_supplier.delete()
        self.test_supplier_parameter.delete()

    def test_creation(self):
        self.assertEqual(str(self.test_supplier_parameter),
                         f'{self.test_supplier_parameter.supplier.name} '
                         f'\'{self.test_supplier_parameter.parameter_name}\' '
                         f'({str(self.test_supplier_parameter.is_outdated)[0]})')


if __name__ == '__main__':
    unittest.main()
