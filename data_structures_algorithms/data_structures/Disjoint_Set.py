# Task -- Create disjoint set data structure  with make_set, find_set, and union functions

class Disjoint_Set:
    '''
Disjoint set structure implementation
    ''' 
    def __init__(self, vertices):       # Initializes disjoint set with vertices list passed as parameters
        self.vertices = vertices 
        self.parent = {}
        self.rank = {}
        self.make_set()

    def make_set(self):     # Implements make_set function
        for i in self.vertices:
            self.parent[i] = i
            self.rank[i] = 0

    def find_set(self, node):       # Implements find_set function
        if self.parent[node] is node:
            return node
        return self.find_set(self.parent[node])

    def union(self, set1, set2):    # Implements union_set function       
        node1 = self.find_set(set1)
        node2 = self.find_set(set2)
        if self.rank[node1] > self.rank[node2]:
            self.parent[node2] = node1 
        elif self.rank[node2] > self.rank[node1]:
            self.parent[node1] = node2 
        else:
            self.parent[node2] = node1
            self.rank[node1] += 1


## Sample test inputs

# vertices = ['A', 'B', 'C', 'D', 'E']
# ds = Disjoint_Set(vertices)
# print(ds.find_set('A'))
# ds.union('A', 'B')
# ds.union('A', 'C')
# print(ds.find_set('A'))
# print(ds.rank['A'])




