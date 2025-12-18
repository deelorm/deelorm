# Deadlock Detector which can allocate, deallocate resources on need basis and detect deadlock prior to allocation and/or after deallocation of resources 


import random as rd, re, logging, os

# Initializes log config and creates output log file in run directory
logger = logging.getLogger(__name__)
logging.basicConfig(filename='output.txt', filemode='w', encoding='utf-8', level=logging.DEBUG)

class Process:
    '''
*********************************************************************************************************************
Process Class creates process instance and maintains a list of all processes
*********************************************************************************************************************
Global Instances
## rand_seed - seed number to generate process numbers and auto-increments (in 10000 folds) if existing processes exceeds limit
## proc_count - maintains count of existing processes, intial value set to 10000 
## identifier_list - list of all existing processes stored in dict() object 
    '''
    identifier_list = dict()
    proc_count = 0
    rand_seed = 10000

    # Initializes proc_identifier object instance
    def __init__(self):
        self.proc_identifier = 0
        self.alloc = None 
    
    # Creates new process (unique number), process number and assigns it to the identifier list
    def set_identifier(self, proc_num):
        while True:
            Process.proc_count += 1
            if Process.proc_count == 10000:
                Process.rand_seed += 10000
            self.proc_identifier = rd.randint(0, self.rand_seed)
            if self.proc_identifier not in Process.identifier_list:
                Process.identifier_list[self.proc_identifier] = proc_num
                break

    # Calls set_identifer function and returns process unique number
    def add_proc(self, proc_num):
        self.set_identifier(proc_num)
        return self.proc_identifier


class Resource:
    '''
*********************************************************************************************************************
Resource Class creates resource instance and maintains a list of all resources
*********************************************************************************************************************
Global Instances
## rand_seed - seed number to generate resource identifiers and auto-increments (in 10000 folds) if existing resources exceeds limit
## rec_count - maintains count of existing resources, intial value set to 20000
## identifier_list - list of all existing resources stored in dict() object 
    '''
    identifier_list = dict()
    rec_count = 0
    rand_seed = 20000

    # Initializes rec_identifier object instance
    def __init__(self):
        self.rec_identifier = 0
        self.alloc = None 

    # Creates new resource (unique number), resource number and assigns it to the identifier list
    def set_identifier(self, rec_num):
        while True:
            Resource.rec_count += 1
            if Resource.rec_count == 20000:
                Resource.rand_seed += 10000
            
            rec_alnum = ''
            for _ in range(4):
                rec_alnum += chr(rd.randint(0, Resource.rand_seed % 100000))
            self.rec_identifier = rec_alnum + str(rec_num)

            if self.rec_identifier not in Resource.identifier_list:
                Resource.identifier_list[self.rec_identifier] = rec_num
                break

    # Calls set_identifer function and returns resource unique number
    def add_rec(self, rec_num):
        self.set_identifier(rec_num)
        return self.rec_identifier


class RAG(object):
    '''
*********************************************************************************************************************************
RAG Class contains allocate, proc_num_gen, rec_num_gen, proc_alloc_gen deallocate, recproc_tabgen, procrec_tabgen, cyclic_detect
*********************************************************************************************************************************
Object Instances
## rec_proc - maintains resouce -> proocess dict() pairs used for allocation and deallocation of  resources and processes
## proc_rec - maintains processe -> resource dict() pairs used for allocation and deallocation of  resources and processes
## alloc_bit - integer bit to track allocation of resource to processes 
## proc -- instance of Process class
## rec -- instance of Resource class
    '''


    # Initializes instance variables
    def __init__(self):
        self.rec_proc = {}
        self.proc_rec = {}
        self.alloc_bit = 0
        self.proc = Process()
        self.rec = Resource()
    

    # Allocates resources and processes 
    def allocate(self, proc_num, rec_num):
        current_proc = ''
        current_rec = ''

        for item in self.rec.identifier_list.items():    # Checks to see if resource exists in list
            if item[1] == rec_num:
                current_rec = item[0]
        if not current_rec:                              # Creates new resource if it is not an existant resource 
            current_rec = self.rec.add_rec(rec_num)

        for item in self.proc.identifier_list.items():   # Checks to see if process exists in list
            if item[1] == proc_num:
                current_proc = item[0]
        if not current_proc:                             # Creates new process if it is not an existant process
            current_proc = self.proc.add_proc(proc_num)

        if current_rec not in self.rec_proc:             # Creates new entry in rec_proc dict() if current resouce is a new resource and allocates
            self.rec_proc[current_rec] = list()
            self.rec_proc[current_rec].append(str(current_proc) + 'token')
            logger.info(f' Process {proc_num} needs resource {rec_num} - Resource {rec_num} is allocated to process {proc_num}.')

        else:
            for item in self.rec_proc[current_rec]:      # Adds entry for process in rec_proc dict()
                token_str = list(item[:-6:-1])
                token_str.reverse()
                if ''.join(token_str) == 'token':
                    self.alloc_bit = 1
                    break 
            if self.alloc_bit:                          # Checks and adds (resource, process) pair to proc_rec dict()
                self.rec_proc[current_rec].append(str(current_proc))
                logger.info(f' Process {proc_num} needs resource {rec_num} - Process {proc_num} must wait.')
            else:
                self.rec_proc[current_rec].append(str(current_proc) + 'token')  
        
        if current_proc not in self.proc_rec:            # Checks and adds (process, resource) pair to proc_rec dict()
            self.proc_rec[current_proc] = list()
        self.proc_rec[current_proc].append(str(current_rec) )

    # Returns unique process number
    def proc_num_gen(self, proc_num):
        for item in self.proc.identifier_list.items():
            if item[1] == proc_num:
                return item[0]


    # Returns unique resource number
    def rec_num_gen(self, rec_num):
        for item in self.rec.identifier_list.items():
            if item[1] == rec_num:
                return item[0]
    

    # Returns next process to be allocated a resource instance using process unique number 
    def proc_alloc_gen(self, rec):
        current_allot_proc = None
        
        if len(self.rec_proc[rec]) > 1:
            for proc in self.rec_proc[rec]:
                if proc.isdigit():
                    current_allot_proc = proc
                    break
            current_allot_proc = self.rec_proc[rec][1]
        return current_allot_proc
            # for item in self.rec_proc[rec]:
            #     if item.isdigit():
            #         if item < current_allot_proc:
            #             current_allot_proc = item

    
    # Deallocates resource and process from rec_proc, proc_rec, resource and process identifier lists 
    def deallocate(self, proc_num, rec_num):

        dealloc_proc = self.proc_num_gen(proc_num)                  # Assigns process deallocation number 
        dealloc_rec = self.rec_num_gen(rec_num)                     # Assigns resource deallocation number

        if self.rec_proc[dealloc_rec] == []:                        # Checks existance of (resource, process) entry in rec_proc dict() pair
                del self.rec_proc[dealloc_rec]
        else:
            for item in self.rec_proc[dealloc_rec]:                 # Iterates through rec_proc dict() entries for deallocate resource for dealloc process and assigns resource to next process
                dealloc_item = str(dealloc_proc) + 'token'
                if item == dealloc_item:
                    token_str = list(item[:-6:-1])
                    token_str.reverse()
                    if ''.join(token_str) == 'token':
                        next_proc = self.proc_alloc_gen(dealloc_rec) # Retrieves next process for allocation of resource
                        if next_proc is not None:
                            proc_index = self.rec_proc[dealloc_rec].index(next_proc)
                            self.rec_proc[dealloc_rec][proc_index] = next_proc + 'token' # Assigns resouce to next process                   
                            self.rec_proc[dealloc_rec].remove(dealloc_item)  # Deallocates and removes process from rec_proc dict()

                            next_proc_num = self.proc.identifier_list[int(next_proc)]
                            logger.info(f' Process {proc_num} releases resource {rec_num} - Resource {rec_num} is allocated to process {next_proc_num}.')
                    
                        else:
                            logger.info(f' Process {proc_num} releases resource {rec_num} - Resource {rec_num} is now free.')
                            #if self.rec_proc[dealloc_rec] == []:             # Removes entry from rec_proc and resource identifier list
                            del self.rec_proc[dealloc_rec]
                            del self.rec.identifier_list[dealloc_rec]
                        
        if self.proc_rec[dealloc_proc] == []:                        # Removes entry from proc_rec and process identifier list
                del self.proc_rec[dealloc_proc]
        else:
            for item in self.proc_rec[dealloc_proc]:
                if item is dealloc_rec:
                    self.proc_rec[dealloc_proc].remove(dealloc_rec)
                    if self.proc_rec[dealloc_proc] == []:           
                        del self.proc_rec[dealloc_proc]
                        del self.proc.identifier_list[dealloc_proc]

    
    # Creates (resource, process) lookup entries for deadlock detection
    def recproc_tabgen(self):
        rec_proc_tab = {}
        rec_match_tk = re.compile(r'^\d+[a-z]+')
        rec_match = re.compile(r'\d+')
        for item, value in self.rec_proc.items():
            for rec in value:
                if rec_match_tk.match(rec):
                    if item not in  rec_proc_tab:
                        rec_proc_tab[item] = []
                    rec_proc_tab[item].append(rec_match.match(rec).group(0))

        return rec_proc_tab


    # Creates (process, resource) lookup entries for deadlock detection
    def procrec_tabgen(self):
        proc_rec_tab = {}
        recproc_tab = self.recproc_tabgen()
        for item, value in self.proc_rec.items():
            for proc in value:
                if proc in recproc_tab and str(item) == ''.join(recproc_tab[proc]):
                    pass
                else:
                    if item not in proc_rec_tab:
                        proc_rec_tab[str(item)] = []                   
                    proc_rec_tab[str(item)].append(proc)
        return proc_rec_tab
    

    # Detects cycles in resouce allocation graph using recproc_tabgen, procrec_tabgen lookup entries
    def cyclic_detect(self, proc_tab, rec_tab, item, cyclic_list):
        # print('proc', proc_tab)
        # print('rec', rec_tab)
        # print('item', item)
        # print('cyclic_list', cyclic_list)
        # print('--------------------------------------')
        if item.isdigit() and item not in proc_tab and item not in cyclic_list:
            cyclic_list = []
            return cyclic_list

        if not item.isdigit() and item not in rec_tab and item not in cyclic_list:
            cyclic_list = []
            return cyclic_list

        if item.isdigit():                                      # Checks if current node is a process
            if item in proc_tab:
                popped_proc_item = proc_tab[item].pop()
                if len(proc_tab[item]) == 0:
                    del proc_tab[item]
                if popped_proc_item not in cyclic_list:
                    cyclic_list.append(popped_proc_item)
                else:
                    cyclic_list.append(popped_proc_item)
                    return cyclic_list
                return self.cyclic_detect(proc_tab, rec_tab, popped_proc_item, cyclic_list)
        else:                                                   # if current node is a resource
            if item in rec_tab:
                popped_rec_item = rec_tab[item].pop()
                if len(rec_tab[item]) == 0:
                    del rec_tab[item]
                if popped_rec_item not in cyclic_list:
                    cyclic_list.append(popped_rec_item)
                else:
                    cyclic_list.append(popped_rec_item)
                    return cyclic_list
                return self.cyclic_detect(proc_tab, rec_tab, popped_rec_item, cyclic_list)
        return cyclic_list                                    
        

    # Checks for cycles for each node in resource allocation graph using cyclic_detect function         
    def cyclic_checker(self):
        # logger.info('Cyclic checker')
        node_list = [str(item) for item in self.proc.identifier_list]
        for item in self.rec.identifier_list:                    # Creates list of all processes and resources 
            node_list.append(item)

        for node_item in node_list:                              # Checks for deadlock for each process or resource item
            init_node = node_item
            cyclic_list = [node_item]
            cyclic_result = self.cyclic_detect(self.procrec_tabgen(), self.recproc_tabgen(), node_item, cyclic_list)        # Calls cyclic detect function
            result_count = [cyclic_list.count(item) for item in cyclic_list]
            result_cond = False
            for num in result_count:                             # Checks deadlock condition in cyclic result from cyclic_detect function call
                if num > 1:
                    result_cond = True
            if result_cond:
                proc_list = []
                rec_list = []
                for item in set(cyclic_result):
                    if item.isdigit():
                        proc_list.append(str(self.proc.identifier_list[int(item)]))
                    else:
                        rec_list.append(str(self.rec.identifier_list[item]))

                logger.info(' DEADLOCK DETECTED: Process(es) {} and Resource(s) {} are found in a cycle'.format(', '.join(proc_list), ','.join((rec_list))))
                break
        logger.info(' EXECUTION COMPLETED: No deadlock encountered')

if __name__ == '__main__':

    work_dir = os.getcwd()
    log_header = f'''
**************************************************************************************************************************
RESOURCE ALLOCATION GRAPH (RAG) with DEADLOCK OR CYCLIC DETECTOR 
File name: output.txt
File type: Log file
File path: {work_dir}\output.txt
**************************************************************************************************************************
                 '''
    logger.info(log_header)

    input_filepath = ".\\input0.txt"
    with open(input_filepath, 'r+') as fh:
        input_file = fh.readlines()

    rag = RAG()                             # Initializes RAG class
    logger.info('Init deadlock check.')
    rag.cyclic_checker()                    # Cyclic check prior to reading input file
    logger.info('-'*110)
    
    for line in input_file:
        line = line[:5]
        line = ''.join(line)
        # print(line)
        proc, request_type, rec = line.split(' ')
        if request_type == 'N':
            rag.allocate(int(proc), int(rec))
        if request_type == 'R':
            rag.deallocate(int(proc), int(rec))


    rag.cyclic_checker()                     # Cyclic check after user inputs
    logger.info('-'*110)

    print('       ')
    print('*******')
    print('Exit 0 ')
    print('*******')














