from typing import Any


class MySet(object):

    def __init__(self, *args):
        self.set = []
        for arg in args:
            self.set.append(arg)

    def __str__(self):
        return "{" + ", ".join(self.set) + "}"

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
        if 0 <= index < len(self.set):
            return self.set[index]
        else:
            self._raise_index_error(index=index, max_index_type="lt")

    def search(self, item: Any) -> int:
        for index, itm in enumerate(self.set):
            if item == itm:
                return index
        else:
            return -1

    def insert(self, item: Any) -> None:
        if self.search(item) == -1:
            self.set = self.set + [item]

    def delete(self, item: Any):
        item_index = self.search(item)
        if item_index > -1:
            self.set = self.set[:item_index] + self.set[(item_index+1):]

