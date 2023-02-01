from datetime import datetime

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from .models import get_suppliers, get_supplier_parameter, SupplierParameter


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
            print(request.GET.get('supplier_id'))
            supplier_parameters_query_set = SupplierParameter.objects.all().filter(pk=request.GET.get('supplier_id'))
            suppliers = serializers.serialize('json', supplier_parameters_query_set)
            print(suppliers)
            return JsonResponse({'suppliers': suppliers}, status=200)
    context = {
        'title': 'Данные поставщиков',
        'suppliers': get_suppliers(),
        'supplier_parameters': get_supplier_parameter()
    }
    return render(request, 'suppliers/index.html', context)
