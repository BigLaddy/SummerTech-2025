class Node():
    def __init__(self,name):
    #O(1)
        self.name = name
        self.edges = []
class Graph():
    def __init__(self):
    #O(1)
        self.nodes = []
    def add(self,name):
    #O(1)
        newNode = Node(name)
        self.nodes.append(newNode)
        return newNode
    def edge(self,node1,node2):
    #O(degree of node1)
        if not self.check(node1,node2):
            node1.edges.append(node2)
            node2.edges.append(node1)
    def check(node1,node2):
    #O(degree of node1)
        for x in range(0,len(node1.edges)):
            if node1.edges[x] == node2:
                return True
        return False
    def neighbors(node1):
    #O(degree of node1)
        list = []
        for x in range(0,len(node1.edges)):
            list.append(node1.edges[x])
        return list
    def nodes(self):
    #O(1)
        return self.nodes
    
graph = Graph()
x = graph.add(1)
y = graph.add(2)
graph.edge(x,y)

    
