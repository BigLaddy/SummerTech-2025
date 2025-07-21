class Node():
    def __init__(self,left,right,parent,sizeleft,sizeright):
        self.left = left
        self.right = right
        self.parent = parent
        self.sizeleft = sizeleft
        self.sizeright = sizeright
    

class Heap():
    def __init__(self):
        self.root = None
    