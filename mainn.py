from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isycyclic(self,v,visited,recrStack):
        #mark  the current node as visited and add it to recursion stack
        visited[v] = True
        recrStack[v] = True

        #recur through the neighbors
        #if any neighbor is visited and in recursion stack then graph is cyclic
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.isycyclic(neighbor,visited,recrStack) == True:
                    return True
            elif recrStack[neighbor] ==True:
                return True
        #the node has to be popped out before function ends
        recrStack[v] = False
        return False
    
    def isycycle(self):
        visited = [False] * (self.V +1)
        recurStack = [False] * (self.V+1)
        for i in range(self.V):
            if visited[i] == False:
                if self.isycyclic(i,visited,recurStack)== True:
                    return True
        return False
        
g = Graph(5)
g.addEdge(0,3)
g.addEdge(2,3)
g.addEdge(3,4)
if g.isycycle() == 1:
    print("Graph has a cycle")
else:
    print("Graph doesnt have a cycle. ")




