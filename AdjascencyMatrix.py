def expand(list):
    #O(n)
    for x in range(0,len(list)):
        list.append(None)
    return list
class Node():
    def __init__(self,name):
    #O(1)
        self.name = name
        self.edges = [None]
class Graph():
    def __init__(self):
    #O(1)
        self.nodes = []
        self.current = 1

    def add(self):
    #O(1)
        newNode = Node(self.current)
        self.nodes.append(newNode)
        self.current +=1
        return newNode
    def edge(self,node1,node2):
    #O(n) but adding an edge to every other node also takes O(n)
        if not self.check(node1,node2):
            long = False
            while not long:
                if len(node1.edges) <= node2.name:
                    node1.edges = expand(node1.edges)
                    continue
                long = True
            node1.edges[node2.name]=node2
            long = False
            while not long:
                if len(node2.edges) <= node1.name:
                    node2.edges = expand(node2.edges)
                    continue
                long = True
            node2.edges[node1.name]=node1
            
    def check(self,node1,node2):
    #O(1)
        if len(node1.edges) < node2.name:
            return False
        if node1.edges[node2.name] == node2:
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
x = graph.add()
y = graph.add()
z = graph.add()
graph.edge(x,y)
print(graph.check(x,y))
print(graph.check(x,z))