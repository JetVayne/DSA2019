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


funList = ["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtTail", "get", "addAtIndex", "addAtHead", "addAtHead",
           "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "addAtIndex", "get", "get", "addAtIndex", "get",
           "addAtHead", "addAtIndex", "addAtIndex", "addAtHead", "addAtIndex", "addAtIndex", "addAtHead", "get",
           "deleteAtIndex", "addAtIndex", "get", "get", "deleteAtIndex", "addAtTail", "addAtHead", "addAtTail",
           "addAtHead", "addAtTail", "addAtTail", "addAtIndex", "get", "get", "addAtHead", "deleteAtIndex",
           "deleteAtIndex", "get", "deleteAtIndex", "get", "addAtIndex", "addAtTail", "addAtHead", "addAtTail",
           "addAtHead", "get", "addAtTail", "addAtTail", "addAtHead", "get", "get", "addAtHead", "addAtHead",
           "addAtIndex", "addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtTail", "addAtIndex",
           "addAtHead", "addAtTail", "deleteAtIndex", "addAtHead", "addAtHead", "addAtIndex", "addAtTail", "addAtIndex",
           "addAtTail", "addAtIndex", "get", "addAtIndex", "addAtIndex", "get", "addAtTail", "addAtTail", "addAtHead",
           "addAtHead", "addAtHead", "deleteAtIndex", "addAtHead", "addAtTail", "addAtTail", "addAtTail", "addAtTail",
           "addAtHead", "addAtHead", "addAtTail", "addAtTail", "addAtIndex", "get", "addAtTail", "addAtHead",
           "addAtTail", "addAtHead"]

inputList = [[], [56], [1], [41], [98], [3], [1, 33], [72], [52], [89], [0], [98], [7, 97], [2, 51], [1], [6], [6, 49],
             [8], [72], [7, 8], [8, 58], [10], [3, 6], [9, 61], [63], [16], [7], [16, 55], [4], [10], [6], [96], [69],
             [20], [3], [44], [4], [8, 16], [15], [21], [41], [1], [11], [21], [22], [2], [5, 7], [62], [95], [91],
             [69], [24], [51], [94], [93], [29], [10], [68], [13], [32, 42], [48], [55], [79], [5], [36], [32],
             [25, 40], [8], [68], [30], [66], [92], [27, 26], [90], [11, 19], [68], [17, 62], [15], [17, 97], [35, 89],
             [44], [90], [67], [2], [51], [30], [38], [30], [43], [76], [16], [38], [82], [81], [67], [67], [3, 16],
             [57], [94], [11], [31], [50]]

# funList = ["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtTail", "get"]
# inputList = [[], [56], [1], [41], [98], [3]]

tester = MyLinkedList()
test_time = 0
for fun, input in zip(funList, inputList):
    test_time += 1
    tempDemand = str(fun) + str(input)
    tempDemand = tempDemand.replace('[', '(').replace(']', ')')
    print(tempDemand)
    if tempDemand == 'MyLinkedList()':
        tester = eval(tempDemand)
    else:
        eval('tester.'+tempDemand)
    print()
