# coding=utf-8
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.top = None

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.top = x

        self.stack1.append(x)

    def pop(self) -> int:
        out_stack = []
        while self.stack1:
            out_stack.append(self.stack1.pop())

        result = out_stack.pop()

        if out_stack:
            self.top = out_stack[-1]  # the save last value
        else:
            self.top = None

        while out_stack:
            self.stack1.append(out_stack.pop())

        return result

    def peek(self) -> int:
        return self.top

    def empty(self) -> bool:
        return self.top is None
