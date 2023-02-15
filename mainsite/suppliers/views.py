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
                # supplier_provider.try_update_parameters_by_id(supplier_id) # долго!
                tree_view_supplier_parameters = supplier_provider.get_tree_view_supplier_parameters(supplier_id)

                if tree_view_supplier_parameters:
                    json_tree_view_supplier_parameters = json.dumps(tree_view_supplier_parameters)
                    return create_json_response(
                        {'json_tree_view_supplier_parameters': json_tree_view_supplier_parameters})
                else:
                    return create_error_json_response('Нет доступных параметров')
            return create_error_json_response(NO_SUPPLIER_ID_MESSAGE)
        if is_query(request, query_name, 'get_materials_as_file'):
            if request.GET.get('supplier_id'):  # if have supplier_id
                t1 = datetime.now()
                supplier_id = int(request.GET.get('supplier_id'))
                material_codes = request.GET.getlist('material_codes[]')
                selected_tree_ids = request.GET.getlist('selected_tree_ids[]')

                if selected_tree_ids:
                    map(int, selected_tree_ids)  # convert to int

                params = {
                    'material_codes': material_codes
                }
                supplier_provider = SupplierProvider()
                material_records = supplier_provider.get_data_with_parameters(supplier_id, params)

                if material_records:
                    # filter by tree fields ids fields
                    # result_data = []
                    # link_on_material_record = TreeViewLinkOnMaterialRecord(material_records)  # links on treeview
                    # for index_, material_record in enumerate(material_records):
                    #     # print(f'{index_=}')
                    #     parameter_link = link_on_material_record.get_parameter_by_tree_id(index_)
                    #     if parameter_link:
                    #         # print(parameter_link)
                    #         # res_object = create_result_object(parameter_link, selected_tree_ids)
                    #         # result_data.append(res_object)
                    #
                    #         result_data.append(parameter_link)

                    json_data = json.dumps(material_records, indent=4, ensure_ascii=False)
                    json_bytes_data = json_data.encode('utf-8')  # to bytes
                    buf = io.BytesIO()
                    buf.write(json_bytes_data)
                    # if you pass a file-like object like io.BytesIO, it’s your task to seek()
                    # it before passing it to FileResponse.
                    buf.seek(0)
                    t2 = datetime.now()
                    print(t2 - t1)
                    return FileResponse(buf, status=200, as_attachment=True)
                else:
                    return create_error_json_response('Из списка материалов не удалось получить данные из API')
            return create_error_json_response(NO_SUPPLIER_ID_MESSAGE)
        return create_error_json_response(WAS_NOT_QUERY_NAME_MESSAGE)


def index(request):
    context = {
        'title': 'Данные поставщиков',
        'suppliers': get_suppliers()
    }
    return render(request, 'suppliers/index.html', context)
