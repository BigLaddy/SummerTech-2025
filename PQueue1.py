class PQueueElement():
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
    def __repr__(self):
        priority = str(self.priority)
        value = str(self.value)
        return priority +" "+ value
class PQueue():
    def __init__(self):
        # O(1)
        self.PQueue = []
    def add(self,priority,value):
        # O(n)
        element = PQueueElement(priority,value)
        if self.PQueue != []:
            for x in range(-1,len(self.PQueue)-1):
                if element.priority>self.PQueue[x+1].priority:
                    self.PQueue.insert(x+1,element)
                    return
        self.PQueue.append(element)
    def remove(self):
        # O(n)
        if self.PQueue != []:
            Val = self.PQueue[0]
            self.PQueue.pop(0)
            return Val.value
        return None
    def length(self):
        # O(1)
        return len(self.PQueue)
    def get(self):
        # O(1)
        return self.PQueue[0].value
    def toList(self):
        # O(n^2)
        list = []
        for x in range(0,len(self.PQueue)):
            list.append(self.remove())
        return list
    
class ListOfLists():
    def __init__(self):
        #O(1)
        self.PQueue = [[],[]]
    def expand(self):
        #O(n)
        for x in range(0,len(self.PQueue)):
            self.PQueue.append([])
    def add(self,priority,value):
        element = PQueueElement(priority,value)
        bigEnough = False
        while bigEnough is False:
            if len(self.PQueue) < priority:
                self.expand()
            if len(self.PQueue) >= priority:
                bigEnough = True
        self.PQueue[priority].append(element)
    def remove(self):
        val = self.PQueue[len(self.PQueue)-1][0]

        

        
    

def freakyprint(val):
    print(val)
    return val
    

Queue = PQueue()
Queue.add(5,4)
Queue.add(5,3)
Queue.add(1,1)
Queue.add(3,2)
Queue.add(7,5)
print(Queue.PQueue)
print(Queue.get())
print(Queue.toList())
print(Queue.PQueue)

