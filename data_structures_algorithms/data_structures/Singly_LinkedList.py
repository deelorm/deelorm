# Task -- Create a circular singly linked list with append, prepend, get, set_value, insert, search, remove, traversal, delete & print functions

class Node:
    '''
 Node for singly linked list implementation
    '''
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    '''
Singly linked list implementation
    '''
    def __init__(self): # Initializes linked list with head and tail set to None and length to 0
        self.head = None
        self.tail = None
        self.length = 0

    def printList(self): # Prints node values in linked list
        node = self.head
        while node:
            print(node.value, end='')
            if node.next is not None:
                print(' -> ', end='')
            node = node.next
        print('')

    def prepend(self, value): # Adds node to the beginning of the linked list at index 0
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else: 
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def append(self, value): # Adds node to the end of linked list at index = length - 1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def insert(self, index, value): # Inserts new node before node at index
        new_node = Node(value)
        if index < 0 or index > self.length - 1:
            self.tail.next = new_node
            self.tail = new_node 
            return True        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        node = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            for _ in range(index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
            self.length += 1

    def search(self, value): # Searches for a particluar node in linked list
        node = self.head
        index = 0
        if node is None:
            return None
        while node:
            if node.value == value:
                return index
            node = node.next
            index += 1
        return None

    def traverse(self): # Prints nodes in linked list
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def get(self, index): # Returns node at index in linked list
        node = self.head
        if not node:
            return None
        else:
            for _ in range(index):
                node = node.next
            return node

    def set(self, index, value): # Modifies node at given index with value in linked list
        node = self.head
        new_node = Node(value)
        if not node:
            self.head = new_node
            self.tail = new_node
            return True
        if index < 0 or index > self.length:
            self.tail.next = new_node
            self.tail = new_node
            return True
        else:
            for _ in range(index):
                node = node.next
            node.value = value
            return True

    def remove(self, value): # Removes node with given value
        node = self.head
        if not node:
            return None
        else:
            if self.length == 1:
                if node.value == value:
                    self.head = None
                    self.tail = None
                    self.length -= 1
            else:
                while node:
                    if node.value == value:
                        if node == self.head:
                            self.head = self.head.next
                        elif node.next == None:
                            prev.next = None
                            self.tail = prev
                            self.length -= 1
                        else:
                            prev.next = node.next
                            self.length -= 1
                    prev = node
                    node = node.next

    def delete(self): # Deletes all nodes in linked list  
        node = self.head
        if node == None:
            return None
        else:
            self.head = None
            self.tail = None

    def reverse(self): # Reverses order of linked list 
        node = self.head
        if not node:
            return None
        else:
            prev = None
            temp = None
            self.tail = node
            while node.next is not None:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            node.next = prev
            self.head = node


## Sample test inputs

# 10->20->30->40

linkedlist = LinkedList()
linkedlist.append(10)
linkedlist.append(20)
linkedlist.prepend(5)
#linkedlist.insert(1, 15)
linkedlist.insert(0,1)
linkedlist.insert(4,30)

linkedlist.printList()
linkedlist.set(-1,45)
linkedlist.printList()
linkedlist.reverse()
linkedlist.printList()
print(Node.__doc__)





