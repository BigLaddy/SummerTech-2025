class Node():
    def __init__(self):
    #O(1)
        self.edges = []
class Graph():
    def __init__(self):
    #O(1)
        self.nodes = []
    def add(self,addednode):
    #O(1)

        self.nodes.append(addednode)
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