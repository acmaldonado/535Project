from registers.RegisterBanks import GeneralRegisterBank, FloatRegisterBank, VectorRegisterBank
from registers.Registers import GeneralRegister
from alus.ALU import GeneralALU, FloatALU, VectorALU
from memory.main import *
from pipeline.Pipeline import Pipeline
from gui import GUI
import jsonpickle
import json
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

class Core:

    def __init__(self, sizeg, sizef, sizev, memsize, caches):
        self.GALU = GeneralALU()
        self.FALU = FloatALU()
        self.VALU = VectorALU()

        self.pc = GeneralRegister()
        self.status = GeneralRegister()
        self.lr = GeneralRegister()
        self.ret = GeneralRegister()

        self.GRegisters = GeneralRegisterBank(sizeg)
        self.FRegisters = FloatRegisterBank(sizef)
        self.VRegisters = VectorRegisterBank(sizev)

        self.memory = Memory(memsize, caches)

        self.pipeline = Pipeline(self.memory, self)

        self.cycles = 0

    def run_cycles(self, num_cycles):
        for i in range(num_cycles):
            self.pipeline.run_cycle(self.pc, self)
            self.cycles += 1

    def memory_array(self):
        return [*enumerate([str(x) for x in self.memory.caches]), ('RAM', str(self.memory.main_memory))]

    def register_array(self):
        def reg_bank_labels(type, bank):
            return [f'{type} Register {i}' for i in range(len(bank.registers))]
        titles = ('PC', 'Status', 'LR', 'RET', *reg_bank_labels('General', self.GRegisters), *reg_bank_labels('Float', self.FRegisters), *reg_bank_labels('Vector', self.GRegisters))
        regs = [str(x) for x in [self.pc, self.status.bin(), self.lr, self.ret, *self.GRegisters.registers, *[f'Hex: {x.hex()}\nFloat: {x}' for x in self.FRegisters.registers], *[f'Hex: {x.hex()}\nFloats: {x}' for x in self.VRegisters.registers]]]
        # print('TITLE LENGTH', len(titles))
        # print('REGS LENGTH', len(regs))
        return zip(titles, regs)

    def interpret_command(self, command):
        inp = command.lower().split(' ')

        cmd = inp[0]
        adr_size = None
        adr = None

        return_string =  ""

        if len(inp) == 2:
            if cmd == 'create_empty_memory':
                adr_size = int(inp[1])
            elif cmd in ['read', 'write']:
                adr = int(inp[1])

        if cmd == 'create_empty_memory':
            return_string +=  f'Creating empty memory with {inp[1]} bit address space ...\n'
            self.memory = Memory(int(inp[1]), json.loads(inp[2]))
            return_string +=  'Done!\n'

        if cmd == 'load_memory_from_json':
            return_string +=  f'Loading memory snapshot from json at {inp[1]} ...\n'
            with open(dir_path + '\\' + inp[1], 'r') as f:
                self.memory = jsonpickle.decode(f.read())
            return_string +=  'Done!\n'
            
        if cmd == 'dump_memory_to_json':
            return_string +=  f'Dumping memory snapshot to json at {inp[1]} ...\n'
            with open(dir_path + '\\' + inp[1], 'w') as f:
                f.write(jsonpickle.encode(self.memory))
            return_string +=  'Done!\n'

        if cmd == 'write':
            if not self.memory:
                return_string +=  'No memory system loaded\n'
                return return_string
            return_string +=  f'Writing {inp[2]} to memory at location {inp[1]} ...\n'
            result = None
            count = -1
            while result != CycleStatus.DONE:
                result = self.memory.store(int(inp[1]), int(inp[2]))
                # return_string +=  f'Waited cycle, result is {result}'
                count += 1
            return_string +=  f'Done! Waited {count} cycle{"s" if count != 1 else ""}!\n'
            
        if cmd == 'read':
            if not self.memory:
                return_string +=  'No memory system loaded\n'
                return return_string
            result = None, None
            count = -1
            while result[0] != CycleStatus.DONE:
                result = self.memory.query(int(inp[1]))
                #return_string +=  f'Waited cycle, result is {result}\n'
                count +=1   
            return_string +=  f'The value at {int(inp[1])} was read to be {result[1]}! Waited {count} cycles!\n'

        if cmd == 'view':
            if not self.memory:
                return_string +=  'No memory system loaded\n'
                return return_string

            if len(inp) < 2:
                # View entire memory system
                return_string +=  "Viewing entire memory\n"
                return_string +=  str(self.memory)
                
            else:
                level = int(inp[1])

                if len(inp) < 3:
                    # If the level of cache you're checking is the RAM (last cache line)
                    if level < 0: 
                        return_string +=  'Viewing RAM\n'
                        # curr_level = self.memory.caches[len(self.memory.caches) - 1]
                        # return_string +=  str(curr_level)
                        return_string +=  str(self.memory.main_memory.memory_array) + '\n'
                    # Else just print the entire line for that cache
                    else:
                        return_string +=  f'Viewing all lines for Level of Cache {inp[1]}:\n'
                        curr_level = self.memory.caches[level]
                        return_string +=  str(curr_level) + '\n'
                else: 
                    line_idx = int(inp[2])
                        # If the level of cache you're checking is the RAM (last cache line)
                    if level < 0: 
                        return_string +=  f'Viewing RAM at line {inp[2]}:\n'
                        return_string +=  str(self.memory.main_memory.memory_array[line_idx]) + '\n'
                    else:
                        return_string +=  f'Viewing Level of Cache {inp[1]} at line {inp[2]}:\n'
                        curr_level = self.memory.caches[level]
                        return_string +=  str(curr_level.memory_array[line_idx]) + '\n'


        # if cmd == 'run_to_done':
        #     return_string += 'Running current program to completion\n'
        #     self.run_until_done()
        #     return_string += f'Done after {self.cycles} cycles!\n'

        '''if cmd == 'toggle_cache':
            return_string += f'Cache now set to {self.memory.toggle_cache()}'

        if cmd == 'toggle_pipeline':
            return_string += f'Pipeline now set to {self.pipeline.toggle_enabled(not self.pipeline.enabled)}'
        '''

        if cmd == 'quit':
            exit(0)
        
        return return_string

if __name__ == '__main__':
    main_core = Core(12, 4, 12, 16, {"layers":2,"sizes":[16,64]})

    print(f'Trying to run on {os.name}')
    if os.name == 'Windows':
        if len(sys.argv) >= 2:
            with open(dir_path + '\\' + sys.argv[1], 'r') as f:
                main_core.memory = jsonpickle.decode(f.read())
    else:
        if len(sys.argv) >= 2:
            with open(dir_path + '/' + sys.argv[1], 'r') as f:
                main_core.memory = jsonpickle.decode(f.read())

    gui = GUI(main_core)
    gui.start()