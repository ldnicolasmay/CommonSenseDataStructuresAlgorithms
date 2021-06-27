from typing import Any


class MyArray(object):

    def __init__(self, *args):
        self.array = []
        for arg in args:
            self.array.append(arg)

    def __str__(self):
        return "(" + ", ".join(self.array) + ")"

    @staticmethod
    def _raise_index_error(index, max_index_type):
        base = "Index must be"
        if index < 0:
            raise IndexError(base + " greater than 0")
        elif max_index_type == "lt":
            raise IndexError(base + " less than array length")
        elif max_index_type == "lte":
            raise IndexError(base + " less than or equal to length")
        else:
            raise IndexError()

    def read(self, index: int) -> Any:
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            self._raise_index_error(index=index, max_index_type="lt")

    def search(self, item: Any) -> int:
        for index, it in enumerate(self.array):
            if item == it:
                return index
        else:
            return -1

    def insert(self, item: Any, index: int) -> None:
        if 0 <= index <= len(self.array):
            self.array = self.array[:index] + [item] + self.array[index:]
        else:
            self._raise_index_error(index, max_index_type="lte")

    def delete(self, index: int):
        if 0 <= index < len(self.array):
            self.array = self.array[:index] + self.array[(index + 1):]
        else:
            self._raise_index_error(index, max_index_type="lt")

