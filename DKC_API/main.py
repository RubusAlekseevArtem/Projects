import json
import pprint

from DKC_API.private_file import INDENT
from DKC_API.dkc_catalog_material import get_dkc_materials

PRINT_TO_CONSOLE = False
ENCODING = 'utf-8'


def my_print(data):
    if PRINT_TO_CONSOLE:
        pprint.pprint(data, indent=2)


def save_to_file(materials, filename):
    json_data = json.dumps(
        [dict(material) for material in materials],
        indent=INDENT,
        ensure_ascii=False
    )
    with open(filename, mode='w', encoding=ENCODING) as f:
        f.writelines(json_data)


if __name__ == '__main__':
    material_codes = ['4400003']
    materials = get_dkc_materials(material_codes)
    if materials:
        my_print(materials)
        print(materials)
    save_to_file(materials, 'load_data.txt')
