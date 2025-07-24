import random
def getLeftChild(index):
    return 2*index+1
def getRightChild(index):
    return 2*index+2
def getParent(index):
    if index == 0:
        return None
    if index%2 == 1:
        return int((index-1)/2)
    else:
        return int((index-2)/2)
class Piece():
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
    def __repr__(self):
        return "Piece "+"("+repr(self.priority)+","+repr(self.value)+")"
Piece(5, "hello")

class Heap():
    def __init__(self):
        self.Heap = []
    def add(self,priority,value):
        newNode = Piece(priority,value)
        self.Heap.append(newNode)
        limit = False
        index = len(self.Heap)-1
        while limit == False:
            parent = getParent(index)
            if parent is None:
                limit = True
                continue
            if self.Heap[parent].priority > self.Heap[index].priority:
                above = self.Heap[parent]
                self.Heap[parent] = self.Heap[index]
                self.Heap[index]= above
                index = parent
                continue
            limit = True 
    def remove(self):
        y = self.Heap[0]
        self.Heap[0] = self.Heap[len(self.Heap)-1]
        self.Heap[len(self.Heap)-1] = y
        value = self.Heap.pop(len(self.Heap)-1)
        limit = False
        x = 0
        while limit != True:
            if getLeftChild(x) >len(self.Heap)-1:
                limit = True
                continue
            if self.Heap[getLeftChild(x)].priority < self.Heap[x].priority:
                if getRightChild(x) <= len(self.Heap)-1 and self.Heap[getRightChild(x)].priority < self.Heap[getLeftChild(x)].priority:
                    temp = self.Heap[getRightChild(x)]
                    self.Heap[getRightChild(x)] = self.Heap[x]
                    self.Heap[x]= temp
                    x = getRightChild(x)
                    continue
                temp = self.Heap[getLeftChild(x)]
                self.Heap[getLeftChild(x)] = self.Heap[x]
                self.Heap[x]= temp
                x = getLeftChild(x)
                continue
            if getRightChild(x) >len(self.Heap)-1:
                limit = True
                continue
            if self.Heap[getRightChild(x)].priority < self.Heap[x].priority:
                temp = self.Heap[getRightChild(x)]
                self.Heap[getRightChild(x)] = self.Heap[x]
                self.Heap[x]= temp
                x = getRightChild(x)
                continue
            limit = True
        return value
list = []
heap = Heap()
