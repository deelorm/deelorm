import Queue_Linkedlist as queue

class BSTNode(object):
    def __init__(self, data):
        self.data = data 
        self.leftchild = None 
        self.rightchild = None 

    def insert(self, root_node, node_data):
        if root_node is None:
            root_node = BSTNode(node_data)
        else:
            while  root_node is not None:
                if node_data <= root_node.data:
                    root_node = root_node.leftchild 
                else:
                    root_node = root_node.rightchild 
            root_node = BSTNode(node_data)

    def in_order(self, root_node):
        self.in_order(root_node.leftchild)
        print(root_node.data)
        self.in_order(root_node.rightchild)

    def pre_order(self, root_node):
        print(root_node.data)
        self.pre_order(root_node.leftchild)
        self.pre_order(root_node.rightchild)

    def post_order(self, root_node):
        print(root_node.data)
        self.post_order(root_node.leftchild)
        self.post_order(root_node.rightchild)

    def level_order(self, root_node):
        queue.enqueue(root_node)

        while not queue.is_empty():
            bstnode = queue.dequeue()
            print(bstnode.data)
            if bstnode.leftnode is not None:
                queue.enqueue(bstnode.leftchild)
            if bstnode.rightchild is not None:
                queue.enqueue(bstnode.rightchild)

    def search(self, root_node, node_data):
        if root_node is None:
            return 'BST is empty'
        if root_node.data == node_data:
            return True
        else:
            
            while root_node is not None:
                flag_node = 0
                if root_node.leftchild is not None:
                    if root_node.leftchild.data == node_data:
                        return True
                    elif node_data < root_node.leftchild.data:
                        root_node = root_node.leftchild
                        flag_node = 1
                if root_node.rightchild is not None:
                    if flag_node:
                        continue
                    if root_node.rightchild.data == node_data:
                        return True 
                    elif node_data > root_node.rightchild.data:
                        root_node = root_node.rightchild 
        return False

    def minimum_node(self, root_node):
        while root_node.leftchild is not None:
            root_node = root_node.leftchild
        return root_node


    def delete_node(self, root_node, node_data):
        
        if root_node is None:
            return 'BST has no nodes'
        if node_data < root_node.leftchild.data:
            root_node.leftchild = self.delete_node(root_node.leftchild, node_data)
        elif node_data > root_node.rightchild.data:
            root_node.rightchild = self.delete_node(root_node.rightchild, node_data)
        else:
            successor_node = self.minimum_node(root_node.rightchild)
            root_node.data = successor_node.data
            self.delete_node(root_node, successor_node.data)
        return root_node 

    def delete_BST(self):
        self.data = None 
        self.leftchild = None 
        self.rightchild = None 






