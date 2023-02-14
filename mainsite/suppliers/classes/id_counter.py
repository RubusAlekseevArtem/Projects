class IdCounter:
    def __init__(self):
        self._id: int = 0

    @property
    def id(self):  # getter
        # print('get id')
        self._id += 1
        return self._id

    @id.setter
    def id(self, new_id: int):  # setter
        self._id = new_id
