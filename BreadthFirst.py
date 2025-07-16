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
class