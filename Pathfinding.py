class node():
    def __init__(self,edges,name):
        self.edges = edges
        self.name = name
    def __str__(self):
        print(self.name)
class graph():
    def __init__(self):
        self.nodes = []
    def Node(self,AddedNode):
        self.nodes.append(AddedNode)           
    def Edge(self,Node1,Node2):
        self.nodes[Node1].edges.append(self.nodes[Node2])
        self.nodes[Node2].edges.append(self.nodes[Node1])   
    def HasEdge(self,Node1,Node2):
        for x in range(0,len(self.nodes[Node1].edges)):
            if self.nodes[Node1].edges[x]==self.nodes[Node2]:
                return True
        return False
class pathfinder():
    def __init__(self,Graph,Start,End,Current,Traveled):
        self.Graph = Graph
        self.Start = Start
        self.End = End
        self.Current= Current
        self.Traveled = Traveled
    def FindPath(self):
        if self.Current == self.End:
            print(self.Traveled)
            return self.Traveled.append(self.Current)
        
        for x in range (0,len(self.Current.edges)):
            print("In for loop")
            Con = True
            for y in range(0,len(self.Traveled)):
                print(y)
                
                if self.Traveled[y] == self.Current.edges[x]:
                    Con = False
            if Con:
                self.Traveled.append(self.Current)
                print(len(self.Traveled))
                pathfinder(Graph,self.Start,self.End,self.Current.edges[x],self.Traveled).FindPath()
    


Graph = graph()
Graph.Node(node([],1))
Graph.Node(node([],2))
Graph.Node(node([],3))
Graph.Node(node([],4))
Graph.Node(node([],5))
Graph.Node(node([],6))
Graph.Edge(0,1)
Graph.Edge(1,2)
Graph.Edge(1,3)
Graph.Edge(3,4)
Graph.Edge(4,5)
Finder = pathfinder(Graph,Graph.nodes[0],Graph.nodes[5],Graph.nodes[0],[Graph.nodes[0]])
print(Finder.FindPath())


    
