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
            current = self.todo.remove()
            edges = self.graph.neighbors(current.value)
            node = edges[0].node
            for x in range(0,len(edges)):
                if not node.done:
                    cost = edges[x].cost
                    node = edges[x].node
                    dist = current.value.distance + cost
                    if node.distance is None or dist <= node.distance:
                        node.distance = current.value.distance + cost
                    if  current.value == self.end:
                        return
                    self.todo.add(dist,node)

            current.value.done = True
            print(current)
        return None
    def getPath(self):
        Con = True
        self.path = []
        self.path.append(self.end)
        current = self.end
        while Con:
            neighbors = self.graph.neighbors(current)
            next = neighbors[0].node
            for x in range(0,len(neighbors)):
                if neighbors[x].node.distance <= next.distance:
                    next = neighbors[x].node
            current = next
            self.path.append(current)
            if current == self.start:
                Con = False
                continue
        self.path.reverse()
        return self.path

        
                

Graph = WeightedGraph.Graph()
x = Graph.add(5)
y = Graph.add(4)
z = Graph.add(3)
Graph.edge(x,y,5)
Graph.edge(y,z,5)
Graph.edge(x,z,1000)
finder = Dijkstras(Graph,x,z)
finder.getDistance()
print(finder.getPath())


       