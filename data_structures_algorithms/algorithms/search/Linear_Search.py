# Task -- Create Linear Search function

def linear_search(sort_list, data):
    
    for i in range(len(sort_list)):
        if data == sort_list[i]:
            return True 
    return False 


## Sample test inputs

sort_list = [2,1,4,3,6,5]
print(linear_search(sort_list, 8))



