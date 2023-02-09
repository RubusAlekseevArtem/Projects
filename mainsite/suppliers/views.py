import io
import json
import pprint
from datetime import datetime

from django.core import serializers
from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from .models import get_suppliers, SupplierParameter

import sys
import os.path

from .classes.parameter_provider import SupplierProvider

# print(sys.path)
sys.path.append(os.path.abspath(rf'..'))

QUERY_NAME = 'query_name'


def is_ajax(request):
    """
    request.is_ajax() is deprecated since django 3.1
    """
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


def is_ajax_query(request, query_name):
    return request.GET.get(QUERY_NAME) == query_name and is_ajax(request)


def index_responses(request):
    if request.method == 'GET':
        print(f'{request.GET=}')
        if is_ajax_query(request, 'test'):
            print(f'request.GET={request.GET}')
            print(f'button_text={request.GET.get(QUERY_NAME)}')
            t = datetime.now()
            return JsonResponse({'seconds': t}, status=200)
        if is_ajax_query(request, 'getSuppliersParameters') and \
                request.GET.get('supplier_id'):  # if have supplier_id

            supplier_id = int(request.GET.get('supplier_id'))
            print(f'{supplier_id=}')

            # долго! можно создать галочку ил кнопку с обновлением
            # supplier_provider = SupplierProvider()
            # supplier_provider.try_update_parameters_by_id(supplier_id)

            supplier_parameters_query_set = SupplierParameter.objects.all().filter(supplier__pk=supplier_id)
            suppliers_parameters = serializers.serialize('json',
                                                         supplier_parameters_query_set)  # serialize query set to json
            data = {
                'suppliers_parameters': suppliers_parameters,
            }
            return JsonResponse(data, status=200)
        if is_ajax_query(request, 'getMaterialsFile') and \
                request.GET.get('supplier_id'):  # if have supplier_id

            supplier_id = int(request.GET.get('supplier_id'))
            print(f'{supplier_id=}')

            material_codes = request.GET.getlist('material_codes[]')
            print(material_codes)
            suppliers_parameters = request.GET.getlist('suppliers_parameters[]')
            print(suppliers_parameters)

            params = {
                'suppliers_parameters': suppliers_parameters,
                'material_codes': material_codes
            }

            supplier_provider = SupplierProvider()
            data = supplier_provider.try_get_data_from_script_with_parameters(supplier_id, params)

            if data:
                # pprint.pprint(data, indent=2)
                json_data = json.dumps(data, indent=4)
                print(json_data)
                json_bytes_data = json_data.encode('utf-8')  # to bytes
                buf = io.BytesIO()
                buf.write(json_bytes_data)
                # if you pass a file-like object like io.BytesIO, it’s your task to seek()
                # it before passing it to FileResponse.
                buf.seek(0)
                return FileResponse(buf, status=200, as_attachment=True)
            return JsonResponse({}, status=500)


def index(request):
    response = index_responses(request)
    if response is not None:
        return response
    context = {
        'title': 'Данные поставщиков',
        'suppliers': get_suppliers(),
        'supplier_parameters': [],
        'is_multiple': True,
        'max_items_in_dropdown_menu': 3,
        'select_all': False,
    }
    return render(request, 'suppliers/index.html', context)
