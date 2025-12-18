# Task -- Create a circular doubly linked list with append, prepend, get, set_value, insert, search, remove, traversal, delete, pop_first, pop, & print functions

class Node:
    '''
Node for circular doubly linked list implementation
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None 
        self.prev = None  


class CDLinkedlist:
    '''
Circular doubly linked list implementation
    '''
    def __init__(self): # Initializes linked list with head and tail set to None and length to 0
        self.head = None 
        self.tail = None 
        self.length = 0


    def __str__(self): # Prints linked list or node values in linked list when using print() function 
        result = ''
        node = self.head 
        while node:
            result += str(node.data)
            if node.next is not self.head: 
                result += ' <==> '
            node = node.next 
            if node is self.head:
                break
        return result 


    def append(self, data): # Adds node to the end of linked list at index = length - 1
        newnode = Node(data)
        current = self.head 
        if current is None:
            self.head = newnode 
            self.tail = newnode 
            self.next = newnode 
            self.prev = newnode 
        else:
            self.tail.next = newnode 
            newnode.prev = self.tail 
            self.tail = newnode
            newnode.next = self.head
            self.head.prev = newnode
        self.length += 1


    def prepend(self, data):  # Adds node to the beginning of the linked list at index 0
        newnode = Node(data)
        current = self.head 
        if current is None:
            self.head = newnode 
            self.tail = newnode 
            self.next = newnode 
            self.prev = newnode
        else:
           newnode.next =  current 
           current.prev = newnode 
           self.head = newnode 
           newnode.prev = self.tail 
           self.tail.next = newnode
        self.length += 1


    def get(self, index): # Returns node at index in linked list
        current = self.head
        if index < 0 or index > self.length - 1:
            return 'Index out of range'
        if current is None:
            return 'List is empty'
        for _ in range(index):
            current = current.next 
        return current 
        
    
    def set_value(self, index, data): # Modifies node at given index with value in linked list
        current = self.head 
        if index < 0 or index > self.length - 1:
            return 'Index out of range'
        if current is None:
            return 'List is empty'
        else:
            for _ in range(index):
                current = current.next 
            current.data = data 


    def insert(self, index, data): # Inserts new node before node at index
        current = self.head 
        if index < 0 or index > self.length - 1:
            return 'Index out of range'
        newnode = Node(data)
        if current is None:
            self.head = newnode 
            self.tail = newnode 
            self.next = newnode 
            self.prev = newnode
        else:
            if index == 0:
                newnode.next = self.head 
                self.head.prev = newnode 
                self.head = newnode  
                newnode.prev = self.tail
                self.tail.next = self.head 
            else:
                for _ in range(index - 1):
                    current = current.next 
                newnode.next = current.next 
                newnode.prev = current
                current.next.prev = newnode
                current.next = newnode 
        self.length += 1


    def search(self, data): # Search for a given node value in list and returns index of node
        current = self.head
        index = 0
        if current is None:
            return 'List is empty'
        else:
            while current:
                if current.data == data:
                    return index
                current = current.next
                index += 1
            return 'Data not found in list'


    def traversal(self): # Prints nodes in linked list
        current = self.head 
        while current:
            print(current.data)
            current = current.next 
            if current is self.head:
                return 
        return 'List is empty'
    

    def remove(self, index): # Removes node with given index
        current = self.head 
        if current is None:
            return 'List is empty'
        if index < 0 or index > self.length - 1:
            return 'Index out of range'
        if index == 0:
            if self.length == 1:
                self.head = None 
                self.tail = None 
            else:
                self.head = self.head.next 
                current.next = None 
                current.prev = None 
                self.head.prev = self.tail 
                self.tail.next = self.head  
        else:
            for _ in range(index - 1):
                current = current.next 
            if current.next == self.tail:
                nextnode = current.next
                current.next = self.head 
                self.head.prev = current 
                self.tail = current
                nextnode.next = None 
                nextnode.prev = None
            else:
                current.next.next.prev = current 
                current.next = current.next.next
        self.length -= 1

    
    def pop_first(self): # Deletes first node from linked list
        current = self.head 
        if current == None:
            return 'List is empty'
        if self.length == 1:
            self.head = None 
            self.tail == None 
        else:
            popped_node = self.head
            self.head = self.head.next 
            popped_node.next = None 
            popped_node.prev = None 
            self.head.prev = self.tail 
            self.tail.next = self.head
        self.length -= 1
        return current


    def pop(self): # Deletes last node from linked list
        current = self.head 
        if current == None:
            return 'List is empty'
        if self.length == 1:
            self.head = None 
            self.tail == None 
        else:
            for _ in range(self.length - 2):
                current = current.next 
            popped_node = self.tail
            self.tail = current 
            self.tail.next = self.head
            self.head.prev = self.tail 
            popped_node.next = None 
            popped_node.prev = None 
        self.length -= 1 
        return popped_node


    def delete(self): # Deletes all nodes in linked list
        self.head = None 
        self.tail = None


## Sample test inputs  

cdll = CDLinkedlist()
cdll.append(5)
cdll.append(10)
cdll.append(15)
cdll.append(20)
cdll.append(25)
print(cdll)

# cdll.delete()
# print(type(cdll))

# print(cdll.pop().data)
# print(cdll)

# print(cdll.pop_first().data)
# print(cdll)

# cdll.remove(4)
# print(cdll)

# cdll.traversal()

# print(cdll.search(25))
# cdll.insert(0,9)
# cdll.insert(3,19)
# cdll.insert(6, 29)
# print(cdll)

# cdll.set_value(0,9)
# cdll.set_value(2,19)
# cdll.set_value(4, 30)
# print(cdll)

# print(cdll.get(2).data)
# cdll.prepend(1)
# cdll.prepend(2)
# print(cdll)




