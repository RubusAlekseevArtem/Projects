import dataclasses
import json
from pprint import PrettyPrinter

from .dkc_obj import DkcObj
from .private_file import HEADERS, INDENT

PRINT_TO_CONSOLE = False


def print(materials):
    if materials and PRINT_TO_CONSOLE:
        pretty_print = PrettyPrinter(indent=2)
        print(pretty_print.pprint(materials))


def save_to_file(dkc, materials, filename):
    json_data = json.dumps(
        [dataclasses.asdict(material) for material in materials],
        indent=INDENT,
        ensure_ascii=False
    )
    with open(filename, mode='w', encoding=dkc.base_encoding) as f:
        f.writelines(json_data)


def get_materials(material_codes, dkc=None):
    if dkc is None:
        dkc = DkcObj()
        if dkc.access_token:
            HEADERS['AccessToken'] = dkc.access_token
            return dkc.get_materials(material_codes)
        else:
            print('Ошибка получения токена для доступа')
    else:
        return dkc.get_materials(material_codes)


def main():
    dkc = DkcObj()
    if dkc.access_token:
        HEADERS['AccessToken'] = dkc.access_token

        material_codes = ['4400003']
        materials = get_materials(material_codes, dkc)
        if materials and PRINT_TO_CONSOLE:
            pretty_print = PrettyPrinter(indent=2)
            print(pretty_print.pprint(materials))
        save_to_file(dkc, materials, 'load_data.txt')
    else:
        print('Ошибка получения токена для доступа')


if __name__ == '__main__':
    main()
