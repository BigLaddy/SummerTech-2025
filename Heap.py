def getLeftChild(index):
    return 2*index+1
def getRightChild(index):
    return 2*index+2
def getParent(index):
    if index == 0:
        return None
    if index%2 == 1:
        return int((index-2)/2)
    else:
        return int((index-1)/2)
class Node():
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
    def __repr__(self):
        return str(self.priority)


class badHeap():
    def __init__(self):
        self.root = None
        
    def add(self,priority,value):
        Node = Node(None,None,None,None,None,priority,value)
        self.current = self.root
        if Node.priority>self.current.priority:
            if self.current.sizeleft>self.current.sizeright:
                Node.right = self.current
                self.current.parent = Node
class Heap():
    def __init__(self):
        self.Heap = []
    def add(self,priority,value):
        newNode = Node(priority,value)
        self.size = len(self.Heap)
        self.Heap.append(newNode)
        limit = False
        if self.size == 0:
            return
        index = self.size
        while limit == False:
            x = getParent(index)
            if x is None:
                limit = True
                continue
            if self.Heap[x].priority < priority:
                temp = self.Heap[x]
                self.Heap[x] = newNode
                self.Heap[index]= temp
                index = x
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
            if getRightChild(x) >len(self.Heap)-1 and getLeftChild(x) >len(self.Heap)-1:
                limit = True
                continue
            if getLeftChild(x) >len(self.Heap)-1:
                limit = True
                continue
            if self.Heap[getLeftChild(x)].priority > self.Heap[x].priority:
                if getRightChild(x) <= len(self.Heap)-1 and self.Heap[getRightChild(x)].priority > self.Heap[getLeftChild(x)].priority:
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
            if self.Heap[getRightChild(x)].priority > self.Heap[x].priority:
                temp = self.Heap[getRightChild(x)]
                self.Heap[getRightChild(x)] = self.Heap[x]
                self.Heap[x]= temp
                x = getRightChild(x)
                continue
            limit = True
        return value
heap = Heap()
for x in range(0,10):
    heap.add(x,x)
for x in range(0,10):
    print(heap.remove())






                                                               
