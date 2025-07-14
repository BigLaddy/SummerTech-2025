class node():
    def __init__(self,edges):
        self.edges = edges

class graph():
    def __init__(self):
        self.nodes = []
    def Node(self,AddedNode):
        self.nodes.append(AddedNode)           
    def Edge(self,Node1,Node2):
        Node1.edges.append(Node2)
        Node2.edges.append(Node1)   
    def HasEdge(self,Node1,Node2):
        for x in range(0,len(Node1.edges)):
            if Node1.edges[x]==Node2:
                return True
        return False

Graph = graph()
Graph.Node(node([]))
Graph.Node(node([]))
Graph.Node(node([]))
Graph.Edge(Graph.nodes[0],Graph.nodes[1])
print(Graph.HasEdge(Graph.nodes[0],Graph.nodes[1]))
print(Graph.HasEdge(Graph.nodes[0],Graph.nodes[2]))

    
