class ListIndexException(Exception):
    def __init__(self, position):
        super().__init__(f'An {position} ist keine Note gespeichert')


class ListRangeException(Exception):
    def __init__(self, size):
        super().__init__(f'Es können maximal {size} Noten gespeichert werden')


class ValueRangeException(Exception):
    def __init__(self, value):
        super().__init__(f'Die Note {value} liegt nicht im Bereich 1 ... 6')
