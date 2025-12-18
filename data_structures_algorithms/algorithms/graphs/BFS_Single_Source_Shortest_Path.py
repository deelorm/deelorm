# Task -- Implement shortest path breadth first search (BFS_SSSP) algorithm using graph structure with graph and BFS_SSSP functions


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
        

    def BFS_SSSP(self, source, dest):       # Finds shortest path with source vertex and dest (destination) vertex passed as parameters 
        bfs_list = [list(source)]
        while bfs_list:
            bfs_path = bfs_list.pop(0)
            bfs_node = bfs_path[-1]
            if bfs_node is dest:
                return bfs_path 
            for adj_node in self.graph_list[bfs_node]:
                adj_path = bfs_path
                adj_path.append(adj_node)
                bfs_list.append(adj_path)


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

print('-------------------')

print(graph.BFS_SSSP('A', 'C'))



