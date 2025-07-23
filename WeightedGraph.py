class Node():
    def __init__(self,name):
    #O(1)
        self.name = name
        self.edges = []
class Edge():
    def __init__(self,node,cost):
        self.node = node
        self.cost = cost


class Graph():
    def __init__(self):
    #O(1)
        self.nodes = []
    def add(self,name):
    #O(1)
        newNode = Node(name)
        self.nodes.append(newNode)
        return newNode
    def getEdge(self,node1,node2):
        for x in range(0,len(node1.edges)):
            if node1.edges[x].node == node2:
                return node1.edges[x]
        return None
    def edge(self,node1,node2,cost):
    #O(degree of node1)
        x = self.getEdge(node1,node2)
        if x is not None:
            if cost < x.cost:
                x.cost = cost
                self.getEdge(node2,node1).cost = cost
        else:
            edge1 = Edge(node1,cost)
            edge2 = Edge(node2,cost)
            node1.edges.append(edge2)
            node2.edges.append(edge1)             
    def check(self,node1,node2):
    #O(degree of node1)
        for x in range(0,len(node1.edges)):
            if node1.edges[x].node == node2:
                return True
        return False
    def getCost(self,node1,node2):
        for x in range(0,len(node1.edges)):
            if node1.edges[x].node == node2:
                return node1.edges[x].cost
        return None
    def neighbors(self,node1):
    #O(degree of node1)
        list = []
        for x in range(0,len(node1.edges)):
            list.append(node1.edges[x])
        return list
    def nodes(self):
    #O(1)
        return self.nodes

