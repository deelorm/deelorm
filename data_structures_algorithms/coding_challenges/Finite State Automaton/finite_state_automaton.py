# String matching with finite state automaton match and compute transition function

import time

def compute_transition_function(pattern, input):
   
    pattern = list(pattern)
    pattern.insert(0, -1)
    pattern_length = len(pattern)

    q = 0
    trans_dict = {}
    for q in range(pattern_length):
        trans_dict[q] = dict()
        for item in input:

            k = min(pattern_length, q+2)
            if q == 0:
                interm_state = item
            else:
                interm_state = ''.join(pattern[1:q+1]) + str(item)

            while k > pattern_length:
                k -= 1
            
            lenk = k

            for _ in range(lenk):
                flag = 0
                if len(pattern[1:k+1]) == 1:
                    if ''.join(pattern[1:k+1]) == interm_state[-1]:
                        trans_dict[q][item] = k
                    else:
                        trans_dict[q][item] = 0
                    flag = 1
                else:
                    interm_match_length = len(interm_state) - k
                    if ''.join(pattern[1:k+1]) == interm_state[interm_match_length:]:
                        trans_dict[q][item] = k
                        flag = 1
                k -= 1
                if flag:
                    break
    return trans_dict 


def finite_state_automaton(text, transition_function, pattern_length):
    text = list(text)
    text.insert(0, -1)
    text_length = len(text)
    pattern_match = []
    q = 0 
    for i in range(1, text_length): 
        q = transition_function[q][text[i]]
        if q == pattern_length:
            pattern_match.append('Pattern occurs at shift index {}'.format(i - pattern_length - 1))
    return pattern_match

if __name__ == '__main__':
    file_path = '.\\'
    file_path1 = '.\\'

    pattern_match = {}
    pattern_list = ['ACT', 'CGT', 'GAT']

    start_time = time.time_ns()

    with open(file_path, 'r+') as fh:
        text_file = fh.readlines()
        input_text = ''.join(text_file)
        input_text = list(set(input_text))
        
        for pattern in pattern_list:
            trans_func = compute_transition_function(pattern, input_text)
            pattern_match[pattern] = finite_state_automaton(''.join(text_file), trans_func, len(pattern))
    

    for i in pattern_list:
        file_path = file_path1 + '\\' + i +'_FSA.txt'
        with open(file_path, 'w') as fh:
            for line in pattern_match[i]:
                fh.write(line)
                fh.write('\n')

    finish_time = time.time_ns()
    print(finish_time - start_time)

