from node import Node
from typing import Callable


class FuncNode(Node):
    def __init__(self, number: str, name: str, fun: Callable[[], dict], children=None):
        super().__init__(number, name, children)
        self.fun = fun

    def __str__(self):
        return f'{super().__str__()} f={self.fun.__name__}'

    def __repr__(self):
        return f'FuncNode({self.__str__()})'


if __name__ == '__main__':
    def f_get_data():
        data = {}
        return data


    def f_get_data_2():
        data = {}
        return data


    def f_get_data_3():
        data = {}
        return data


    func_node = FuncNode(
        'id', 'test_func_name',
        f_get_data,
        [
            FuncNode(
                'id_2', 'test_func_name_2',
                f_get_data_2
            ),
            FuncNode(
                'id_3', 'test_func_name_3',
                f_get_data_3
            ),
        ]
    )
    print(func_node)
