# Task -- Implement topological sort function using graph structure with print_graph, add_vertex, add_edge, remove_vertex, remove_edge
# Cont'd -- topological_sort_func, and topological_sort functions


class Graph:
    '''
Graph structure implementation
    '''
    def __init__(self):     # Initializes graph structure 
        self.graph_list = {}

    def print_graph(self):      # Prints graph 
        for vertex in self.graph_list:
            print(vertex, ':', self.graph_list[vertex])

    def add_vertex(self, vertex):      # Adds vertex to graph  
        if vertex not in self.graph_list:
            self.graph_list.update({vertex : []})
            return True 
        return False 

    def add_edge(self, vertex1, vertex2):    # Adds edge to graph with vertex1 and vertex2 passed as parameters 
        if vertex1 in self.graph_list and vertex2 in self.graph_list:
            self.graph_list[vertex1].append(vertex2)
            return True 
        return False 

    def remove_vertex(self, vertex):     # Removes vertex from graph
        if vertex in self.graph_list:
            for adj_vertex in self.graph_list[vertex]:
                if vertex in self.graph_list[adj_vertex]:
                    self.graph_list[adj_vertex].remove(vertex)
            del self.graph_list[vertex]
            return True 
        return False 

    def remove_edge(self, vertex1, vertex2):        # Removes edge from graph with vertex1 and vertex2 passed as parameters 
        if vertex1 in self.graph_list and vertex2 in self.graph_list:
            if vertex1 in self.graph_list[vertex2]:
                self.graph_list[vertex2].remove(vertex1)
            if vertex2 in self.graph_list[vertex1]:
                self.graph_list[vertex1].remove(vertex2)
            return True 
        return False

    def topological_sort_func(self, traversed_list, vertex, topol_list):    # Sorts list topologically with traversed_list,vertex and topol_list passed as parameters 
        traversed_list.add(vertex)
        for node in self.graph_list[vertex]:
            if node not in traversed_list:
                self.topological_sort_func(traversed_list, node, topol_list)

        topol_list.append(vertex)


    def topological_sort(self):     # Sorts list by calling topological_sort_func        
        traversed_list = set()
        topol_list = []
        for vertex in self.graph_list:
            if vertex not in traversed_list:
                self.topological_sort_func(traversed_list, vertex, topol_list)
        topol_list.reverse()
        return topol_list


## Sample test inputs

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')


graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')

# graph.print_graph()


# graph.remove_edge('B', 'C')
print('-------------------')
# graph.print_graph()

print(graph.topological_sort())
