# Creates stack data structue using Python list with maximum size and has the following functions: is_empty(), is_full(), pop(), push(), peek(), delete()
class Stack(object):
    '''
Creates stack data structue using Python list, user defined maximum size, and has the following functions: is_empty(), is_full(), pop(), push(), peek(), delete()
    '''

    # Initializes stack list
    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size 

    #  Returns stack elements when print function is called
    def __str__(self):
        return '\n'.join([str(i) for i in reversed(self.list)])

    # Returns True if stack is empty, otherwise False
    def is_empty(self):
        if self.list == []:
            return True 
        else:
            return False 
    
    # Returns True if stack is full, otherwise False
    def is_full(self):
        if len(self.list) == self.max_size:
            return True 
        else:
            return False
    
    # Removes and returns element on top of stack if not empty
    def pop(self):
        if self.list == []:
            print('There is no element is stack')
        else:
            popped_item = self.list[len(self.list) - 1]
            self.list.pop()
            return popped_item 

    # Adds element to top of stack if not full
    def push(self, data):
        if len(self.list) == self.max_size:
            print('Stack is full')
        else:
            self.list.append(data)
            print('Element has been successfully added!')

    # Returns element on top of stack
    def peek(self):
        if self.list == []:
            print('There is no element in stack')
        else:
            return self.list[len(self.list) - 1]

    # Deletes stack
    def delete(self):
        self.list = []


customStack = Stack(4)

print(customStack.is_empty())

customStack.push(10)
customStack.push(20)
customStack.push(30)
customStack.push(40)

print(customStack)
print(customStack.is_full())
print('----------------')
print(customStack.pop())
print('----------------')
print(customStack)
print(customStack.peek())
print(customStack.is_full())




