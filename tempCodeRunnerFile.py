for x in range(-1,len(self.PQueue)-1):
                if element.priority>self.PQueue[x+1].priority:
                    self.PQueue.insert(x+1,element)
                    return