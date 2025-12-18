# Task -- Implement prims algorithm using minimum spanning tree with print_graph and prims functions

# Imported modules

import sys 

class MST_Graph:
    '''
Graph structure implementation
    ''' 
    def __init__(self, num_vertices, edges, vertices):     # Initializes graph structure with num_vertices, edges and vertices passed as parameters
        self.num_vertices = num_vertices 
        self.edges = edges 
        self.vertices = vertices 
        self.MST = []

    def print_graph(self):      # Prints graph
        for source, destination, weight in self.MST:
            print('%s - %s -> %s' %(source, destination, weight))

    def prims(self):        # Finds minimum spanning tree
        traversed = [0] * self.num_vertices
        traversed[0] = True
        edge_count = 0
        while edge_count < self.num_vertices - 1:
            min_data = sys.maxsize
            for i in range(self.num_vertices):
                if traversed[i]:
                    for k in range(self.num_vertices):
                        if not traversed[k] and self.edges[i][k]:
                            if self.edges[i][k] < min_data:
                                min_data = self.edges[i][k]
                                source = i 
                                destination = k
            self.MST.append([self.vertices[source], self.vertices[destination], edges[source][destination]])
            traversed[destination] = True
            edge_count += 1
        self.print_graph()


## Sample test inputs

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]
        ]
graph = MST_Graph(5, edges, vertices)
graph.prims()
