# Task -- Implement dijkstra algorithm using graph structure with edge, vertex and dijkstra classes

# Imported modules

import heapq 


class Edge:
    '''
Graph edge structure implementation
    '''
    def __init__(self, source_vertex, destination_vertex, weight):      # Initializes vertex structure with source, destination vertices and edge weight passed as parameters
        self.source_vertex = source_vertex 
        self.destination_vertex = destination_vertex 
        self.weight = weight 

class Vertex:
    '''
Graph vertex structure implementation
    '''
    def __init__(self, name):       # Initializes vertex structure with name passed as parameter
        self.name = name 
        self.visited = False 
        self.predecessor = None 
        self.neighbors = []
        self.distance = float('inf')

    def add_edge(self, destination_vertex, weight): # Adds edge to graph with source, destination vertices and edge weight passed as parameters
        edge = Edge(self, destination_vertex, weight)
        self.neighbors.append(edge)

    def __lt__(self, vertex):       # Overrides __lt__ function with vertex passed as parameter
        return self.distance < vertex.distance


class Dijkstra:
    '''
Dijkstra class implementation
    '''
    def __init__(self):     # Initializes class structure 
        self.heap = []

    def shortest_path(self, vertex):       # Calculates shortest path with starting vertex passed as parameter
        vertex.distance = 0
        heapq.heappush(self.heap, vertex)
        while self.heap: 
            current_vertex = heapq.heappop(self.heap)
            if current_vertex.visited:
                continue 
            for edge in current_vertex.neighbors:
                source_vertex = edge.source_vertex 
                destination_vertex = edge.destination_vertex 
                destination_vertex.distance
                if source_vertex.distance + edge.weight < destination_vertex.distance:
                    destination_vertex.distance = source_vertex.distance + edge.weight
                    destination_vertex.predecessor = current_vertex
                    heapq.heappush(self.heap, destination_vertex)
            current_vertex.visited = True 


    def get_shortest_path(self, vertex):    # Prints out shortest path with destination vertex passed as parameter 
        print('The shortest path to {} is {}'.format(vertex.name, vertex.distance))
        current_vertex = vertex 
        while current_vertex:
            print(current_vertex.name, end=' ')
            current_vertex = current_vertex.predecessor
        print('')

## Sample test inputs

A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')

A.add_edge(B, 2)
A.add_edge(C, 3)

B.add_edge(C, 3)
B.add_edge(D, 4)

C.add_edge(D, 5)
C.add_edge(B, 3)

D.add_edge(A, 5)
D.add_edge(E, 2)

E.add_edge(B, 1)
E.add_edge(C, 2)

dij_algorithm = Dijkstra()
dij_algorithm.shortest_path(A)
dij_algorithm.get_shortest_path(E)
