maxsize = 100000
class Graph(): 
   
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        
        ### Modified
        # Array of verticies
        self.arr_of_v = []
    

    ### Modified
    def addEdge(self, e1, e2, cost):
        # Add Edges to Array of edges
        if e1 not in self.arr_of_v:
            self.arr_of_v.append(e1)
        
        if e2 not in self.arr_of_v:
            self.arr_of_v.append(e2)
        
        # Index values of edges 
        i_e1 = self.arr_of_v.index(e1)
        i_e2 = self.arr_of_v.index(e2)

        # Add edge to adjecancy Matrix
        self.graph[i_e1][i_e2] = cost
        self.graph[i_e2][i_e1] = cost
   
    def printSolution(self, dist, src, dest): 
        ### Modified 
        print ("Vertex tDistance from Source") 
        for node in range(self.V): 
            print(src, 'to', self.arr_of_v[node], "is", dist[node])

            # Stop If Destination reached
            if self.arr_of_v[node] == dest:
                break
   
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
   
        # Initilaize minimum distance for next node 
        min = maxsize 
   
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index 
   
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, source, dest): 
        ### Modified
        src = self.arr_of_v.index(source)


        dist = [maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
   
        for cout in range(self.V): 
   
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
   
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
   
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 

        ### Modified 
        self.printSolution(dist, source, dest) 
   
# Test 1

g = Graph(6)

# Add edges with weight
g.addEdge('a', 'b', 4)
g.addEdge('a', 'c', 2)
g.addEdge('b', 'c', 1)
g.addEdge('b', 'd', 5)
g.addEdge('c', 'd', 8)
g.addEdge('c', 'e', 10)
g.addEdge('d', 'e', 2)
g.addEdge('d', 'z', 6)
g.addEdge('e', 'z', 5)

# Dijkstras Algo
g.dijkstra('a', 'z')