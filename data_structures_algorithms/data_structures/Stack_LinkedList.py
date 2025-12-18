# Task --  Create stack data structue using linked list with no size limitation and has the following functions: is_empty(), pop(), push(), peek(), delete()

class Node:
    '''
Creates node for linked list
    '''

    # Initializes node with default data
    def __init__(self, data=None):
        self.data = data
        self.next = None 

    # Returns node data
    def __str__(self):
        return str(self.data)


class LinkedList:
    '''
Creates linked list class
    '''

    # Initializes linked list
    def __init__(self):
        self.head = None 
        self.tail = None 

    # Returns an iterator object for linked list
    def __iter__(self):
        current =  self.head 
        while current:
            yield current 
            current = current.next


class Stack(object):
    '''
Creates stack data structue using linked list, no size limitation, and has the following functions: is_empty(), pop(), push(), peek(), delete()
    '''
    # Initializes stack list
    def __init__(self):
        self.linkedlist = LinkedList() 
        
    # Return stack elements when print function is called
    def __str__(self):
        return '\n'.join([str(i) for i in self.linkedlist])

    # Returns True if stack is empty, otherwise False
    def is_empty(self): 
        if self.linkedlist.head is None:
            True
        else:
            False 

    # Removes and returns element on top of stack if not empty
    def pop(self):
        if self.linkedlist.head is None:
            print('There is no element in stack')
        else:
            popped_node = self.linkedlist.head
            if self.linkedlist.head.next is None:
                self.linkedlist.head = None 
                self.linkedlist.tail = None 
            else:
                self.linkedlist.head = self.linkedlist.head.next
                return popped_node
    
    # Adds element to top of stack
    def push(self, data):
        newnode = Node(data) 
        if self.linkedlist.head is None: 
            self.linkedlist.head = newnode 
            self.linkedlist.tail = newnode
            print('Element has been successfully added!')
        else:
            newnode.next = self.linkedlist.head 
            self.linkedlist.head = newnode 
            print('Element has been successfully added!')
    
    # Returns element on top of stack
    def peek(self):
        if self.linkedlist is None:
                print('There is no element in stack')
        else:
            return self.linkedlist.head 
    
    # Deletes stack
    def delete(self):
        self.linkedlist.head = None 
        self.linkedlist.tail = None


## Sample test inputs

customStack = Stack()

print(customStack.is_empty())

customStack.push(10)
customStack.push(20)
customStack.push(30)
customStack.push(40)

print(customStack)

print('----------------')
print(customStack.pop())
print('----------------')
print(customStack)
print(customStack.peek())

customStack.delete()
print(customStack)
