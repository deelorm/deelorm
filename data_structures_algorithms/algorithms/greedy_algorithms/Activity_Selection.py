
def activity_selection(tasks):
    tasks.sort(key=lambda i:i[2])
    print(tasks[0][0])
    
    for i in range(1, len(tasks)):
        if tasks[i][1] >= tasks[i-1][2]:
            print(tasks[i][0])

tasks = [['A', 2, 3],
         ['B', 5, 11],
         ['C', 1, 8],
         ['D', 0, 1],
         ['E', 8, 9]
         ]

activity_selection(tasks)