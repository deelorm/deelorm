# Task -- Implement kruskal algorithm using minimum spanning tree with print_graph, add_vertex, add_edge and kruskal functions

# Imported modules

import Disjoint_Set as disjoint

class MST_Graph:
    '''
Graph structure implementation
    ''' 
    def __init__(self, num_vertices):       # Initializes graph structure with num_vertices passed as parameter
        self.num_vertices = num_vertices 
        self.graph = []
        self.vertices = []
        self.MST = []

    def add_vertex(self, vertex):       # Adds vertex to graph
        self.vertices.append(vertex)

    def add_edge(self, source, destination, weight):      # Adds edge to graph with source, destination vertices and edge weight passed as parameters
        self.graph.append([source, destination, weight])

    def print_graph(self):      # Prints graph
        for source, destination, weight in self.MST:
            print("{} - {} -> {}".format(source, destination, weight))

    def kruskal(self):        # Finds minimum spanning tree      
        index1 = 0
        index2 = 0
        self.graph = sorted(self.graph, key=lambda i : i[2])
        disjoint_set = disjoint.Disjoint_Set(self.vertices)

        while index1 < len(self.vertices) - 1:
            source, destination, weight = self.graph[index2]
            index2 += 1
            node_source = disjoint_set.find_set(source)
            node_destination = disjoint_set.find_set(destination)

            if node_source is not node_destination:
                self.MST.append([source, destination, weight])
                disjoint_set.union(node_source, node_destination)
                index1 += 1
        self.print_graph()


## Sample test inputs

mst_graph = MST_Graph(4)
mst_graph.add_vertex('A')
mst_graph.add_vertex('B')
mst_graph.add_vertex('C')
mst_graph.add_vertex('D')

mst_graph.add_edge('A', 'B',2)
mst_graph.add_edge('B', 'A', 2)
mst_graph.add_edge('B', 'C', 3)
mst_graph.add_edge('C', 'B', 3)

mst_graph.add_edge('C', 'D', 4)
mst_graph.add_edge('D', 'C', 4)
mst_graph.add_edge('D', 'A', 2)
mst_graph.add_edge('A', 'D', 2)

mst_graph.kruskal()