## ECCP model
import time, random

# Memory Model
class Memory:
    mem_data = {}

    def __init__(self):
        self.data = None
        self.address = None 

    def mem_count(self):
        count = random.randint(100000000, 10000000000)
        while count:
            count -= 1

    def write_mem(self, address, data):
        self.mem_count()
        Memory.mem_data[address] = data
        
    def read_mem(self, address):
        self.mem_count()
        return Memory.mem_data[address]

    def time_cnt(self):
        return time.time_ns()

# Cache Model
class Cache:
    cache_data = {}

    def __init__(self):
        self.cache_index = 0
        self.data = None
        self.address = None
        self.set_cache_index()

    def set_cache_index(self):
        if self.cache_index <= 2:
            self.cache_index += 1 
    
    def get_cache_index(self):
        return self.cache_index  

    def cache_count(self):
        count = random.randint(800000, 1000000)
        while count:
            count -= 1

    def write_cache(self, address, data):
        self.cache_count()
        Cache.cache_data[address] = data
        
    def read_cache(self, address):
        self.cache_count()
        return Cache.cache_data[address]

    def time_cnt(self):
        return time.time_ns()

# Processor Core Model
class Core:

    def __init__(self):
        self.core_index = 0
        self.cache = Cache()
        self.set_core_index()

    def set_core_index(self):
        if self.core_index <= 2:
            self.core_index += 1 
    
    def get_core_index(self):
        return self.core_index  

# Enclave Model
class Enclave:

    def __init__(self):
        self.enclave_index = 0
        self.core = Core()
        self.set_enclave_index()

    def set_enclave_index(self):
        if self.enclave_index <= 4:
            self.enclave_index += 1 
    
    def get_enclave_index(self):
        return self.enclave_index

    def init_core(self):
        self.core.set_core_index()
        return self.core.get_core_index()

    def init_cache(self):
        self.core.cache.set_cache_index()
        return self.core.cache.get_cache_index()

enclave = Enclave()
mem = Memory()

# print('Enclave {} intialized...'.format(enclave.get_enclave_index()))
# print('Core {} for Enclave {} intialized...'.format(enclave.core.get_core_index(), enclave.get_enclave_index()))
# print('Cache {} Core {} for Enclave {} intialized...'.format(enclave.core.cache.get_cache_index(), enclave.core.get_core_index(), enclave.get_enclave_index()))

file_path = 'C:\\Users\\denni\\OneDrive\\Desktop\\CSEN\\Fall_2024\\CSEN 5304\\Assignment\\Semester Project\\'
cache_path = file_path + 'cache.txt'
mem_path = file_path + 'mem.txt'
# with open(cache_path, 'w+') as fh:
#     for _ in range(10):
#         cache_start = enclave.core.cache.time_cnt()
#         enclave.core.cache.write_cache(5, b'0001')
#         cache_finish = enclave.core.cache.time_cnt()
#         fh.write(str(cache_finish - cache_start))
#         fh.write('\n')
for _ in range(9):
    with open(mem_path, 'a+') as fh:
        mem_start = mem.time_cnt()
        mem.write_mem(5, b'0001')
        mem_finish = mem.time_cnt()
        fh.write(str(mem_finish - mem_start))
        fh.write('\n')
    # for _ in range(10):
    #     mem_start = mem.time_cnt()
    #     mem.write_mem(5, b'0001')
    #     mem_finish = mem.time_cnt()
    #     fh.write(str(mem_finish - mem_start))
    #     fh.write('\n')

# enclave.core.set_core_index()
# print('Cache {} Core {} for Enclave {} intialized...'.format(enclave.core.cache.get_cache_index(), enclave.core.get_core_index(), enclave.get_enclave_index()))

# cache_start = enclave.core.cache.time_cnt()
# enclave.core.cache.write_cache(5, b'0001')
# cache_finish = enclave.core.cache.time_cnt()
# print(cache_finish - cache_start)


# mem = Memory()
# mem_start = mem.time_cnt()
# mem.write_mem(5, b'0001')
# mem_finish = mem.time_cnt()
# print(mem_finish - mem_start)

# cache_start = time_cnt()
# cache = Cache()
# cache.write_cache(5, b'0001')
# print(cache.read_cache(5))
# cache_finish = time_cnt()

# print('Memory latency: ', mem_finish - mem_start)
# print('Cache latency: ', cache_finish - cache_start)
