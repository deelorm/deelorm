# Task -- Create a binary tree data structure using Python list with insert, inorder_traversal, preorder_traversal, postorder_traversal, level_order_traversal,
# Cont'd -- search, delete_node, and delete_tree functions


class BTree:
    '''
Binary tree structure implementation
    '''
    def __init__(self, size):       # Initializes binary tree class with size as parameter
        self.maxsize = size + 1
        self.tree_list = [None] * self.maxsize
        self.last_index = 0
        
    def insert(self, node_data):    # Adds new node to the binary tree with node data passed as parameter
        if self.last_index is not self.maxsize:
            self.tree_list[self.last_index + 1] = node_data
            self.last_index += 1

    def inorder_traversal(self, index):      # Traverses nodes in the binary tree structure inorder wise i.e. left child, root, and right child nodes with index passed as parameter
        if index > self.last_index:
            return 
        self.inorder_traversal(2 * index)
        print(self.tree_list[index])
        self.inorder_traversal(2 * index + 1)

    def preorder_traversal(self, index):    # Traverses nodes in the binary tree structure pre-order wise i.e. root, left child and right child nodes with index passed as parameter
        if index > self.last_index:
            return 
        print(self.tree_list[index])
        self.inorder_traversal(2 * index)
        self.inorder_traversal(2 * index + 1)

    def postorder_traversal(self, index):   # Traverses nodes in the binary tree structure post-order wise i.e. left child, right child and root nodes with index passed as parameter
        if index > self.last_index:
            return 
        self.inorder_traversal(2 * index)
        self.inorder_traversal(2 * index + 1)
        print(self.tree_list[index])

    def level_order_traversal(self):        # Traverses nodes in the binary tree structure level- wise i.e levels 0, 1, 2, etc. with size passed as parameter
        for i in range(1, self.last_index + 1):
            print(self.tree_list[i])

    def search(self, node_data):            # Searches for a particular node in the binary tree (using passed parameter - node data to be searched), prints 'Item found' if it exists, otherwise 'Item not found' 
        for i in range(1, self.last_index + 1):
            if self.tree_list[i] is node_data:
                print('Item found')
                return
        print('Item not found')

    def delete_node(self, node_data):        # Deletes a node in the binary tree with given node data (to be deleted) as parameter, and returns 1 otherwise it prints 'Item not in tree'
        last_node = self.tree_list[self.last_index]
        for i in range(1, self.last_index + 1):
            if self.tree_list[i] is node_data:
                self.tree_list[i] = last_node
                self.tree_list[self.last_index] = None
                self.last_index -= 1
                return 1
        print('Item not in tree')

    def delete_tree(self):           # Deletes entire binary tree
        self.tree_list = None
        self.last_index = 0


## Main function with sample test inputs
if __name__ == '__main__':

    tree = BTree(5)
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    #print(tree.tree_list)
    tree.inorder_traversal(1)
    #tree.level_order_traversal()
    #tree.search(60)
    #tree.delete_node(10)
    tree.delete_tree()
    print('-------')
    tree.inorder_traversal(1)