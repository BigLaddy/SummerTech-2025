import WeightedGraph
import MinHeap

class Dijkstras():
    def __init__(self,Graph,Start,End):
        self.graph = Graph
        self.start = Start
        self.end = End
        self.todo = MinHeap.Heap()
        
    def getDistance(self):
        #O(m log m)
        self.todo.add(0,self.start)#O(1)
        done = False
        for x in range(0,len(self.graph.nodes)):#O(n)
            self.graph.nodes[x].distance = None
            self.graph.nodes[x].done = False
        self.start.distance = 0
        while not done:#O(number of edges)
            current = self.todo.remove()#O(log(number of edges))
            if current.value.done == True:
                continue
            edges = self.graph.neighbors(current.value)#O(n)
            node = edges[0].node
            for x in range(0,len(edges)):#O(n)
                if  current.value == self.end:
                        return
                node = edges[x].node
                if not node.done:
                    cost = edges[x].cost
                    dist = current.value.distance + cost
                    if node.distance is None or dist <= node.distance:
                        node.distance = current.value.distance + cost
                    self.todo.add(node.distance,node)#O(log(number of edges))

            current.value.done = True
        return None
    def getPath(self):
        #O(m)
        Con = True
        self.path = []
        self.path.append(self.end)
        current = self.end
        while Con:#O(n)
            neighbors = self.graph.neighbors(current)#O(n)
            next = neighbors[0]
            for x in range(0,len(neighbors)):#O(m )
                if neighbors[x].node.distance+neighbors[x].cost <= next.node.distance+next.cost:
                    next = neighbors[x]
            current = next.node
            self.path.append(current)
            if current == self.start:
                Con = False
                continue
        self.path.reverse()#O(n)
        return self.path

        
                

Graph = WeightedGraph.Graph()
a = Graph.add('a')
b = Graph.add('b')
c = Graph.add('c')
d = Graph.add('d')
e = Graph.add('e')
f = Graph.add('f')
g = Graph.add('g')
h = Graph.add('h')
Graph.edge(a,b,4)
Graph.edge(a,f,800)
Graph.edge(b,c,2)
Graph.edge(e,g,12)
Graph.edge(c,d,2)
Graph.edge(d,f,12)
Graph.edge(f,h,10)
Graph.edge(e,d,15)
Graph.edge(a,e,12)
Graph.edge(d,h,20)
Graph.edge(g,h,2)
finder = Dijkstras(Graph,a,h)
finder.getDistance()
print(finder.getPath())


       