import dataclasses
import json
from pprint import PrettyPrinter

from dkc_obj import DkcObj
from private_file import HEADERS, INDENT

PRINT_TO_CONSOLE = False

if __name__ == '__main__':
    dkc = DkcObj()
    if dkc.access_token:
        HEADERS['AccessToken'] = dkc.access_token

        material_codes = ['4400003']
        materials = dkc.get_materials(material_codes)
        if materials and PRINT_TO_CONSOLE:
            pretty_print = PrettyPrinter(indent=2)
            print(pretty_print.pprint(materials))
        json_data = json.dumps(
            [dataclasses.asdict(material) for material in materials],
            indent=INDENT,
            ensure_ascii=False
        )
        with open('load_data.txt', mode='w', encoding=dkc.base_encoding) as f:
            f.writelines(json_data)
    else:
        print('Ошибка получения токена для доступа')
