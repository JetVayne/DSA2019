# coding=utf-8
class Node:
    def __init__(self, initVal, newNode=None):
        self.data = initVal
        self.curr_min = initVal
        self.nextNode = newNode


class MinStack:
    def __init__(self):
        self.topNode = None  # 初始值的第一個值不存在

    def push(self, newVal: int) -> None:
        if self.topNode is None:
            self.topNode = Node(newVal, None)
        else:
            # save old min
            temp = self.topNode.curr_min
            # init new node and re-assigned new min
            self.topNode = Node(newVal, self.topNode)
            if temp < self.topNode.data:
                self.topNode.curr_min = temp

    def pop(self) -> None:
        if self.topNode is None:
            return

        self.topNode = self.topNode.nextNode

    def top(self) -> int:
        if self.topNode is None:
            return None

        return self.topNode.data

    def getMin(self) -> int:
        if self.topNode is None:
            return None
        return self.topNode.curr_min
