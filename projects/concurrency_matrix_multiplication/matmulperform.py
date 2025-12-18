
from multiprocessing import Process, Queue, Lock, Pool
import os
import multiprocessing as mp
import re
import time
import random
import csv
from tkinter import W

# Computes the resultant matrix of two matrixes where matrix1 is the row of matrix1 while matrix2 is fully representative of matrix2
def matrix_compute(matrix1, matrix2):
    print('.....')
    print('.....')
    temp_result = []
    for k in range(len(matrix2[0])):
        i = 0
        temp = 0
        for j in range(len(matrix2)):
            temp_imm = float(matrix1[i] * matrix2[j][k])
            temp += temp_imm
            i += 1
        temp_result.append(temp)
    print('+ COMPUTING RESULTANT MATRIX FOR ROW...')
    print('.....')
    print('+ RESULTANT FOR ROW COMPLETE....')
    return temp_result


# Selects correct mode (sequential or parallel) for matrix multiplication and calls the matrix_compute function
def matrix_mode(q, matrix1, matrix2, mode):
    result = []
    if mode == 'seq':
        print('+ MATRIX_MODE FUNCTION TRANSFERRING CONTROL TO MATRIX_COMPUTE FOR SEQUENTIAL MATRIX COMPUTATION')
        for row in matrix1:
            q.put(matrix_compute(row, matrix2))     # Assigns result to queue buffer
    else:
        print('+ MATRIX_MODE FUNCTION TRANSFERRING CONTROL TO MATRIX_COMPUTE FOR PARALLEL MATRIX COMPUTATION')
        for row in matrix1:
            q.put(matrix_compute(row, matrix2))     # Assigns result to queue buffer


# Creates/Spawns/Forks new processes off main process, calls matrix mode fuction and appends compute result to result variable
def process_alloc(q, matrix1, matrix2, mode):
    result = []
    row_count = 1
    print('.....'*15)
    p = Process(target=matrix_mode, args=(q, matrix1, matrix2, mode))       # Creates new process while calling matrix_mode function
    p.start()
    print('+ ENTERING PROCESS_ALLOC FUNCTION FOR {}'.format(p.name))
    print('+ PROCESS STARTED...')
    print('+ PROCESS ID: {}'.format(p.pid))
    print('+ PROCESS NAME: {}'.format(p.name))
    print('+ CALLING MATRIX_MODE FUNCTION...')
    if mode == 'seq':
        for num in range(len(matrix1)):
            intermediate_result = q.get()
            print('+ PROCESS {} ROW {} <--->  INTERMEDIATE RESULT'.format(p.name, row_count))        # Prints intermediate result
            print('{}'.format(intermediate_result))
            result.append(intermediate_result)      # Obtains from result to queue buffer
            row_count += 1
    else:
        for num in range(len(matrix1)):
            intermediate_result = q.get()
            print('+ PROCESS {}  ROW {} <--->  INTERMEDIATE RESULT'.format(p.name, row_count))        # Prints intermediate result
            print('{}'.format(intermediate_result))
            result.append(intermediate_result)      # Obtains from result to queue buffer
            row_count += 1
    p.join()
    print('+ EXITING PROCESS_ALLOC FUNCTION FOR {} PID {}'.format(p.name, p.pid))
    return result


# Processes each row in input matrix to remove delimiters, etc.
def file_process(line):
    list_line = []
    pattern = re.compile(r'\d+[\.]?[\d]*')
    for item in line:
        line_match = pattern.search(item.strip())
        if line_match:
            list_line.append(float(line_match.group()))
    return list_line


# Redirects result to Output file
def result_process(result):
    pattern = re.compile(r'\[(.*)\]')
    with open(output_filepath, 'w') as fh:
        for line in result:
            fh.write(pattern.match(str(line)).group(1))
            fh.write('\n')

# Generates a 50 * 50 matrix with values between -101 and 100
def matrix_gen(matrix):
    for i in range(50):
        temp = []
        for j in range(50):
            temp.append(random.randrange(-101, 101))
        matrix.append(temp)
    return matrix


# Function for __main__
def main_function(num_process=1):
    print('*'*150)
    print('*'*25, '   MATRIX MULTIPLICATION WITH PYTHON MULTIPROCESSING MODULE    ', '*'*60)
    print('*'*150)
    print('*'*150)
    print('')
    print('matrixmul program'.upper())
    print('.....'*15)
    print('+ Initializing ...')
    print('.....'''*15)

    matrix1 = []
    matrix2 = []
    input_type = 'rand'

    # num_process = int(input('Enter number of processes: '))         # Takes process input from user
    # input_type = input('Select input type (rand or file): ')        # Takes input tyoe from user either rand (random) or file (if to be read from file)

    # File paths for input and output
    input_filepath = ".\\input0.txt"
    # output_filepath = ".\\Output.txt"

    if input_type == 'file':
        with open(input_filepath, 'r+') as fh:
            input_file = fh.readlines()     # Reads input0 file
    # Processes input file
        count = 0
        for line in input_file:
            if line == '\n':
                count += 1
                continue
            if count == 0:
                print(line)
                line = line.strip().split()
                line = file_process(line)    # Processes file to remove delimiters
                matrix1.append(line)
            if count == 1:
                line = line.strip().split()
                line = file_process(line)    # Processes file to remove delimiters
                matrix2.append(line)
            if count == 2:
                break
    elif input_type == 'rand':
        matrix1 = matrix_gen(matrix1)
        matrix2 = matrix_gen(matrix2)
    resultant = []

    if len(matrix1) == 0 or len(matrix2) == 0:
        print('Matrix is not multiplable')      # Checks for elements in matrix input
        exit()
    
    if len(matrix1) < len(matrix2):
        matrix1, matrix2 = matrix2, matrix1 # Assigns matrix with maximum row as matrix1

 #   if num_process != 1:
 #       num_process = len(matrix1) # Defaults to row number of processes if process number is not 1
    
    alloc_per_process = int(len(matrix1) / num_process)     # row allocation per process
    num_process = len(matrix1) // alloc_per_process         # number of processes 
    alloc_last_process_supplus = len(matrix1) - (alloc_per_process * num_process)       # row allocation for last process or first/last process if number of process is 1 or less than 2
    # print('alloc per proc', alloc_per_process)
    # print('num proc', num_process)
    # print('alloc last proc', alloc_last_process_supplus)
    # System messages
    print('.....'''*15)
    print('+ SPAWNING PROCESSES FROM MAIN PROCESS...')
    print('+ SETTING UP SEMAPHORE/LOCK QUEUE BUFFER FOR IPC...')


    ctx = mp.get_context('spawn')
    #    ctx.set_start_method('spawn')    # Sets method for creating identical child process of its parent similar to fork
    q = ctx.Queue()     # Creates a FIFO like buffer that enables communication between processes; uses semaphores and locks to maintain consistency among threads

    # System messages
    print('.....'*15)  
   # print('+ NUMBER OF PROCESS(ES) ALLOCATED: {}'.format(num_process))
    print('+ QUEUE SETUP COMPLETE')


    # Sequential/Parallel computation if number of processes is 1 or greater than 1
    start_time = time.time()
    if num_process == 1:
        # System messages
        print('.....'*15)
        print('+ SEQUENTIAL COMPUTATION...')
        resultant = process_alloc(q, matrix1, matrix2, 'seq')
    else:
        row_num = len(matrix1)
        # System messages
        print('.....'*15)
        print('+ PARALLEL COMPUTATION...')
        process_row_count = 0
        count_row = 0                       # number of rows per process       
        process_count = 0                   # number of processes
        row_buffer = []                     # per process buffer
        row_last_process = alloc_per_process + alloc_last_process_supplus
        count_alloc_first = 0
        for row in matrix1:
            if num_process > 2:
                if process_row_count < alloc_per_process  and process_count != num_process - 1:
                    row_buffer.append(row)
                    process_row_count += 1
                    count_alloc_first = 1
                    if process_row_count != alloc_per_process:
                        continue
                elif process_row_count != row_last_process and process_count == num_process - 1:
                    row_buffer.append(row)
                    process_row_count += 1
            else:
                row_buffer.append(row)
                process_row_count += 1
            if count_alloc_first or process_row_count == row_last_process:
                result_process_alloc = process_alloc(q, row_buffer, matrix2, 'pll')

                for i in range(len(result_process_alloc)):
                    resultant.append(result_process_alloc[i])

                process_count += 1
                print('proc_count', process_count)
                process_row_count = 0
                count_alloc_first = 0
                row_buffer = []
    end_time = time.time()
    execution_time = end_time - start_time 

    # System messages
    print('.....'*15, '...')
    print('...'*12, 'STAT', '...'*12)
    print('.....'*15, '...')
    print('NUMBER OF PROCESSES: {}'.format(num_process))
    print('AVERAGE NUMBER OF ROWS ALLOCATED PER PROCESS: {}'.format( alloc_per_process))
    print('AVERAGE NUMBER OF COMPUTATIONS: {}'.format(len(matrix1)*len(matrix2[0])))
    if num_process == 1:
        print('AVERAGE NUMBER OF COMPUTATIONS PER PROCESS FOR SEQUENTIAL EXECUTION: {}'.format(len(matrix1)*len(matrix2[0])))
        print('EXECUTION TIME FOR SEQUENTIAL COMPUTE: {}s'.format(execution_time))
    else:
        avg_compute_per_process = int((alloc_per_process * len(matrix2[0])) + (row_last_process * len(matrix2[0])) / 2)
        print('AVERAGE NUMBER OF ROWS ALLOCATED FOR LAST PROCESS PROCESS: {}'.format(row_last_process))   
        print('AVERAGE NUMBER OF COMPUTATIONS PER PROCESS FOR PARALLEL EXECUTION: {}'.format(avg_compute_per_process))
        print('EXECUTION TIME FOR PARALLEL COMPUTE: {}s'.format(execution_time))
            # print('alloc per proc', alloc_per_process)
    # print('num proc', num_process)
    # print('alloc last proc', alloc_last_process_supplus)
    print('.....'*15)
    print('************************** RESULTANT MATRIX ********************************')
    print('.....'*15)


    # Displays result on standard output
    # for row in resultant:
    #     print('[', end='')
    #     for i in range(len(row)):
    #         if i == len(row) - 1:
    #             print(row[i], end='')
    #         else:
    #             print(row[i], end=', ')
    #     print(']',end='')
    #     print('')

    # # Redirects result to Output file
    # result_process(resultant)

    # System messages
    print('')
    print('*'*180)
    return execution_time



'''
**********************************************************************************************************************************************************
***********************************        Main program block    *****************************************************************************************
**********************************************************************************************************************************************************
'''
if __name__ == '__main__':
    '''
Program consist of process_alloc, matrix_mode, matrix_compute, file_process, result_process & matrix_gen functions
Input; number of processes
Optional Input; input file type, set to rand by default
    '''

    # Average Execution time runs
    row_entry_list_paral = []
    row_entry_list_seq = []
    fields = ['Number of processes (n)', 'Average Execution Time']
    for n in range(1,51):
        print('PROCESS {}'.format(n))
        num_process = n
        temp_exec = []
        for k in range(100):
            print('PROCESS {} ITERATION {}....STARTED.....'.format(n, k))
            execution_time = main_function(n)
            temp_exec.append(execution_time)
            print('PROCESS {} ITERATION {}....COMPLETED.....'.format(n, k))
        row_entry = {}
        row_entry['Number of processes (n)'] = n
        row_entry['Average Execution Time'] = sum(temp_exec)/100
        if n == 1:
            row_entry_list_seq.append(row_entry)
        else:
            row_entry_list_paral.append(row_entry)
#    print(len(row_entry_list))
    
    # Writing to paral_exe.csv
    for num in range(len(row_entry_list_paral)):
        csv_file = 'Paral_exe.csv'
        csv_path = ".\\{}".format(csv_file)
        with open(csv_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, fieldnames=fields)
            writer.writeheader()
            writer.writerows(row_entry_list_paral)

    # Writing to seq_exe.csv
    for num in range(len(row_entry_list_paral)):
        csv_file = 'Seq_exe.csv'
        csv_path = ".\\{}".format(csv_file)
        with open(csv_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, fieldnames=fields)
            writer.writeheader()
            writer.writerows(row_entry_list_seq)
    
    
    