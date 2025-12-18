# Task -- Implement bellman ford algorithm using graph structure with bellman ford class

class Graph:
    '''
Graph structure implementation
    '''
    def __init__(self, num_vertices):        # Initializes graph structure with num_vertices passed as parameter 
        self.num_vertices = num_vertices
        self.graph = []
        self.vertices = []

    def add_node(self, data):       # Adds vertex to graph 
        self.vertices.append(data)

    def add_edge(self, source_vertex, destination_vertex, weight):      # Adds edge to graph with source, destination vertices and edge weight passed as parameters
        self.graph.append([source_vertex, destination_vertex, weight])

    def print_graph(self, vertex_distance):     # Prints graph with vertex_distance list passed as parameter 
        for i,k in vertex_distance.items():
            print('Source ---->  Distance')
            print(' ', i, ':        ', k)

    def bellman_ford(self, vertex):     # Checks if negative cycle exists in graph with starting vertex passed as parameter  and prints 'Graph contains negative cycle' otherwise None 
        vertex_distance = {i : float('inf') for i in self.vertices}
        vertex_distance[vertex] = 0

        for _ in range(self.num_vertices - 1):
            for source, destination, weight in self.graph:
                if vertex_distance[source] != float('inf') and vertex_distance[destination] > (vertex_distance[source] + weight):
                    vertex_distance[destination] = vertex_distance[source] + weight 
        
        for source, destination, weight in self.graph:
                if vertex_distance[source] != float('inf') and vertex_distance[destination] > (vertex_distance[source] + weight):
                    print('Graph contains negative cycle')

        self.print_graph(vertex_distance)


## Sample test inputs

graph = Graph(5)
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
# graph.add_node('D')
# graph.add_node('E')

# graph.add_edge('A', 'B', 2)
# graph.add_edge('A', 'C', 3)
# graph.add_edge('B', 'C', 3)
# graph.add_edge('B', 'D', 4)
# graph.add_edge('C', 'D', 5)
# graph.add_edge('C', 'B', 5)
# graph.add_edge('D', 'A', -5)
# graph.add_edge('D', 'E', 2)
# graph.add_edge('E', 'B', 1)
# graph.add_edge('E', 'C', 2)

graph.add_edge('A', 'B', 2)
graph.add_edge('B', 'C', 0)
graph.add_edge('C', 'A', -3)


graph.bellman_ford('A')
