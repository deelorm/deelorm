#  Task -- Create queue data structure using Python list with no size limitation and has the following functions: is_empty(), pop(), push(), peek(), delete()

class Queue(object):
    '''
Creates queue data structure using Python list, no size limitation, and has the following functions: is_empty(), pop(), push(), peek(), delete()
    '''

    # Initializes queue list
    def __init__(self): 
        self.list = []
    
    # Return queue elements when print function is called
    def __str__(self): 
        return ' '.join([str(i) for i in self.list])

    # Returns True if queue is empty, otherwise False
    def is_empty(self):
        if self.list == []:
            return True 
        else:
            return False 

    # Removes and returns element on top of queue if not empty
    def dequeue(self):
        if self.list == []:
            print('There is no element in queue')
        else:
            return self.list.pop(0)

    # Adds element to top of queue
    def enqueue(self, data):
        self.list.append(data)
        print('Element has been successfully added!')

    # Returns element on top of queue
    def peek(self):
        return self.list[0]

    # Deletes queue
    def delete(self):
        self.list = []


## Sample test inputs

customQueue = Queue()

customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)

# print(customQueue.is_empty())
print(customQueue)

customQueue.dequeue()
print(customQueue)
print(customQueue.peek())

customQueue.delete()
print(customQueue)

    




