import WeightedGraph
import MinHeap

class BreadthFirst():
    def __init__(self,Graph,Start,End):
        self.graph = Graph
        self.start = Start
        self.end = End
        self.todo = []
        
    def AddList(self):
        self.todo.append(self.start)
        y=0
        while y < len(self.todo): 
            for x in range(0,len(self.todo[y].edges)):
                if self.todo[y].edges[x].color == "white":
                    self.todo[y].edges[x].color = "gray"
                    if self.todo[y].edges[x].predecesor is  None:
                        self.todo[y].edges[x].predecesor= self.todo[y]
                    self.todo.append(self.todo[y].edges[x])
                if self.todo[y].edges[x]== self.end:
                    return
            y+=1
    def FindPath(self):
        Con = True
        self.Path = []
        self.Path.append(self.end)
        self.end.color = "fancy" 
        self.start.color = "fancy"
        while Con:
            if self.Path[len(self.Path)-1].predecesor is None:
                print("No valid path")
                return
            
            
            self.Path[len(self.Path)-1].predecesor.color = "black"
            self.start.color = "fancy"
            self.Path.append(self.Path[len(self.Path)-1].predecesor)
            if self.Path[len(self.Path)-1] == self.start:
                Con = False
        self.Path.reverse()
        print(self.Path)
