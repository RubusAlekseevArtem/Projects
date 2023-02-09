import dataclasses
import json
import pprint

from .dkc_obj import DkcObj, DkcAccessTokenError
from .private_file import HEADERS, INDENT

PRINT_TO_CONSOLE = False


def print(materials):
    if materials and PRINT_TO_CONSOLE:
        pprint.pprint(materials, indent=2)


def save_to_file(dkc, materials, filename):
    json_data = json.dumps(
        [dataclasses.asdict(material) for material in materials],
        indent=INDENT,
        ensure_ascii=False
    )
    with open(filename, mode='w', encoding=dkc.base_encoding) as f:
        f.writelines(json_data)


def get_materials(material_codes, params=None, dkc=None):
    if dkc is None:
        try:
            dkc = DkcObj()
            return dkc.get_materials(material_codes, params)
        except DkcAccessTokenError as err:
            print(err)
    else:
        return dkc.get_materials(material_codes, params)


def main():
    dkc = DkcObj()
    if dkc.access_token:
        HEADERS['AccessToken'] = dkc.access_token

        material_codes = ['4400003']
        materials = get_materials(material_codes, None, dkc)
        if materials and PRINT_TO_CONSOLE:
            pprint.pprint(materials)
        save_to_file(dkc, materials, 'load_data.txt')
    else:
        print('Ошибка получения токена для доступа')


if __name__ == '__main__':
    main()
