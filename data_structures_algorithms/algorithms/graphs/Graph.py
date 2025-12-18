# Task -- Create graph structure with print_graph, add_vertex, add_edge, remove_vertex, remove_edge, breadth first search (BFS), and depth first search (DFS) functions

class Graph:
    '''
Graph structure implementation
    '''
    def __init__(self):     # Initializes graph structure 
        self.graph_list = {}

    def print_graph(self):  # Prints graph 
        for node in self.graph_list:
            print(node, ':', self.graph_list[node])

    def add_vertex(self, vertex):   # Adds vertex to graph 
        if vertex not in self.graph_list:
            self.graph_list[vertex] = []
            return True 
        return False 

    def add_edge(self, vertex1, vertex2):       # Adds edge to graph with vertex1 and vertex2 passed as parameters
        if vertex1 in self.graph_list and vertex2 in self.graph_list:
            self.graph_list[vertex1].append(vertex2)
            self.graph_list[vertex2].append(vertex1)
            return True 
        return False

    def remove_edge(self, vertex1, vertex2):    # Removes edge from graph with vertex1 and vertex2 passed as parameters
        if vertex1 in self.graph_list and vertex2 in self.graph_list:
            self.graph_list[vertex1].remove(vertex2)
            self.graph_list[vertex2].remove(vertex1)
            return True 
        return False 

    def remove_vertex(self, vertex):       # Removes vertex from graph
        if vertex in self.graph_list:
            for list_vertex in self.graph_list[vertex]:
                self.graph_list[list_vertex].remove(vertex)
            del self.graph_list[vertex]
            return True 
        return False 

    def BFS(self, vertex):      # Traverses nodes in graph structure level- wise i.e levels 0, 1, 2, etc. with starting vertex passed as parameter
        traversed_list = set()
        traversed_list.add(vertex)
        bfs_list = [vertex]
        while bfs_list:
            current_vertex = bfs_list.pop(0) 
            print(current_vertex, end=' ')
            
            for adj_vertex in self.graph_list[current_vertex]:
                if adj_vertex not in traversed_list:
                    traversed_list.add(adj_vertex)
                    bfs_list.append(adj_vertex)
        print('')

    def DFS(self, vertex):      # Traverses nodes in graph structure deepest nodes first with starting vertex passed as parameter
        traversed_list = set()
        dfs_list = [vertex]

        while dfs_list:
            current_vertex = dfs_list.pop()
            if current_vertex not in traversed_list:
                print(current_vertex, end=' ')
                traversed_list.add(current_vertex)

                for adj_vertex in self.graph_list[current_vertex]:
                    if adj_vertex not in traversed_list:
                        dfs_list.append(adj_vertex)

        print('')


## Sample test inputs

graph = Graph()
graph.add_vertex('S')
graph.add_vertex('D')
graph.add_vertex('F')
graph.add_vertex('H')
graph.add_edge('S', 'F')
graph.add_edge('S', 'D')
graph.add_edge('D', 'F')
graph.add_edge('S', 'H')
graph.print_graph()
print('-----------------')
#graph.remove_edge('S', 'F')
# graph.remove_vertex('D')
# graph.print_graph()

#graph.BFS('S')
graph.DFS('S')

