# Task -- Create a binary tree data structure using linked list  with insert, inorder_traversal, preorder_traversal, postorder_traversal, level_order_traversal,
# Cont'd -- search, get_last_node, delete_last_node, delete_node, and delete_tree functions

# Imported modules
import Queue_LinkedList as queue

class BTree:
    '''
Binary tree structure implementation
    '''
    def __init__(self, data):       # Initializes binary tree class with data as parameter
        self.data = data 
        self.leftchild = None 
        self.rightchild = None 

    def insert(self, root_node, node_data):     # Adds new node to the binary tree with root node and node data passed as parameters
        if root_node is None:
            return 
        tree_queue = queue.Queue()
        tree_queue.enqueue(root_node)
        while tree_queue:
            root_node = tree_queue.dequeue().data
            if root_node.leftchild is None:
                root_node.leftchild = BTree(node_data)
                print('Node inserted!', node_data)
                return
            else:
                tree_queue.enqueue(root_node.leftchild) 

            if root_node.rightchild is None:
                root_node.rightchild = BTree(node_data)
                print('Node inserted!', node_data)
                return
            else:   
                tree_queue.enqueue(root_node.rightchild)            
    
    def inorder_traversal(self, root_node):     # Traverses nodes in the binary tree structure inorder wise i.e. left child, root, and right child nodes with root node passed as parameter
        if not root_node:
            return
        self.inorder_traversal(root_node.leftchild)
        print(root_node.data)
        self.inorder_traversal(root_node.rightchild)

    def preorder_traversal(self, root_node):    # Traverses nodes in the binary tree structure pre-order wise i.e. root, left child and right child nodes with root node passed as parameter
        if not root_node:
            return
        print(root_node.data)
        self.preorder_traversal(root_node.leftchild)
        self.preorder_traversal(root_node.rightchild)

    def postorder_traversal(self, root_node):   # Traverses nodes in the binary tree structure post-order wise i.e. left child, right child and root nodes with root node passed as parameter
        if not root_node:
            return
        self.postorder_traversal(root_node.leftchild)
        self.postorder_traversal(root_node.rightchild)
        print(root_node.data)

    def level_order_traversal(self, root_node):     # Traverses nodes in the binary tree structure level- wise i.e levels 0, 1, 2, etc. with root node passed as parameter
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

    def search(self, root_node, node_data):     # Searches for a particular node in the binary tree (using passed parameters - root node and node data to be searched), prints 'Item found' if it exists, otherwise 'Item not found' 
        if not root_node:
            return
        tree_queue = queue.Queue()
        tree_queue.enqueue(root_node)
        while not tree_queue.is_empty():
            root_node = tree_queue.dequeue().data 

            if root_node.data is node_data:
                print('Item found')
                return

            if root_node.leftchild:
                if root_node.leftchild.data is node_data:
                    print('Item found')
                    return
                else:
                    tree_queue.enqueue(root_node.leftchild)
            
            if root_node.rightchild:
                if root_node.rightchild.data is node_data:
                    print('Item found')
                    return
                else:
                    tree_queue.enqueue(root_node.rightchild)
        print('Item not found')


    def get_last_node(self, root_node):     # Returns last node in the binary tree
        if not root_node:
            return 
        tree_queue = queue.Queue()
        tree_queue.enqueue(root_node)

        while not tree_queue.is_empty():
            root_node = tree_queue.dequeue().data 
            if not root_node:
                break
            else:
                if root_node.leftchild:
                    tree_queue.enqueue(root_node.leftchild)
                if root_node.rightchild:
                    tree_queue.enqueue(root_node.rightchild)
        return root_node

    def delete_last_node(self, root_node, node_data):       # Deletes last node in the binary tree 
        if not root_node:
            return 
        tree_queue = queue.Queue()
        tree_queue.enqueue(root_node)

        while not tree_queue.is_empty():
            root_node = tree_queue.dequeue().data 
            if not root_node:
                break 
            if root_node.leftchild:
                if root_node.leftchild.data is node_data:
                    root_node.leftchild = None
                    return
                else:
                    tree_queue.enqueue(root_node.leftchild)
            if root_node.rightchild:
                if root_node.rightchild.data is node_data:
                    root_node.rightchild = None
                    return
                else:
                    tree_queue.enqueue(root_node.rightchild)

    def delete_node(self, root_node, node_data):        # Deletes a node in the binary tree with given root node and node data (to be deleted) as parameters, and returns 1 otherwise None
        if not root_node:
            return 
        tree_queue = queue.Queue()
        tree_queue.enqueue(root_node)
        while not tree_queue.is_empty():
            root_node = tree_queue.dequeue().data 
            if root_node.data is node_data:
                last_node = self.get_last_node(root_node)
                self.delete_last_node(root_node, last_node.data)
                if last_node.data is node_data:
                    return 1
                root_node = last_node.data
                return 1

            if root_node.leftchild:
                if root_node.leftchild.data is node_data:
                    last_node = self.get_last_node(root_node)
                    self.delete_last_node(root_node, last_node.data)
                    if last_node.data is node_data:
                        return
                    root_node.leftchild.data = last_node.data
                    return
                else:
                    tree_queue.enqueue(root_node.leftchild)

            if root_node.rightchild:
                if root_node.rightchild.data is node_data:
                    last_node = self.get_last_node(root_node)
                    self.delete_last_node(root_node, last_node.data)
                    if last_node.data is node_data:
                        return
                    root_node.rightchild.data = last_node.data
                    return
                else:
                    tree_queue.enqueue(root_node.rightchild)

    def delete_tree(self, root_node):       # Deletes entire binary tree
        root_node.data = None
        root_node.leftchild = None 
        root_node.rightchild = None


## Main function with sample test inputs
if __name__ == '__main__':

    colors = BTree('Colors')
    colors.insert(colors, 'Green')
    colors.insert(colors, 'Violet')
    colors.insert(colors, 'magenta')
    colors.insert(colors, 'cyan')
    colors.inorder_traversal(colors)
    # colors.preorder_traversal(colors)
    # colors.postorder_traversal(colors)
    # colors.search(colors, 'magenta')
    node_data = colors.get_last_node(colors)
    print('--------------------------')
    #colors.delete_last_node(colors, node_data)
    #colors.delete_node(colors, 'cyan')
    #colors.delete_tree(colors)
    #colors.inorder_traversal(colors)

    colors.level_order_traversal(colors)


