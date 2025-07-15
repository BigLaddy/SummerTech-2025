def CopyList(List):
    NewList = []
    for x in range (0,len(List)):
        NewList.append(List[x])
    return NewList
class node():
    def __init__(self,edges,name):
        self.edges = edges
        self.name = name
    def __repr__(self):
        return str(self.name)
class graph():
    def __init__(self):
        self.nodes = []
    def Node(self,AddedNode):
        self.nodes.append(AddedNode)           
    def Edge(self,Node1,Node2):
        self.nodes[Node1-1].edges.append(self.nodes[Node2-1])
        self.nodes[Node2-1].edges.append(self.nodes[Node1-1])   
    def HasEdge(self,Node1,Node2):
        for x in range(0,len(self.nodes[Node1].edges)):
            if self.nodes[Node1].edges[x]==self.nodes[Node2]:
                return True
        return False
class pathfinder():
    def __init__(self,Graph,Start,End,Current,Traveled,Paths):
        self.Graph = Graph
        self.Start = Start
        self.End = End
        self.Current= Current
        self.Traveled = Traveled
        self.Paths=Paths
    def FindPath(self):
        
        if len(self.Current.edges) == 1 and self.Current != self.Start and self.Current != self.End:
            self.Traveled.pop(len(self.Traveled)-1)

            return None
        if self.Current == self.End:
            print("WE HAVE FOUND THE END")
            self.Traveled.append(self.Current)
            NewList = CopyList(self.Traveled)
            self.Paths.append(NewList)
            self.Traveled.clear()
            return 
        
        
        for x in range (0,len(self.Current.edges)):
            
            Con = True
            for y in range(0,len(self.Traveled)):
                
                
                if self.Traveled[y] == self.Current.edges[x]:
                    Con = False
            if Con:
                self.Traveled.append(self.Current)
                
                FoundPath = pathfinder(Graph,self.Start,self.End,self.Current.edges[x],self.Traveled,self.Paths).FindPath()
                if FoundPath is not None:
                    return FoundPath
        return
        
                
            


    


Graph = graph()
Graph.Node(node([],1))
Graph.Node(node([],2))
Graph.Node(node([],3))
Graph.Node(node([],4))
Graph.Node(node([],5))
Graph.Node(node([],6))
Graph.Edge(1,2)
Graph.Edge(2,3)
Graph.Edge(2,4)
Graph.Edge(4,5)
Graph.Edge(5,6)
Finder = pathfinder(Graph,Graph.nodes[0],Graph.nodes[5],Graph.nodes[0],[],[])
Finder.FindPath()
print(Finder.Paths)

Graph2 = graph()
Graph2.Node(node([],1))
Graph2.Node(node([],2))
Graph2.Node(node([],3))
Graph2.Node(node([],4))
Graph2.Node(node([],5))
Graph2.Node(node([],6))
Graph2.Edge(1,2)
Graph2.Edge(2,3)
Graph2.Edge(2,4)
Graph2.Edge(4,5)
Graph2.Edge(5,6)
Graph2.Edge(3,6)
Finder2 = pathfinder(Graph2,Graph2.nodes[0],Graph2.nodes[5],Graph2.nodes[0],[],[])
Finder2.FindPath()
print(Finder2.Paths)

Graph3 = graph()
Graph3.Node(node([],1))
Graph3.Node(node([],2))
Graph3.Node(node([],3))
Graph3.Node(node([],4))
Graph3.Node(node([],5))
Graph3.Node(node([],6))
Graph3.Node(node([],7))
Graph3.Node(node([],8))

Graph3.Edge(1,2)
Graph3.Edge(2,4)
Graph3.Edge(4,8)
Graph3.Edge(2,3)
Graph3.Edge(3,5)
Graph3.Edge(5,6)
Graph3.Edge(6,7)
Graph3.Edge(7,8)


Finder3 = pathfinder(Graph3,Graph3.nodes[0],Graph3.nodes[7],Graph3.nodes[0],[],[])
Finder3.FindPath()
print(Finder3.Paths)


    
