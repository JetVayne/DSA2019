class Node():
    def __init__(self, init_val=None):
        self.data = init_val
        self.prev_node = None
        self.next_node = None


class MyLinkedList():
    def __init__(self):
        self.size = 0
        self.head_node = None
        self.tail_node = None

    def get_node(self, index: int) -> Node:
        if index >= self.size or index < 0:
            return None
        # 到尾巴的index差
        tail_distance = self.size - 1 - index
        count = 0
        result = Node()
        # 決定要從head開始找，還是從tail
        if index <= tail_distance:
            result = self.head_node
            while count < index:
                result = result.next_node
                count += 1
        else:
            result = self.tail_node
            while count < tail_distance:
                result = result.prev_node
                count += 1

        return result

    def addAtHead(self, new_head_val: int):
        new_node = Node(new_head_val)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.head_node.prev_node = new_node
            new_node.next_node = self.head_node
            self.head_node = new_node

        self.size += 1

    def addAtTail(self, new_tail_val: int):
        new_node = Node(new_tail_val)
        if self.tail_node is None:
            self.tail_node = new_node
            self.head_node = new_node
        else:
            self.tail_node.next_node = new_node
            new_node.prev_node = self.tail_node
            self.tail_node = new_node

        self.size += 1

    def addAtIndex(self, index: int, new_val: int):
        if index <= 0:
            self.addAtHead(new_val)
        elif index == self.size:
            self.addAtTail(new_val)
        elif index < self.size:
            new_node = Node(new_val)
            target = self.get_node(index)

            new_node.next_node = target
            new_node.prev_node = target.prev_node # *
            target.prev_node = new_node
            # newNode.prevNode.nextNode還是指到targetNode要改成指到newNode
            new_node.prev_node.next_node = new_node # **
            self.size += 1

    def deleteAtIndex(self, index: int):
        if index >= self.size or index < 0:
            return
        elif index == 0:
            self.head_node = self.head_node.next_node
            if self.head_node:
                self.head_node.prev_node == None
        elif index == self.size - 1:
            self.tail_node = self.tail_node.prev_node
            if self.tail_node:
                self.tail_node.next_node == None
        elif index < self.size - 1:
            target = self.get_node(index)
            target.next_node.prev_node = target.prev_node
            target.prev_node.next_node = target.next_node
            del target

        self.size -= 1

    def get(self, index: int) -> int:
        target = self.get_node(index)
        return target.data if target is not None else -1
