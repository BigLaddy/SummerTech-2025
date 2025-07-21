def getLeftChild(index):
    return 2*index+1
def getRightChild(index):
    return 2*index+2
def getParent(index):
    if index == 0:
        return None
    if index%2 == 1:
        return (index-2)/2
    else:
        return (index-1)/2
class Node():
    def __init__(self,left,right,parent,sizeleft,sizeright,priority,value):
        self.priority = priority
        self.value = value


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
        index = self.size
        while limit != True:
            if self.Heap[getParent(index)].priority > priority:
                temp = self.Heap[getParent(index)]
                self.Heap[getParent(index)] = newNode
                self.Heap[index]= temp
                index = getParent(index)
                continue
            limit = True 




                                                               
