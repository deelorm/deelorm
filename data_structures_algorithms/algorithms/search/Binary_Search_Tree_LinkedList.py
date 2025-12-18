# Task -- Create a binary search tree data structure using linked list with insert, inorder_traversal, preorder_traversal, postorder_traversal, level_order_traversal,
# Cont'd -- search, minimum_node, delete, and delete_tree functions


# Imported modules
import Queue_LinkedList as queue

class BSTree:
    '''
Binary search tree structure implementation
    '''
    def __init__(self, data):       # Initializes binary search tree class with data as parameter
        self.data = data 
        self.leftchild = None 
        self.rightchild = None 

    def insert(self, root_node, node_data):      # Adds new node to the binary search tree with root node and node data passed as parameters
        if not root_node:
            return 
        if node_data <= root_node.data:
            if not root_node.leftchild:
                root_node.leftchild = BSTree(node_data)
                print('Item inserted', node_data)
                return
            else:
                self.insert(root_node.left_child, node_data)
        else:
            if not root_node.rightchild:
                root_node.rightchild = BSTree(node_data)
                print('Item inserted', node_data)
                return
            else:
                self.insert(root_node.rightchild, node_data)


    def inorder_traversal(self, root_node):     # Traverses nodes in the binary search tree structure inorder wise i.e. left child, root, and right child nodes with root node passed as parameter
        if not root_node:
            return 
        self.inorder_traversal(root_node.leftchild)
        print(root_node.data)
        self.inorder_traversal(root_node.rightchild)

    def preorder_traversal(self, root_node):    # Traverses nodes in the binary search tree structure pre-order wise i.e. root, left child and right child nodes with root node passed as parameter
        if not root_node:
            return 
        print(root_node.data)
        self.preorder_traversal(root_node.leftchild)
        self.preorder_traversal(root_node.rightchild)

    def postorder_traversal(self, root_node):    # Traverses nodes in the binary search tree structure post-order wise i.e. left child, right child and root nodes with root node passed as parameter
        if not root_node:
            return 
        self.postorder_traversal(root_node.leftchild)
        self.postorder_traversal(root_node.rightchild)
        print(root_node.data)

    def level_order_traversal(self, root_node):      # Traverses nodes in the binary search tree structure level- wise i.e levels 0, 1, 2, etc. with root node passed as parameter
        if not root_node:
            return 
        tree_queue = queue.Queue()
        tree_queue.enqueue(root_node)
        while not tree_queue.is_empty():
            root_node = tree_queue.dequeue().data
            print(root_node.data)
            if root_node.leftchild:
                tree_queue.enqueue(root_node.leftchild)
            if root_node.rightchild:
                tree_queue.enqueue(root_node.rightchild)

    def search(self, root_node, node_data):     # Searches for a particular node in the binary search tree (using passed parameters - root node and node data to be searched), returns 1 if it exists, otherwise None
        if not root_node:
            return
        if node_data is root_node.data:
            print('Item found', node_data)
            return 1
        if node_data < root_node.data:
            self.search(root_node.leftchild, node_data)

        if node_data > root_node.data:
            self.search(root_node.rightchild, node_data)

    def minimum_node(self, root_node):     # Returns the successor node in the binary search tree, otherwise returns None
        if not root_node:
            return
        while root_node.leftchild:
            root_node = root_node.leftchild
        return root_node 

    def delete(self, root_node, node_data):     # Deletes a node in the binary search tree with given root node and node data (to be deleted) as parameters, otherwise returns None
        if not root_node:
            return 
        if node_data < root_node.data:
            root_node.leftchild = self.delete(root_node.leftchild, node_data)
        elif node_data > root_node.data:
            root_node.rightchild = self.delete(root_node.rightchild, node_data)
        else:
            if not root_node.leftchild:
                temp = root_node.rightchild 
                root_node.rightchild = None 
                return temp 
            if not root_node.rightchild:
                temp = root_node.leftchild 
                root_node.leftchild = None 
                return temp 
            temp = self.minimum_node(root_node.rightchild)
            root_node.rightchild = self.delete(root_node.rightchild, temp.data)
            root_node.data = temp.data
        return root_node

    def delete_tree(self, root_node):     # Deletes entire binary search tree
        root_node.data = None 
        root_node.leftchild = None 
        root_node.rightchild = None


## Main function with sample test inputs
if __name__ == '__main__':

    tree = BSTree(10)
    tree.insert(tree, 5)
    tree.insert(tree, 30)
    # tree.insert(tree, 40)
    # tree.insert(tree, 50)
    tree.level_order_traversal(tree)
    print('-------------')
    #tree.inorder_traversal(tree)
    #tree.preorder_traversal(tree)
    #tree.level_order_traversal(tree)
    #tree.search(tree, 5)
    # tree.delete_tree(tree)
    # tree.level_order_traversal(tree)
    tree.delete(tree, 5)
    tree.level_order_traversal(tree)