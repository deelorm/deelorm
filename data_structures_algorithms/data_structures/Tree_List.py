# Task -- Create a tree data structure with add_child & print functions. Print function overrides built in __str__ function


class Tree:
    '''
Tree structure implementation
    '''
    def __init__(self, data, children=[]):      # Initializes tree class with children parameter set to empty list  
        self.children = children 

    def __str__(self, level=0):     # Traverses and prints individual tree node (string values) when called using print() function 
        tree_str = ' ' * level + str(self.data) + '\n'
        for child in self.children:
            tree_str += child.__str__(level + 1)
        return tree_str 

    def add_child(self, data):       # Adds a child node (left or right child) to the tree structure
        self.children.append(data)


## Sample test inputs

colors = Tree('Colors', [])
green = Tree('Green', [])
violet = Tree('violet', [])
colors.add_child(green)
colors.add_child(violet)

print(colors)