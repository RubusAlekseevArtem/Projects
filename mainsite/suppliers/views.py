from datetime import datetime

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from .models import get_suppliers, SupplierParameter


def is_ajax(request):
    """
    request.is_ajax() is deprecated since django 3.1
    """
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


def index(request):
    if request.method == 'GET':
        data = request.GET.get('query_name')
        if data == 'test' and is_ajax(request):
            print(f'request.GE`T={request.GET}')
            print(f'button_text={data}')
            t = datetime.now()
            return JsonResponse({'seconds': t}, status=200)
        if data == 'getSuppliersParameters' and is_ajax(request) and request.GET.get('supplier_id'):
            supplier_id = int(request.GET.get('supplier_id'))
            supplier_parameters_query_set = SupplierParameter.objects.all().filter(supplier__pk=supplier_id)
            suppliers = serializers.serialize('json', supplier_parameters_query_set)  # serialize query set to json
            print(suppliers)
            return JsonResponse({'suppliers': suppliers}, status=200)
    context = {
        'title': 'Данные поставщиков',
        'suppliers': get_suppliers(),
        'supplier_parameters': [],
        'is_multiple': True,
        'max_items_in_dropdown_menu': 5,
    }
    return render(request, 'suppliers/index.html', context)
