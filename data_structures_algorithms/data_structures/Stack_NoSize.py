# Task -- Create stack data structue using Python list with no size limitation and has the following functions: is_empty(), pop(), push(), peek(), delete()

class Stack:
    '''
Creates stack data structue using Python list, no size limitation, and has the following functions: is_empty(), pop(), push(), peek(), delete()
    '''

    # Initializes stack list
    def __init__(self):
        self.list = []
    
    #  Returns stack elements when print function is called
    def __str__(self):
        return '\n'.join([str(i) for i in reversed(self.list)]) 

    # Returns True if stack is empty, otherwise False
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False 
    
    # Removes and returns element on top of stack if not empty
    def pop(self):
        if self.list == []:
            print('There is no element in stack')
        else:
            popped_item = self.list[len(self.list) - 1]
            self.list.pop()
            return popped_item 

    # Adds element to top of stack
    def push(self, data):
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
#print(customStack.peek())





