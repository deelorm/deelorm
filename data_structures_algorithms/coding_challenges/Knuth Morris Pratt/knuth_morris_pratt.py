# Implementation of the knuth-morris-pratt algorithm with a compute_prefix function

import time 

def compute_prefix_function(pattern):
    pattern = list(pattern)
    pattern.insert(0, -1)
    pattern_length = len(pattern)                           
    prefix_list = [0 for i in range(pattern_length + 1)]
    prefix_list[1] = 0
    k = 0
    for n in range(2, pattern_length): # ababaca pl= 1->-1 
        while k > 0 and pattern[k+1] != pattern[n]:
            k = prefix_list[k]
        if pattern[k + 1] == pattern[n]:
            k = k + 1
        prefix_list[n] = k
    prefix_list.pop()
    prefix_list.pop(0)
    return prefix_list 


def knuth_morris_pratt(text, pattern):

    text = list(text)
    text.insert(0, -1)

    pattern_match = []
    text_length = len(text)
    

    prefix_list = compute_prefix_function(pattern)
    prefix_list = list(prefix_list)
    prefix_list.insert(0, -1)

    pattern = list(pattern)
    pattern.insert(0, -1)
    pattern_length = len(pattern)

    q = 0
    for i in range(1, text_length):  # ababaca bababacaab
        while q > 0 and pattern[q + 1] != text[i]:
            q = prefix_list[q]
        if pattern[q+1] == text[i]:
            q = q + 1 
        if q == pattern_length - 1:
            # print('Pattern match found with shift {}'.format(i - pattern_length + 1))
            pattern_match.append('Pattern match found with shift index {}'.format(i - pattern_length))
            q = prefix_list[q]
    return pattern_match


if __name__ == '__main__':
    file_path = '.\\'
    file_path1 = '.\\'

    pattern_match = {}
    pattern_list = ['ACT', 'CGT', 'GAT']

    start_time = time.time_ns()

    start_time = time.time()
    with open(file_path, 'r+') as fh:
        text_file = fh.readlines()

        for pattern in pattern_list:
            pattern_match[pattern] = knuth_morris_pratt(''.join(text_file), pattern)
    finish_time = time.time()

    for i in pattern_list:
        file_path = file_path1 + '\\' + i +'_KMP.txt'
        with open(file_path, 'w') as fh:
            for line in pattern_match[i]:
                fh.write(line)
                fh.write('\n')
    
    finish_time = time.time_ns()
    print(finish_time - start_time)
        




