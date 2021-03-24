from enum import Enum
from math import log2, ceil
import jsonpickle
import json
import os

# read, write, show, start, stop
# Your view command should return the tag, contents, dirty, and valid bit values for a given cache line, and should just return the contents of a block in DRAM if you tell it to view that level

LINE_SIZE = 4
ADDRESS_SIZE = 16
OFFSET_SIZE = 2
dir_path = os.path.dirname(os.path.realpath(__file__))

class CycleStatus(Enum):
    WAIT = -1
    DONE = 1
    SQUASH = 2

class CycleTimer():
    
    def __init__(self, wait_time):
        self.wait_time = wait_time
        self.curr_working_address = None
        self.curr_wait_time = None
        
    def check_on(self, address):
        # print(f'Checking a timer with wait time of {self.curr_wait_time}')
        if self.curr_working_address is None:
            self.curr_wait_time = self.wait_time
            self.curr_working_address = address
            # print('self.curr_working_address was none')
            return CycleStatus.WAIT
        elif self.curr_working_address == address:
            # print('address is the same as working')
            if self.curr_wait_time <= 1:
                # print('curr_wait_time <= 1')
                return CycleStatus.DONE
            else:
                self.curr_wait_time -= 1
                # print(f'decreasing time to {self.curr_wait_time}')
                return CycleStatus.WAIT
        return CycleStatus.WAIT
    
    def reset(self):
        # print(f'resetting timer to {self.wait_time}')
        self.curr_wait_time = self.wait_time
        self.curr_working_address = None


class CacheLine():

        def __init__(self):
            self.valid = False
            self.tag = 0
            self.data = [0] * LINE_SIZE

        def __str__(self):
            return f'valid:{self.valid}, tag:{self.tag}, data:{self.data}'

        def __repr__(self):
            return f'valid:{self.valid}, tag:{self.tag}, data:{self.data}'

class CacheBlock():

    def __init__(self, num_lines, lower_cache=None):
        if (num_lines & (num_lines-1)) != 0 or num_lines == 0: # not a power of 2
            raise Exception('Please define the number of lines as a power of 2')
        self.index_bit_count = ceil(log2(num_lines))
        
        self.memory_array = [CacheLine() for i in range(num_lines)]
        self.lower_cache = lower_cache

        self.timer = CycleTimer(1)

    def __last_n_bits(self, address, n):
        # print(f'address:{address}, mask:{((1 << self.index_bit_count) - 1)}')
        return address & ((1 << self.index_bit_count) - 1)

    def __tag(self, address):
        # print(f'address:{address}, mask:{(self.index_bit_count+OFFSET_SIZE)}')
        return address >> (self.index_bit_count+OFFSET_SIZE)

    def __index(self, address):
        return self.__last_n_bits(address >> OFFSET_SIZE, self.index_bit_count)

    def __offset(self, address):
        #return self.__last_n_bits(address, OFFSET_SIZE)
        return address % LINE_SIZE

    def query(self, address):
        if self.timer.check_on(address) == CycleStatus.DONE:
            idx = self.__index(address)
            # print(f'index: {idx} arraysize: {len(self.memory_array)}')
            line = self.memory_array[idx]
            tag = self.__tag(address)

            if line.valid and tag == line.tag:
                self.timer.reset()
                return CycleStatus.DONE, line
            else: 
                ret = self.lower_cache.query(address)
                # print(f'Cache block returned:{ret}')
                status, line = ret
                if status == CycleStatus.DONE:
                    self.memory_array[idx] = line
                    self.memory_array[idx].valid = True
                    self.memory_array[idx].tag = tag
                    self.timer.reset()
                return status, line

        return CycleStatus.WAIT, None
        
    def store(self, address, data):
        if self.timer.check_on(address) == CycleStatus.DONE:
            line = self.memory_array[self.__index(address)]
            if line.valid and line.tag == self.__tag(address):
                self.memory_array[self.__index(address)].data[self.__offset(address)] = data
            
            status = self.lower_cache.store(address, data)
            if status == CycleStatus.DONE:
                self.timer.reset()
            return status
        else:
            return CycleStatus.WAIT, None

    def __str__(self):
        return str('\n'.join([ (str(i) + ': ' + str(self.memory_array[i])) for i in range(len(self.memory_array)) ]))

    def __repr__(self):
        return str(self)
        

class RAMBlock():
    def __init__(self, address_size):
        self.memory_array = [CacheLine() for i in range(2**(address_size-2))]
        self.address_size = address_size
        self.timer = CycleTimer(3)

    def query(self, address):
        if self.timer.check_on(address) == CycleStatus.DONE:
            self.timer.reset()
            ret = CycleStatus.DONE, self.memory_array[(address//LINE_SIZE)%(2**(self.address_size-OFFSET_SIZE))]
            # print(f'RAM Block returned:{ret}')
            return ret
        else:
            ret = CycleStatus.WAIT, None
            # print(f'RAM Block returned:{ret}')
            return ret

    def store(self, address, data):
        if self.timer.check_on(address) == CycleStatus.DONE:
            i = (address//LINE_SIZE)%(2**(self.address_size-OFFSET_SIZE))
            # print(f'i is {i}')
            self.memory_array[i].data[address%(2**OFFSET_SIZE)] = data
            self.timer.reset()
            return CycleStatus.DONE
        else:
            return CycleStatus.WAIT

    def __str__(self):
        return str(self.memory_array)
    
    def __repr__(self):
        return str(self.memory_array)


class Memory():
    '''args:
    address_size: size of address space in bits
    caches: dict with 'layers' being the number of layers for the cache
            and 'sizes' being a list with the same size as layers of line numbers for each layer'''
    def __init__(self, address_size, caches):
        if ('layers' not in caches) or ('sizes' not in caches) or (len(caches['sizes']) != caches['layers']):
            raise TypeError('Caches dict badly formatted') 

        self.main_memory = RAMBlock(address_size)
        self.cache_enabled = True

        self.caches = [None] * caches['layers']        
        for i in range(caches['layers']):
            tmp_cache = CacheBlock(caches['sizes'][i])
            if i != 0:
                self.caches[i-1].lower_cache = tmp_cache
            if i == caches['layers']-1:
                tmp_cache.lower_cache = self.main_memory
            self.caches[i] = tmp_cache
    
    def query(self, address):
        if self.cache_enabled:
            status, value = self.caches[0].query(address)
            # print(f'Memory query returned:{ret}')
            if status == CycleStatus.WAIT:
                return status, value
            else:
                return status, value.data[address%4]
        else:
            status, value = self.main_memory.query(address)
            # print(f'Memory query returned:{ret}')
            if status == CycleStatus.WAIT:
                return status, value
            else:
                return status, value.data[address%4]

    def store(self, address, data):
        if self.cache_enabled:
            return self.caches[0].store(address, data)
        else:
            return self.main_memory.store(address, data)

    def toggle_cache(self):
        self.cache_enabled = not self.cache_enabled
        return self.cache_enabled

    def __str__(self):
        string_mem = f'Caches:{self.caches}, Cache Enabled:{self.cache_enabled}, Main Memory:{self.main_memory}'
        return string_mem

    def __repr__(self):
        string_mem = f'Caches:{self.caches}, Cache Enabled:{self.cache_enabled}, Main Memory:{self.main_memory}'
        return string_mem

def main():
    print('Thank you for choosing AMMM shell V1.0!')
    memory_system = None

    while True:
        inp = input('> ').lower().split(' ')

        cmd = inp[0]
        adr_size = None
        adr = None

        if len(inp) == 2:
            if cmd == 'create_empty_memory':
                adr_size = int(inp[1])
            elif cmd in ['read', 'write']:
                adr = int(inp[1])

        if cmd == 'create_empty_memory':
            print(f'Creating empty memory with {inp[1]} bit address space ...')
            memory_system = Memory(int(inp[1]), json.loads(inp[2]))
            print('Done!')

        if cmd == 'load_memory_from_json':
            print(f'Loading memory snapshot from json at {inp[1]} ...')
            with open(dir_path + '\\' + inp[1], 'r') as f:
                memory_system = jsonpickle.decode(f.read())
            print('Done!')
            
        if cmd == 'dump_memory_to_json':
            print(f'Dumping memory snapshot to json at {inp[1]} ...')
            with open(dir_path + '\\' + inp[1], 'w') as f:
                f.write(jsonpickle.encode(memory_system))
            print('Done!')

        if cmd == 'write':
            if not memory_system:
                print('No memory system loaded')
                continue
            print(f'Writing {inp[2]} to memory at location {inp[1]} ...')
            result = None
            count = -1
            while result != CycleStatus.DONE:
                result = memory_system.store(int(inp[1]), int(inp[2]))
                # print(f'Waited cycle, result is {result}')
                count += 1
            print(f'Done! Waited {count} cycle{"s" if count != 1 else ""}!')
            
        if cmd == 'read':
            if not memory_system:
                print('No memory system loaded')
                continue
            result = None, None
            count = -1
            while result[0] != CycleStatus.DONE:
                result = memory_system.query(int(inp[1]))
                #print(f'Waited cycle, result is {result}')
                count +=1   
            print(f'The value at {int(inp[1])} was read to be {result[1]}! Waited {count} cycles!')

        if cmd == 'view':
            if not memory_system:
                print('No memory system loaded')
                continue

            if len(inp) < 2:
                # View entire memory system
                print("Viewing entire memory")
                print(str(memory_system))
                
            else:
                level = int(inp[1])

                if len(inp) < 3:
                    # If the level of cache you're checking is the RAM (last cache line)
                    if level < 0: 
                        print('Viewing RAM')
                        # curr_level = memory_system.caches[len(memory_system.caches) - 1]
                        # print(str(curr_level))
                        print(str(memory_system.main_memory.memory_array))
                    # Else just print the entire line for that cache
                    else:
                        print(f'Viewing all lines for Level of Cache {inp[1]}:')
                        curr_level = memory_system.caches[level]
                        print(str(curr_level))
                else: 
                    line_idx = int(inp[2])
                     # If the level of cache you're checking is the RAM (last cache line)
                    if level < 0: 
                        print(f'Viewing RAM at line {inp[2]}:')
                        print(str(memory_system.main_memory.memory_array[line_idx]))
                    else:
                        print(f'Viewing Level of Cache {inp[1]} at line {inp[2]}:')
                        curr_level = memory_system.caches[level]
                        print(str(curr_level.memory_array[line_idx]))

        if cmd == 'quit':
            exit(0)
        
        if cmd == 'toggle_cache':
            print(f'Cache now set to {memory_system.toggle_cache()}')
        '''
        COMMAND create_empty_memory(address_size, caches)

        COMMAND load_memory_from_json(filename)
        
        COMMAND dump_memory_to_json(filename)

        COMMAND write(address, data)

        COMMAND read(address)

        COMMAND view(level, line)
        '''

        print() # output

if __name__ == '__main__':
    main()

'''
Your view command should return the tag, contents, dirty, and valid bit values for a given cache line, and should just return the contents of a block in DRAM if you tell it to view that level. Think of it as your debugging probe for the simulation. 

create_empty_memory 16 {"layers":2,"sizes":[8,16]}
view 0 0
write 0 12
'''