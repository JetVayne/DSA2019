# coding=utf-8
class Node(object):
    def __init__(self, initVal = None, prevNode = None, nextNode = None):
        self.data = initVal
        self.prevNode = None
        self.nextNode = None

class MyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.headNode = None
        self.tailNode = None

    def addAtHead(self, newHeadVal: int):
        newNode = Node(newHeadVal)
        if self.headNode == None:
            self.headNode = newNode
            self.tailNode = newNode
        else:
            newNode.nextNode = self.headNode
            self.headNode.prevNode = newNode
            self.headNode = newNode

        self.size += 1

    def addAtTail(self, newTailVal: int):
        newNode = Node(newTailVal)
        if self.headNode == None:
            self.headNode = newNode
            self.tailNode = newNode
        else:
            newNode.prevNode = self.tailNode
            self.tailNode.nextNode = newNode
            self.tailNode = newNode
        self.size += 1

    def addAtIndex(self, index: int, newVal: int):
        if index <= 0:
            self.addAtHead(newVal)
        elif index == self.size:
            self.addAtTail(newVal)
        elif index < self.size:
            newNode = Node(newVal)
            target = self.getNode(index)
            newNode.nextNode = target
            newNode.prevNode = target.prevNode  # *
            target.prevNode = newNode
            # newNode.prevNode.nextNode還是指到targetNode要改成指到newNode
            newNode.prevNode.nextNode = newNode  # **
            self.size += 1

    def deleteAtIndex(self, index: int):
        if index >= self.size or index < 0:
            return
        elif index == 0:
            self.headNode = self.headNode.nextNode
            if self.headNode != None:
                self.headNode.prevNode = None
        elif index == self.size - 1:
            self.tailNode = self.tailNode.prevNode
            if self.tailNode != None:
                self.tailNode.nextNode = None
        elif index < self.size - 1:
            target = self.getNode(index)
            target.prevNode.nextNode = target.nextNode
            target.nextNode.prevnode = target.prevNode

        self.size -= 1

    def getNode(self, index: int) -> Node:
        if index >= self.size or index < 0:
            return None
        # 到尾巴的index差
        tailDistance = self.size - 1 - index
        count = 0
        temp = Node()
        # 決定要從head開始找，還是從tail
        if index <= tailDistance:
            temp = self.headNode
            while count < index:
                temp = temp.nextNode
                count += 1
        else:
            temp = self.tailNode
            while count < tailDistance:
                temp = temp.prevNode
                count += 1

        return temp

    def get(self, index: int) -> int:
        target = self.getNode(index)
        return target.data if target != None else -1


