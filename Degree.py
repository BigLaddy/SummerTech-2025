import multiprocessing
import WeightedGraph
list = []
pipes = []
def getNode(Node,Pipe):
    global list
    cost = Node.edges[0].cost 
    for x in range(0,len(Node.edges)):
        if Node.edges[x].cost > cost:
            cost = Node.edges[x].cost
    Pipe[0].send(cost)
    


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
for x in range(0,len(Graph.nodes),1):
    #O(n + max degree) span
    #O(n * max degree) work
    Pipe = multiprocessing.Pipe()
    pipes.append(Pipe)
    Process = multiprocessing.Process(target = getNode,args = [Graph.nodes[x],Pipe])
    Process.start()
for x in range(0,len(Graph.nodes)):
    list.append(pipes[x][1].recv())
print(list)