#Task -- Create a circular singly linked list with append, prepend, get, set_value, insert, remove, traversal, delete, pop_first, pop, & print functions

class Node(object):
    '''
 Node for circular singly linked list implementation
    '''
    def __init__(self, value=0):
        self.value = value 
        self.next = None 


class CSLinkedList(object):
    '''
Circular singly linked list implementation
    '''
    def __init__(self):  # Initializes linked list with head and tail set to None and length to 0
        self.head = None
        self.tail = None
        self.length = 0 

    def __str__(self): # Prints linked list or node values in linked list when using print() function 
        result = ''
        current = self.head 
        while current:
            result += str(current.value)
            current = current.next 
            if current is self.head:
                break
            result += " -> "
        return result 
    
    def append(self, value): # Adds node to the end of linked list at index = length - 1
        newnode = Node(value)
        if self.head is None:
            self.head = newnode 
            self.tail = newnode 
            newnode.next = newnode
            self.length += 1
        else:
            current = self.head  
            while current.next is not self.head:
                current = current.next 
            newnode.next = self.head 
            current.next = newnode 
            self.tail = newnode 
            self.length += 1

    def prepend(self, value): # Adds node to the beginning of the linked list at index 0
        newnode = Node(value)
        if self.head is None:
            self.head = newnode 
            self.tail = newnode 
            newnode.next = newnode
            self.length += 1 
        else:
            newnode.next = self.head 
            self.head = newnode 
            self.tail.next = newnode 
            self.length += 1

    def traversal(self): # Prints nodes in linked list
        current = self.head 
        if current is None:
            print('None')
        else:
            while current:
                print(current.value)
                current = current.next
                if current is self.head:
                    break 
    
    def insert(self, index, value): # Inserts new node before node at index
        newnode = Node(value)
        if index < 0 or index > self.length - 1:
            return None 
        if self.head == None:
            self.head = newnode 
            self.tail = newnode 
            newnode.next = newnode 
            self.length += 1 
        else:
            current = self.head 
            if index == 0:
                newnode.next = self.head 
                self.head = newnode 
                self.tail.next = newnode
                self.length += 1
            else:
                for _ in range(index):
                    prev = current 
                    current = current.next 
                newnode.next = prev.next 
                newnode.next = current 
                prev.next = newnode
                self.length += 1

    def get(self, index): # Returns node at index in linked list
        current = self.head
        if index < 0 or index > self.length - 1:
            return None
        if current is None:
            return None 
        if index == 0:
            return current 
        else:
            while current:
                for _ in range(index):
                    current = current.next 
                    if current == self.head:
                        break
                return current 

    def set_value(self, index, value): # Modifies node at given index with value in linked list
        current = self.head
        newnode = Node(value)
        if index < 0 or index > self.length - 1:
            return None
        if current is None:
            return None
        if index == 0:
            current.value = value 
        else: 
            for _ in range(index):
                current = current.next 
            current.value = value

    def remove(self, index): # Removes node with given index
        current = self.head
        popped_node = None
        if index < 0 or index > self.length - 1:
            return None 
        if current is None:
            return None
        if index == 0:
            popped_node = current.value
            self.head = self.head.next 
            self.tail.next = self.head
            current.next = None
            self.length -= 1
            return popped_node
        else:
            prev = self.head 
            for _ in range(index):
                prev = current
                current = current.next 
                if current == self.head:
                    break
            popped_node = current.value
            if current == self.tail:
                prev.next = self.head 
                self.tail = prev
                current.next = None
                self.length -= 1
                return popped_node
            prev.next = current.next 
            current.next = None
            self.length -= 1
            return popped_node 

    def delete_list(self): # Deletes all nodes in linked list 
        current = self.head
        if current == None:
            return None 
        else:
            self.head = None 
            self.tail = None 

    def pop_first(self): # Deletes first node from linked list
        current = self.head
        popped_node = current
        if not current:
            return None 
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0 
        else:
            self.head = self.head.next 
            self.tail.next = self.head 
            current.next = 0 
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
            self.length = 0
        else:
            for _ in range(self.length-2):
                current = current.next
            popped_node = current.next 
            current.next = self.head 
            self.tail.next = None 
            self.tail = current 
            self.length -= 1
        return popped_node


## Sample test inputs

csllist = CSLinkedList()
csllist.append(10)
csllist.append(20)
csllist.append(30)
csllist.append(40)
csllist.prepend(5)
print(csllist)

# print(csllist.pop().value)
# print(csllist)
# csllist.delete_list()
# print('------------------')
# print(csllist)
#csllist.insert(4,35)
#print(csllist)
#csllist.set_value(5,55)
#print(csllist)
# print(csllist.get(5).value)
# print(csllist.remove(4))
# print(csllist)






