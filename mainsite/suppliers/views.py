import inspect
import io
import json
import os.path
import pprint
import sys
from datetime import datetime

from django.core import serializers
from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from .classes.supplier_provider import SupplierProvider
from .models import get_suppliers, SupplierParameter

# print(sys.path)
sys.path.append(os.path.abspath(rf'..'))
from DKC_API.data_classes.material_record import MaterialRecord

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
        # print(f'{request.GET=}')
        # if is_ajax_query(request, 'getSuppliersParameters') and \
        #         request.GET.get('supplier_id'):  # if have supplier_id
        #
        #     supplier_id = int(request.GET.get('supplier_id'))
        #     # print(f'{supplier_id=}')
        #
        #     # долго! можно создать галочку ил кнопку с обновлением
        #     # supplier_provider = SupplierProvider()
        #     # supplier_provider.try_update_parameters_by_id(supplier_id)
        #
        #     supplier_parameters_query_set = SupplierParameter.objects.all().filter(supplier__pk=supplier_id)
        #     suppliers_parameters = serializers.serialize('json',
        #                                                  supplier_parameters_query_set)  # serialize query set to json
        #     data = {
        #         'suppliers_parameters': suppliers_parameters,
        #     }
        #     return JsonResponse(data, status=200)
        if is_ajax_query(request, 'getSuppliersParametersTreeView') and \
                request.GET.get('supplier_id'):  # if have supplier_id
            supplier_id = int(request.GET.get('supplier_id'))

            supplier_provider = SupplierProvider()
            # долго! можно создать галочку ил кнопку с обновлением
            # supplier_provider.try_update_parameters_by_id(supplier_id)

            tree_view = supplier_provider.get_tree_view_supplier_parameters(supplier_id)
            # pprint.pprint(f'{tree_view_supplier_parameters_query_set=}', indent=2)
            if tree_view:
                json_tree_view = json.dumps(tree_view)
                return JsonResponse({'json_tree_view': json_tree_view}, status=200)
            return JsonResponse({}, status=500)
        if is_ajax_query(request, 'getMaterialsFile') and \
                request.GET.get('supplier_id'):  # if have supplier_id

            supplier_id = int(request.GET.get('supplier_id'))
            # print(f'{supplier_id=}')

            material_codes = request.GET.getlist('material_codes[]')
            # print(material_codes)
            suppliers_parameters = request.GET.getlist('suppliers_parameters[]')
            # print(suppliers_parameters)

            params = {
                'suppliers_parameters': suppliers_parameters,
                'material_codes': material_codes
            }

            supplier_provider = SupplierProvider()
            data = supplier_provider.get_data_with_parameters(supplier_id, params)

            if data:
                # pprint.pprint(data, indent=2)
                json_data = json.dumps(data, indent=4, ensure_ascii=False)
                # print(json_data)
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
