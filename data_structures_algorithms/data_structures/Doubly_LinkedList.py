# Task -- Create a doubly linked list with append, prepend, get, set_value, insert, search, remove, traversal, delete, pop_first, pop, & print functions

class Node:
    '''
 Node for doubly linked list implementation
    '''    
    def __init__(self, value=0):
        self.value = value 
        self.next = None 
        self.prev = None

class DoublyLinkedList:
    '''
Doubly linked list implementation
    '''
    def __init__(self): # Initializes linked list with head and tail set to None and length to 0
        self.head = None 
        self.tail = None 
        self.length = 0

    def __str__(self): # Prints linked list or node values in linked list using print() function
        result = ''
        current = self.head 
        while current:
            result += str(current.value)
            if current.next:
                result += ' <-> '
            current = current.next 
        return result

    def append(self, value): # Adds node to the end of linked list at index = length - 1
        current = self.head 
        newnode = Node(value)
        if not current:
            self.head = newnode 
            self.tail = newnode 
            self.length += 1
            return
        if self.length == 1:
            current.next = newnode 
            newnode.prev = self.head 
            self.tail = newnode 
            self.length += 1 
        else:
            self.tail.next = newnode 
            newnode.prev = self.tail 
            self.tail = newnode 
            self.length += 1 

    def prepend(self, value): # Adds node to the beginning of the linked list at index 0
        current = self.head 
        newnode = Node(value)
        if not current:
            self.head = newnode 
            self.tail = newnode 
            self.length += 1 
        else:
            newnode.next = self.head 
            self.head.prev = newnode
            newnode.next = self.head 
            self.head = newnode
            self.length += 1 

    def traversal(self): # Prints nodes in linked list
        current = self.head 
        if not current:
            return None 
        else:
            while current:
                print(current.value)
                current = current.next

    def reverse_traversal(self): # Prints nodes in linked list in reverse order 
        current = self.tail
        if not current:
            return None 
        else:
            while current:
                print(current.value)
                current = current.prev 

    def insert(self, index, value): # Inserts new node before node at index
        newnode = Node(value)
        current = self.head
        if index < 0 or index > self.length-1:
            return None
        if not current:
            self.head = newnode 
            self.tail = newnode 
        if self.length == 1:
            self.head.next = newnode 
            newnode.prev = self.head 
            self.tail = newnode 
        else:
            if index == 0:
                newnode.next = self.head 
                self.head.prev = newnode 
                self.head = newnode
            else:
                for _ in range(index-1):
                    current = current.next 
                newnode.next = current.next
                newnode.prev = current.next.prev
                current.next.prev = newnode 
                current.next = newnode 
        self.length += 1

    def get(self, index): # Returns node at index in linked list
        current = self.head
        if index < 0 or index > self.length-1:
            return None
        if not current:
            return None
        else:
            for _ in range (index):
                current = current.next 
        return current 

    def set_value(self, index, value): # Modifies node at given index with value in linked list
        current = self.get(index)
        if not current:
            return None 
        else:
            current.value = value 

    def remove(self, index): # Removes node with given index
        current = self.head
        if index < 0 or index > self.length-1:
            return None
        if not current:
            return None
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            if index == 0:
                self.head = self.head.next 
                self.head.prev = None 
                current.next = None 
            else:
                for _ in range(index):
                    temp = current
                    current = current.next
                if current == self.tail:
                    temp.next = None 
                    current.temp = None 
                    self.tail = temp 
                else:
                    temp.next = current.next 
                    current.next.prev = temp 
                    current.next = None
                    current.prev = None 
        self.length -= 1

    def pop_first(self): # Deletes first node or head node from linked list
        current = self.head
        popped_node = current
        if not current:
            return None
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            self.head = self.head.next 
            self.head.prev = None 
            current.next = None 
        self.length -= 1 
        return popped_node

    def pop(self): # Deletes last node from linked list
        current = self.head
        popped_node = current
        if not current:
            return None
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            while current.next:
                temp = current
                current = current.next 
            popped_node = current 
            temp.next = None 
            current.prev = None 
            self.tail = temp 
        self.length -= 1
        return popped_node


## Sample test inputs

dll = DoublyLinkedList()
dll.append(5)
dll.append(10)
dll.append(15)
dll.append(20)
dll.append(25)
print(dll)

# dll.reverse_traversal()

# dll.traversal()
# print(dll.pop_first().value)
# print(dll)
# dll.remove(0)
# print(dll)
# dll.set_value(4, 30)
# print(dll)

# print(dll.get(4).value)
# dll.prepend(2)
# print(dll)
# dll.insert(0, 1)
# print(dll)










































