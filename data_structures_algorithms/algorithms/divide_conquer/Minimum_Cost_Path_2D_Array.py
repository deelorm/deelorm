

def min_cost_path_2d_arr(arr, row, col):
    if row == -1 or col == -1:
        return float('inf') 
    elif row == 0 and col == 0:
        return arr[0][0]
    else:
        op1 = min_cost_path_2d_arr(arr, row-1, col)
        op2 = min_cost_path_2d_arr(arr, row, col-1)
        return arr[row][col] + min(op1, op2)

arr = [[2,4,6],
       [1,3,5],
       [5,3,2]
      ]
arr1 = [[4,7,8,6,4],
        [6,7,3,9,2],
        [3,8,1,2,4],
        [7,1,7,3,7],
        [2,9,8,9,3]
        ]


print(min_cost_path_2d_arr(arr, 2, 2))




