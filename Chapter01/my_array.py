from typing import Any


class MyArray(object):

    def __init__(self, *args):
        self.array = []
        for arg in args:
            self.array.append(arg)

    def __str__(self):
        return "(" + ", ".join(self.array) + ")"

    def read(self, index: int) -> Any:
        if 0 <= index < len(self.array):
            return self.array[index]
        elif index < 0:
            raise IndexError("index must be greater than 0")
        else:
            raise IndexError("index must be less than or equal to array length")

    def search(self, item: Any) -> int:
        for index, it in enumerate(self.array):
            if item == it:
                return index
        else:
            return -1

    def insert(self, item: Any, index: int):
        if 0 <= index <= len(self.array):
            self.array = self.array[:index] + [item] + self.array[index:]
        elif index < 0:
            raise IndexError("index must be greater than 0")
        else:
            raise IndexError("index must be less than or equal to array length")

    def delete(self, index: int):
        if 0 <= index < len(self.array):
            self.array = self.array[:index] + self.array[(index + 1):]
        elif index < 0:
            raise IndexError("index must be greater than 0")
        else:
            raise IndexError("index must be less than array length")

