from django.views import generic

from .models import Supplier, SupplierParameter


class SuppliersView(generic.ListView):
    template_name = 'suppliers/supplier.html'
    context_object_name = 'suppliers_list'

    def get_queryset(self):
        """
        Return all Suppliers with is_outdated=False
        """
        return Supplier.objects.filter(is_outdated=False)

    # def get_supplier_parameters(self, supplier: Supplier):
    #     """
    #     Return all SupplierParameters with is_outdated=False
    #     """
    #     return SupplierParameter.objects.filter(
    #         supplier=supplier,
    #         is_outdated=False,
    #     )

# ChoiceField MultipleChoiceField TypedMultipleChoiceField
