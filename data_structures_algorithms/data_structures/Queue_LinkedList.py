# Task --  Create queue data structure using linked list with no size limitation and has the following functions: is_empty(), pop(), push(), peek(), delete()

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
        current = self.head 
        while current:
            yield current 
            current = current.next


class Queue(object):
    '''
Creates queue data structure using linked list, no size limitation, and has the following functions: is_empty(), pop(), push(), peek(), delete()
    '''

    # Initializes queue list
    def __init__(self):
        self.linkedlist = LinkedList()
    
    # Return queue elements when print function is called
    def __str__(self):
        return ' '.join([str(i) for i in self.linkedlist])

    # Returns True if queue is empty, otherwise False
    def is_empty(self):
        if self.linkedlist.head is None:
            return True 
        else:
            return False 

    # Removes and returns element on top of queue if not empty
    def dequeue(self):
        if self.is_empty():
            print('There is no element in queue')
        else:
            popped_item = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None 
                self.linkedlist.tail = None 
            else:
                self.linkedlist.head = self.linkedlist.head.next 
    
    # Adds element to top of queue
    def enqueue(self, data):
        newnode = Node(data)
        if self.linkedlist.head == None:
            self.linkedlist.head = newnode 
            self.linkedlist.tail = newnode
        else:
            self.linkedlist.tail.next = newnode
            self.linkedlist.tail = newnode

    # Returns element on top of queue
    def peek(self):
        if self.is_empty():
            print('There is no element in queue')
        else:
            return self.linkedlist.head

    # Deletes queue
    def delete(self):
        self.linkedlist.head = None 
        self.linkedlist.tail = None


## Sample test inputs

customQueue = Queue()

print(customQueue.is_empty())

# print(customQueue)

customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)

print(customQueue)

customQueue.dequeue()
print(customQueue)

# customQueue.enqueue(50)

print(customQueue.peek())


customQueue.delete()
print(customQueue)















