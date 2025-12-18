

def num_paths_2d_arr_min(arr, row, col, cost):
    if cost < 0:
        return 0
    if row == 0 and col == 0:
        if arr[row][col] - cost == 0:
            return 1 
        else:
            return 0
    if row == 0:
        return num_paths_2d_arr_min(arr, 0, col-1, cost - arr[row][col])
    if col == 0:
        return num_paths_2d_arr_min(arr, row-1, 0, cost - arr[row][col])
    op1 = num_paths_2d_arr_min(arr, row-1, col, cost - arr[row][col])
    op2 = num_paths_2d_arr_min(arr, row, col-1, cost - arr[row][col])
    return op1+op2

arr1 = [[4,7,1,6],
        [5,7,3,9],
        [3,2,1,2],
        [7,1,6,3]
        ]

print(num_paths_2d_arr_min(arr1, 3, 3, 25))





