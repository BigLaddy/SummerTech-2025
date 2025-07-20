class PQueueElement():
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
    def __str__(self):
        return str(self.value)
class PQueue():
    def __init__(self):
        self.PQueue = []
    def add(self,priority,value):
        element = PQueueElement(priority,value)
        for x in range(0,len(self.PQueue)-1):
            if element.priority>self.PQueue[x+1].value:
                self.PQueue.insert(priority,value)
                return
        self.PQueue.append(element)
    def remove(self):
        if self.PQueue != []:
            Val = self.PQueue[0]
            self.PQueue.pop(0)
            return Val.value
        return None
    def length(self):
        return len(self.PQueue)
    def get(self):
        return self.PQueue[0].value
    def toList(self):
        list = []
        for x in range(0,len(self.PQueue)):
            list.append(self.remove())
        return list
    
def freakyprint(val):
    print(val)
    return val
    

Queue = PQueue()
Queue.add(5,4)
Queue.add(5,3)
Queue.add(1,1)
Queue.add(4,2)
print(Queue.toList())

