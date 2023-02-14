import io
import json
import os.path
import pprint
import sys
from dataclasses import is_dataclass, asdict
from json import JSONEncoder

from django.http import JsonResponse, FileResponse
from django.shortcuts import render

from .classes.supplier_provider import SupplierProvider
from .classes.tree_view_link_on_material_record import TreeViewLinkOnMaterialRecord
from .models import get_suppliers

# print(sys.path)
sys.path.append(os.path.abspath(rf'..'))
from DKC_API.data_classes.material_record import MaterialRecordEncoder, MaterialRecord

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
        if is_ajax_query(request, 'getSuppliersParametersTreeView') and \
                request.GET.get('supplier_id'):  # if have supplier_id
            supplier_id = int(request.GET.get('supplier_id'))

            supplier_provider = SupplierProvider()
            # долго!
            # supplier_provider.try_update_parameters_by_id(supplier_id)

            tree_view_supplier_parameters = supplier_provider.get_tree_view_supplier_parameters(supplier_id)
            # pprint.pprint(f'{tree_view_supplier_parameters_query_set=}', indent=2)
            if tree_view_supplier_parameters:
                json_tree_view_supplier_parameters = json.dumps(tree_view_supplier_parameters)
                return JsonResponse({'json_tree_view_supplier_parameters': json_tree_view_supplier_parameters},
                                    status=200)
            return JsonResponse({}, status=500)
        if is_ajax_query(request, 'getMaterialsFile') and \
                request.GET.get('supplier_id'):  # if have supplier_id

            supplier_id = int(request.GET.get('supplier_id'))
            # print(f'{supplier_id=}')

            material_codes = request.GET.getlist('material_codes[]')
            # print(material_codes)
            selected_tree_ids = request.GET.getlist('selected_tree_ids[]')
            # print(selected_tree_ids)

            if selected_tree_ids:
                map(int, selected_tree_ids)  # convert to int

            params = {
                'material_codes': material_codes
            }
            supplier_provider = SupplierProvider()
            material_records = supplier_provider.get_data_with_parameters(supplier_id, params)
            print(len(material_records))

            if material_records:
                # filter by tree fields ids fields
                result_data = []
                link_on_material_record = TreeViewLinkOnMaterialRecord(material_records)  # links on treeview
                for index_, material_record in enumerate(material_records):
                    # print(f'{index_=}')
                    parameter_link = link_on_material_record.get_parameter_by_tree_id(index_)
                    if parameter_link:
                        # print(parameter_link)
                        # res_object = create_result_object(parameter_link, selected_tree_ids)
                        # result_data.append(res_object)

                        result_data.append(parameter_link)

                json_data = json.dumps(result_data, cls=MaterialRecordEncoder, indent=4, ensure_ascii=False)
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
