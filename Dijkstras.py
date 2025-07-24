import WeightedGraph
import MinHeap

class Dijkstras():
    def __init__(self,Graph,Start,End):
        self.graph = Graph
        self.start = Start
        self.end = End
        self.todo = MinHeap.Heap()
        
    def getDistance(self):
        self.todo.add(0,self.start)
        done = False
        for x in range(0,len(self.graph.nodes)):
            self.graph.nodes[x].distance = None
            self.graph.nodes[x].done = False
        self.start.distance = 0
        while not done:
            print(self.todo.Heap)
            current = self.todo.remove()
            print(current)
            edges = self.graph.neighbors(current.value)
            node = edges[0].node
            for x in range(0,len(edges)):
                if  current.value == self.end:
                        for x in range(0,len(self.graph.nodes)):
                            print(self.graph.nodes[x].distance)

                        return
                node = edges[x].node
                if not node.done:
                    cost = edges[x].cost
                    dist = current.value.distance + cost
                    if node.distance is None or dist <= node.distance:
                        node.distance = current.value.distance + cost
                    self.todo.add(node.distance,node)

            current.value.done = True
        return None
    def getPath(self):
        Con = True
        self.path = []
        self.path.append(self.end)
        current = self.end
        while Con:
            neighbors = self.graph.neighbors(current)
            next = neighbors[0]
            for x in range(0,len(neighbors)):
                if neighbors[x].node.distance+neighbors[x].cost <= next.node.distance+next.cost:
                    next = neighbors[x]
            current = next.node
            self.path.append(current)
            if current == self.start:
                Con = False
                continue
        self.path.reverse()
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


       