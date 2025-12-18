#  Task --  Create queue data structure using Python list with size and has the following functions: is_empty(), is_full(), pop(), push(), peek(), delete()

class Queue(object):
    '''
Creates queue data structure using Python list, no size limitation, and has the following functions: is_empty(), is_full(), pop(), push(), peek(), delete()
    '''

    # Initializes queue list
    def __init__(self, max_size):
        self.list = max_size * [None]
        self.top = -1
        self.start = -1 
        self.max_size = max_size 

    # Return queue elements when print function is called
    def __str__(self):
        return ' '.join([str(i) for i in self.list])

    # Returns True if queue is empty, otherwise False
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    # Removes and returns element on top of queue if not empty
    def is_full(self):
        if self.start == 0 and self.top == self.max_size - 1:
            return True 
        elif self.start == self.top + 1:
            return True 
        else:
            return False
    
    # Removes and returns element on top of queue if not empty
    def dequeue(self):
        if self.is_empty():
            print('There is no element is queue')
        else:
            start = self.start 
            if self.start == 0:
                if self.top == 0:
                    self.start = -1 
                    self.top = -1
                else:
                    self.start += 1
            elif self.start == self.max_size - 1:
                self.start = 0 
            else:
                self.start += 1
            popped_item = self.list[start]
            self.list[start] = None 
            return popped_item 
    
    # Adds element to top of queue
    def enqueue(self, data):
        if self.is_full():
            print('Queue is full')
        else:
            if self.top == -1:
                self.top += 1
                self.start += 1
            elif self.top == self.max_size - 1:
                self.top = 0
            else:
                self.top += 1 
            self.list[self.top] = data 

    # Returns element on top of queue
    def peek(self):
        if self.is_empty():
            print('There is no element in queue')
        else:
            return self.list[self.start]

    # Deletes queue
    def delete(self):
        self.list = self.max_size * [None]


## Sample test inputs

customQueue = Queue(4)

print(customQueue.is_empty())
print(customQueue.is_full())
print(customQueue)

customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)

print(customQueue)

# print(customQueue.dequeue())
# print(customQueue)

# customQueue.enqueue(50)

print(customQueue.peek())

print(customQueue.is_full())
customQueue.delete()
print(customQueue)



    



































            












