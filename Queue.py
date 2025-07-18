class Queue():
    def __init__(self):
        self.queue = []
        self.pointer = 0
        self.end = 0
        self.length = 0
    def add(self,appended):
        self.queue.append(appended)
        self.end += 1
    def pop(self):
        self.pointer+=1
        if self.end == self.pointer:
            return None
        return self.queue[self.pointer-1]
    def get(self):
        return self.queue[self.pointer]
    def getLength(self):
        return len(self.queue)-self.pointer
    
queue = Queue()
queue.add(5)
queue.add(6)
print(queue.get())
print(queue.pop())
print(queue.length())