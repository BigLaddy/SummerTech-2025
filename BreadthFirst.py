import random
def CopyList(List):
    NewList = []
    for x in range (0,len(List)):
        NewList.append(List[x])
    return NewList
class node():
    def __init__(self,edges,name):
        self.edges = edges
        self.name = name
        self.color = "white"
        self.predecesor = None
    def __repr__(self):
        if self.color =="white":
            return "\u26AA "
        if self.color == "gray":
            return "\u26AB "
        if self.color == "black":
            return " \u26AC "
        if self.color =="fancy":
            return " \u25C9 "
    def GetColor(self):
        return self.Color
class graph():
    def __init__(self):
        self.nodes = []
        self.Length = 0
    def FromCoor(self,Coor):
        for x in range(0,len(self.nodes)):
            if [self.nodes[x].xCoor,self.nodes[x].yCoor] == Coor:
                return self.nodes[x]
    def Node(self,AddedNode):
        self.nodes.append(AddedNode)           
    def Edge(self,Node1,Node2):
        self.nodes[Node1-1].edges.append(self.nodes[Node2-1])
        self.nodes[Node2-1].edges.append(self.nodes[Node1-1])   
    def CoorEdge(self,Coor1,Coor2):
        Node1 = None
        Node2 = None
        for x in range(0,len(self.nodes)):
            if [self.nodes[x].xCoor,self.nodes[x].yCoor] == Coor1:
                Node1 = self.nodes[x]
        for y in range(0,len(self.nodes)):
            if [self.nodes[y].xCoor,self.nodes[y].yCoor] == Coor2:
                Node2 = self.nodes[y]
        if Node2 is None:
            return
        
        Node1.edges.append(Node2)
        Node2.edges.append(Node1)
        

    def HasEdge(self,Node1,Node2):
        for x in range(0,len(Node1.edges)):
            if Node1.edges[x] == Node2:
                return True
            
        return False
    def CreateNew(self,Length,Amount):
        
        Graph = graph()
        for x in range(0,Length):
            for y in range(0,Length):
                Node = node([],[x,y])
                Node.xCoor = x
                Node.yCoor = y
                Graph.Node(Node)
        for x in range(0,Length*2):  
            for z in range(0,Length):
                Graph.CoorEdge([x,z],[x,z+1])
                Graph.CoorEdge([x,z],[x+1,z])
        x=0
        while x < Amount:
        
            Node = Graph.nodes[random.randrange(0,len(Graph.nodes))]
            
            if Node.edges == []:
                continue
            Node2 = Node.edges[random.randrange(0,len(Node.edges))]
            Node.edges.remove(Node2)
            Node2.edges.remove(Node)

            x +=1
        Graph.Length = Length
        return Graph
    def Display(self):
        for x in range(0,self.Length):
            for y in range(0,self.Length):
                Node = self.FromCoor([y,x])
                print(Node,end='')
                space = True
                for p in range(0,len(Node.edges)):
                    if Node.edges[p] == self.FromCoor([y+1,x]):
                        print("-",end='')
                        space = False
                if space:
                    print(' ',end='')
            print()
            for y in range(0,self.Length):
                Node = self.FromCoor([y,x])
                Node2 = self.FromCoor([y,x+1])
                if self.HasEdge(Node,Node2):
                    print(' |  ',end="")
                else:
                    print("    ",end="")

                
            print()

                
            

            

        
        
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
Graph10 = graph()
Graph10 = Graph10.CreateNew(41,1500)
Finder10 = BreadthFirst(Graph10,Graph10.FromCoor([random.randrange(0,40),random.randrange(0,40)]),Graph10.FromCoor([random.randrange(0,40),random.randrange(0,40)]))
Finder10.AddList()
Finder10.FindPath()
Graph10.Display()
# Graph = graph()
# Graph.Node(node([],1))
# Graph.Node(node([],2))
# Graph.Node(node([],3))
# Graph.Node(node([],4))
# Graph.Node(node([],5))
# Graph.Node(node([],6))
# Graph.Edge(1,2)
# Graph.Edge(2,3)
# Graph.Edge(2,4)
# Graph.Edge(4,5)
# Graph.Edge(5,6)
# Graph.Edge(3,4)
# Finder = BreadthFirst(Graph,Graph.nodes[0],Graph.nodes[5],[],0)
# Finder.AddList()
# Finder.FindPath()

# Graph2 = graph()
# Graph2.Node(node([],1))
# Graph2.Node(node([],2))
# Graph2.Node(node([],3))
# Graph2.Node(node([],4))
# Graph2.Node(node([],5))
# Graph2.Node(node([],6))
# Graph2.Edge(1,2)
# Graph2.Edge(2,3)
# Graph2.Edge(2,4)
# Graph2.Edge(4,5)
# Graph2.Edge(5,6)
# Graph2.Edge(3,6)
# Finder2=BreadthFirst(Graph2,Graph2.nodes[0],Graph2.nodes[5],[],0)
# Finder2.AddList()
# Finder2.FindPath()


# Graph3 = graph()
# Graph3.Node(node([],1))
# Graph3.Node(node([],2))
# Graph3.Node(node([],3))
# Graph3.Node(node([],4))
# Graph3.Node(node([],5))
# Graph3.Node(node([],6))
# Graph3.Node(node([],7))
# Graph3.Node(node([],8))

# Graph3.Edge(1,2)
# Graph3.Edge(2,4)
# Graph3.Edge(4,8)
# Graph3.Edge(2,3)
# Graph3.Edge(3,5)
# Graph3.Edge(5,6)
# Graph3.Edge(6,7)
# Graph3.Edge(7,8)
# Finder=BreadthFirst(Graph3,Graph3.nodes[0],Graph3.nodes[7],[],0)
# Finder.AddList()
# Finder.FindPath()

# Graph4 = graph()
# Graph4.Node(node([],1))
# Graph4.Node(node([],2))
# Graph4.Node(node([],3))
# Graph4.Node(node([],4))
# Graph4.Node(node([],5))
# Graph4.Node(node([],6))
# Graph4.Node(node([],7))
# Graph4.Node(node([],8))
# Graph4.Node(node([],9))
# Graph4.Node(node([],10))
# Graph4.Node(node([],11))
# Graph4.Node(node([],12))

# Graph4.Edge(1,2)
# Graph4.Edge(8,11)
# Graph4.Edge(2,3)
# Graph4.Edge(1,5)
# Graph4.Edge(1,4)
# Graph4.Edge(4,5)
# Graph4.Edge(5,6)
# Graph4.Edge(7,8)
# Graph4.Edge(8,12)
# Graph4.Edge(10,9)
# Graph4.Edge(10,11)
# Graph4.Edge(11,12)
# Graph4.Edge(7,12)
# Graph4.Edge(5,8)

# Finder4=BreadthFirst(Graph4,Graph4.nodes[0],Graph4.nodes[11],[],0)
# Finder4.AddList()
# Finder4.FindPath()

# Graph5=graph()
# for x in range(0,10):
#     Graph5.Node(node([],x+1))
# for y in range(0,len(Graph5.nodes)):
#     for z in range(0,len(Graph5.nodes)):
#         Graph5.Edge(y,z)
# Finder5 = BreadthFirst(Graph5,Graph5.nodes[0],Graph5.nodes[9],[],0)
# Finder5.AddList()
# Finder5.FindPath()
# Graph6=graph()
# for x in range(0,200):
#     Graph6.Node(node([],x+1))

# def Chain(Length,Graph):
#     for x in range(0,Length,3):
#         Graph.Edge(x+1,x+2)
#         Graph.Edge(x+1,x+3)
#         Graph.Edge(x+2,x+4)
#         Graph.Edge(x+3,x+4)
# Chain(100,Graph6)
        

# Finder6 = BreadthFirst(Graph6,Graph6.nodes[0],Graph6.nodes[99],[],0)
# Finder6.AddList()
# Finder6.FindPath()




