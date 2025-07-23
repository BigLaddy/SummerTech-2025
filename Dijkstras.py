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
        while not done:
            current = self.todo.remove()
            edges = self.graph.neighbors(current)
            for x in range(0,len(edges)):
                if not node.done:
                    cost = self.graph.getCost(edges[x])
                    node = edges[x]
                    dist = current.distance + cost
                    if node.distance is None or dist <= node.distance:
                        node.distance = current.distance + cost
                    if node == self.end:
                        return
                    self.todo.add(cost,node)
            current.done = True
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
                if neighbors[x].distance <= next.distance:
                    next = neighbors[x]
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
Graph.edge(x,y,5)
finder = Dijkstras(Graph,x,y)
finder.getDistance()


       