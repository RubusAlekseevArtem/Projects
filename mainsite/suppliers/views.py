import io
import json
import os.path
import sys
from datetime import datetime

from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from .classes.supplier_provider import SupplierProvider
from .models import get_suppliers

sys.path.append(os.path.abspath(rf'..'))

QUERY_NAME = 'query_name'
ERROR = 'error'


def is_ajax(request):
    """
    request.is_ajax() is deprecated since django 3.1
    """
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


def is_query(request, query_name: str, server_query_name: str):
    return is_ajax(request) and \
        query_name == server_query_name


def create_error_json_response(message: str):
    return JsonResponse({ERROR: message}, status=500)


def create_json_response(data: dict):
    return JsonResponse(data, status=200)


NO_SUPPLIER_ID_MESSAGE = f'Json don\'t have supplier_id'
WAS_NOT_QUERY_NAME_MESSAGE = f'The QUERY_NAME was not found.'


def response_by_query_name(request, query_name):
    if request.method == 'GET' and query_name:
        print(f'{request.GET=}')
        if is_query(request, query_name, 'get_tree_view_of_supplier_parameters'):
            if request.GET.get('supplier_id'):  # if have supplier_id
                supplier_id = int(request.GET.get('supplier_id'))

                supplier_provider = SupplierProvider()
                supplier_tree_params = supplier_provider.get_supplier_tree_params(supplier_id)

                if supplier_tree_params:
                    json_supplier_tree_params = json.dumps(supplier_tree_params)
                    return create_json_response(
                        {'json_supplier_tree_params': json_supplier_tree_params})
                return create_error_json_response('Нет доступных параметров поставщика')
            return create_error_json_response(NO_SUPPLIER_ID_MESSAGE)
        if is_query(request, query_name, 'get_materials_as_file'):
            if request.GET.get('supplier_id'):  # if have supplier_id
                t1 = datetime.now()
                supplier_id = int(request.GET.get('supplier_id'))
                material_codes = request.GET.getlist('material_codes[]')
                selected_tree_numbers = request.GET.getlist('tree_numbers[]')

                params = {
                    'material_codes': material_codes
                }
                supplier_provider = SupplierProvider()
                supplier_data = supplier_provider.get_supplier_data(supplier_id, params)

                if supplier_data:
                    data = supplier_provider.get_filter_data_by_tree_numbers(
                        supplier_id,
                        supplier_data,
                        selected_tree_numbers
                    )

                    if data:
                        json_data = json.dumps(data, indent=4, ensure_ascii=False)
                        json_bytes_data = json_data.encode('utf-8')  # to bytes
                        buf = io.BytesIO()
                        buf.write(json_bytes_data)
                        # if you pass a file-like object like io.BytesIO, it’s your task to seek()
                        # it before passing it to FileResponse.
                        buf.seek(0)
                        t2 = datetime.now()
                        processing_time = t2 - t1
                        average_processing_time = processing_time / len(supplier_data)
                        print(f'Transmitted material codes : {len(material_codes)}')
                        print(f'Materials received from the api : {len(supplier_data)}')
                        print(f'Processing time = {processing_time}')
                        print(f'Average processing time = {average_processing_time}')
                        return FileResponse(buf, status=200, as_attachment=True)
                    return create_error_json_response('Не удалось достать выбранные данные из списка')
                return create_error_json_response('Из списка материалов не удалось получить данные из API')
            return create_error_json_response(NO_SUPPLIER_ID_MESSAGE)
        return create_error_json_response(WAS_NOT_QUERY_NAME_MESSAGE)
    return create_error_json_response(f'Не указан query_name')


def index(request):
    context = {
        'title': 'Данные поставщиков',
        'suppliers': get_suppliers()
    }
    return render(request, 'suppliers/index.html', context)
