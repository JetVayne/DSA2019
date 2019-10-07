# coding=utf-8
class MinStack:
    def __init__(self):
        self.stack_list = []
        self.size = 0

    def push(self, data: int) -> None:
        self.stack_list.append(data)
        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return
        else:
            self.stack_list.pop(self.size - 1)
            self.size -= 1

    def top(self) -> int:
        return self.stack_list[self.size - 1]

    def getMin(self) -> int:
        return min(self.stack_list)

