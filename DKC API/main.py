import json
from pprint import PrettyPrinter

from dkc_obj import DkcObj
from private_file import HEADERS, INDENT

if __name__ == '__main__':
    dkc = DkcObj()
    if dkc.access_token:
        HEADERS['AccessToken'] = dkc.access_token

        material_codes = ['4400003']
        materials = dkc.get_materials(material_codes)
        if materials:
            pretty_print = PrettyPrinter(indent=INDENT)
            print(pretty_print.pprint(materials))
        json_data = json.dumps(
            [material.__dict__ for material in materials],
            indent=INDENT
        )
        with open('load_data.txt', mode='w', encoding=dkc.base_encoding) as f:
            f.writelines(json_data)
    else:
        print('Ошибка получения токена для доступа')
