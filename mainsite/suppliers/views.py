from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

from .models import get_suppliers, get_supplier_parameter


def index(request):
    if request.method == 'GET':
        text = request.GET.get('button_text')
        print(f'request.GET={request.GET}')
        print(f'button_text={text}')
        # request.is_ajax() is deprecated since django 3.1
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            t = datetime.now()
            return JsonResponse({'seconds': t}, status=200)
    context = {
        'title': 'Данные поставщиков',
        'suppliers': get_suppliers(),
        'supplier_parameters': get_supplier_parameter()
    }
    return render(request, 'suppliers/index.html', context)
