# Task -- Create AVL data structure using linked list  with insert, inorder_traversal, preorder_traversal, postorder_traversal, level_order_traversal,
# Cont'd -- get_height, get_balance, right_rotate, left_rotate, minimun_node, search, delete, and delete_tree functions


# Imported modules
import Queue_LinkedList as queue

class AVL:
    '''
AVL tree structure implementation
    '''
    def __init__(self, data):        # Initializes AVL tree class with data as parameter
        self.data = data 
        self.leftchild = None 
        self.rightchild = None 
        self.height = 0

    def inorder_traversal(self, root_node):     # Traverses nodes in the AVL tree structure inorder wise i.e. left child, root, and right child nodes with root node passed as parameter
        if not root_node:
            return 
        self.inorder_traversal(root_node.leftchild)
        print(root_node.data)
        self.inorder_traversal(root_node.rightchild)

    def preorder_traversal(self, root_node):    # Traverses nodes in the AVL tree structure pre-order wise i.e. root, left child and right child nodes with root node passed as parameter
        if not root_node:
            return 
        print(root_node.data)
        self.preorder_traversal(root_node.leftchild)
        self.preorder_traversal(root_node.rightchild)

    def postorder_traversal(self, root_node):   # Traverses nodes in the AVL tree structure post-order wise i.e. left child, right child and root nodes with root node passed as parameter
        if not root_node:
            return 
        self.postorder_traversal(root_node.leftchild)
        self.postorder_traversal(root_node.rightchild)
        print(root_node.data)

    def level_order_traversal(self, root_node):     # Traverses nodes in the AVL tree structure level- wise i.e levels 0, 1, 2, etc. with root node passed as parameter
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

    def get_height(self, root_node):        # Returns height of AVL tree node
        if not root_node:
            return 0
        return root_node.height

    def get_balance(self, root_node):       # Returns the height difference between AVL tree node left child and right child
        if not root_node:
            return 0
        right_height = self.get_height(root_node.rightchild)
        left_height = self.get_height(root_node.leftchild)
        return left_height - right_height

    def right_rotate(self, unbal_node):     # Rotates AVL tree node clockwise 
        if not unbal_node:
            return 
        new_root = unbal_node.leftchild
        unbal_node.leftchild = unbal_node.leftchild.rightchild 
        new_root.rightchild = unbal_node
        new_root.height = 1 + max(self.get_height(new_root.leftchild), self.get_height(new_root.rightchild))
        unbal_node.height = 1 + max(self.get_height(unbal_node.leftchild), self.get_height(unbal_node.rightchild))
        return new_root 

    def left_rotate(self, unbal_node):      # Rotates AVL tree node anti-clockwise 
        if not unbal_node:
            return 
        new_root = unbal_node.rightchild 
        unbal_node.rightchild = unbal_node.rightchild.leftchild 
        new_root.leftchild = unbal_node
        new_root.height = 1 + max(self.get_height(new_root.leftchild), self.get_height(new_root.rightchild))
        unbal_node.height = 1 + max(self.get_height(unbal_node.leftchild), self.get_height(unbal_node.rightchild))
        return new_root

    def search(self, root_node, node_data): # Searches for a particular node in the AVL tree (using passed parameters - root node and node data to be searched), prints 'Item found' if it exists, otherwise None
        if not root_node:
            return 
        if node_data < root_node.data:
            root_node.leftchild = self.search(root_node.leftchild, node_data)
        elif node_data > root_node.data:
            root_node.rightchild = self.search(root_node.rightchild, node_data)
        else:
            if node_data is root_node.data:
                print('Item found', node_data)


    def insert(self, root_node, node_data):      # Adds new node to the AVL tree with root node and node data passed as parameters
        if not root_node:
            return 
        if node_data <= root_node.data:
            if not root_node.leftchild:
                root_node.leftchild = AVL(node_data)
            else:
                root_node.leftchild = self.insert(root_node.leftchild, node_data)
        else:
            if not root_node.rightchild:
                root_node.rightchild = AVL(node_data)
            else:
                root_node.rightchild = self.insert(root_node.rightchild, node_data)

        root_node.height = 1 + max(self.get_height(root_node.leftchild), self.get_height(root_node.rightchild))
        balance = self.get_balance(root_node)

        if balance > 0 and node_data <= root_node.leftchild.data:
           return self.right_rotate(root_node)
        if balance > 0 and node_data > root_node.leftchild.data:
            root_node.leftchild = self.left_rotate(root_node.leftchild)
            return self.right_rotate(root_node)
        if balance < 0 and node_data > root_node.rightchild.data:
            return self.left_rotate(root_node)
        if balance < 0 and node_data <= root_node.rightchild.data:
            root_node.rightchild = self.right_rotate(root_node.rightchild)
            return self.left_rotate(root_node)
        return root_node 

    def minimum_node(self, root_node):      # Returns the successor node in the AVL tree, otherwise returns None
        if not root_node:
            return
        while root_node.leftchild:
            root_node = root_node.leftchild
        return root_node 

    def delete(self, root_node, node_data):     # Deletes a node in the AVL tree with given root node and node data (to be deleted) as parameters     
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

        balance = self.get_balance(root_node)

        if balance > 0 and node_data <= self.get_balance(root_node.leftchild) >= 0:
           return self.right_rotate(root_node)
        if balance > 0 and node_data > self.get_balance(root_node.leftchild) < 0:
            root_node.leftchild = self.left_rotate(root_node.leftchild)
            return self.right_rotate(root_node)
        if balance < 0 and node_data > self.get_balance(root_node.rightchild) <= 0:
            return self.left_rotate(root_node)
        if balance < 0 and node_data <= self.get_balance(root_node.rightchild) > 0:
            root_node.rightchild = self.right_rotate(root_node.rightchild)
            return self.left_rotate(root_node)
       
        return root_node

    def delete_tree(self, root_node):       # Deletes entire AVL tree
        self.root_node.data = None 
        self.root_node.leftchild = None 
        self.root_node.rightchild = None


## Main function with sample test inputs
if __name__ == '__main__':

    tree = AVL(10)
    tree = tree.insert(tree, 20)
    tree = tree.insert(tree, 15)

    tree.level_order_traversal(tree)
    print('-----------------------')
    tree = tree.delete(tree, 15)
    tree.level_order_traversal(tree)
    #tree.search(tree, 20)


        