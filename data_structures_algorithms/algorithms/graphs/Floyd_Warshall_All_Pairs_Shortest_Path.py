# Task -- Implement floyd_warshall alogorithm using graph structure with print_graph and floyd_warshall function

# Initialized variables 

inf = float('inf')

class Graph:
    '''
Graph structure implementation
    '''    
    def __init__(self, graph, num_vertices):     # Initializes graph structure with num_vertices passed as parameter 
        self.graph = graph 
        self.num_vertices = num_vertices

    def print_graph(self):      # Prints graph
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                if self.graph[k][i] is inf:
                    print('inf ', end=' ')
                else:
                    print(self.graph[k][i], end=' ')
            print('')

    def floyd_warshall(self):       # Finds shortest path 
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for l in range(self.num_vertices):
                    self.graph[i][l] = min(self.graph[i][l], self.graph[i][k] + self.graph[k][l])
        self.print_graph()


## Sample test inputs

graph = [[0, 8, inf, 1],
         [2, 1, 0, 0],
         [0, inf, 5, 1],
         [0, 4, inf, 0],
        ]

floyd_graph = Graph(graph, 4)
floyd_graph.floyd_warshall()

