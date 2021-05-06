from enum import Enum
from memory.main import CycleStatus
from instructions.instructions import *

class FetchStage:

    def __init__(self, memory):
        self.memory = memory
        self.instruction = CycleStatus.WAIT, None
        self.enabled = True
        self.fetch_flag = True
        self.ended = False
        #self.squashed = False

    def fetch_cycle(self, status, pc, core):
        print(f'fetching cycle instr: {self.instruction}, enabled: {self.enabled}, fetch_flag: {self.fetch_flag}, ended: {self.ended}, stat: {status}, pc: {pc.read()}')
        print()

        if not self.enabled and not self.fetch_flag:
            if self.instruction is not None and self.instruction[1] is not None:
                ins = self.instruction
                self.instruction = CycleStatus.WAIT, None
                return CycleStatus.WAIT, ins[1]
            return CycleStatus.WAIT, None

        print('fs1')

        ended = format(core.status.read(), '032b')
        if ended[31] == '1':
            self.ended = True
            return CycleStatus.WAIT, None

        print('fs2')

        '''if self.instruction is None:
            self.instruction = self.memory.query(pc)
            if self.instruction[0] == CycleStatus.WAIT:
                return CycleStatus.WAIT, None
            else:
                if self.instruction[1] == 4294967295:
                    self.ended = True
                pc.write(pc.read() + 1)
            return CycleStatus.WAIT, None'''
            
        if status == CycleStatus.WAIT:
            if self.instruction[1] is None:
                self.instruction = core.memory.query(pc.read())
                if self.instruction[0] != CycleStatus.WAIT:
                    pc.write(pc.read() + 1)
                    # if self.instruction[1] == 4294967295:
                    #     self.ended = True
            return CycleStatus.WAIT, None 

        print('fs3')

        curr_instruction = self.instruction
        self.instruction = core.memory.query(pc.read())
        if self.instruction[0] != CycleStatus.WAIT:
            pc.write(pc.read() + 1)
            # if self.instruction[1] == 4294967295:
            #     self.ended = True

            if not self.enabled and self.instruction is not None and self.instruction[1] is not None:
                print(f'flag disabled, {status}')
                self.fetch_flag = False

        '''if self.squashed:
            self.squashed = False
            return CycleStatus.WAIT, None'''
        return CycleStatus.WAIT, curr_instruction[1]

    def toggle_enabled(self, val):
        self.enabled = val
        print(f'fstage enabled: {self.enabled}')
        return self.enabled

    def raise_fetch_flag(self):
        print('flag raised')
        self.fetch_flag = True

    def squash(self):
        if self.instruction[1] is not None:
            self.instruction = CycleStatus.DONE, None
        #self.squashed = True


class DecodeStage:

    def __init__(self, fetch):
        self.fetch = fetch
        self.decoded = None
        #self.squashed = False

    def decode_cycle(self, status, pc, core):
        if self.decoded is None:
            self.decoded = self.fetch.fetch_cycle(CycleStatus.DONE, pc, core)
            return None

        if self.decoded[0] == CycleStatus.DONE and status == CycleStatus.WAIT:
            self.fetch.fetch_cycle(CycleStatus.WAIT, pc, core)
            return None

        print(f"passing {self.decoded} to decode with status {status}")

        if self.decoded[0] != CycleStatus.DONE:
            self.decoded = decode(self.decoded[1], core)

        if self.decoded[0] == CycleStatus.WAIT or status == CycleStatus.WAIT:
            self.fetch.fetch_cycle(CycleStatus.WAIT, pc, core)
            return None
        else:
            decoded_to_return = CycleStatus.WAIT, self.decoded[1]
            self.decoded = self.fetch.fetch_cycle(CycleStatus.DONE, pc, core)
            '''if self.squashed:
                self.squashed = False
                return CycleStatus.WAIT, None'''
            return decoded_to_return
    
    def squash(self):
        if self.decoded[1] is not None:
            self.decoded = CycleStatus.DONE, None
        #self.squashed = True
        

class ExecuteStage:

    def __init__(self, decode):
        self.decode = decode
        self.executed = None

    def execute_cycle(self, status, pc, core, pipe):
        if self.executed is None:
            self.executed = self.decode.decode_cycle(CycleStatus.DONE, pc, core)
            return None

        if self.executed[0] == CycleStatus.DONE and status == CycleStatus.WAIT:
            self.decode.decode_cycle(CycleStatus.WAIT, pc, core)
            return None

        print(f"passing {self.executed} to execute")

        self.executed = execute(self.executed[1], core)

        if self.executed[0] == CycleStatus.SQUASH:
            # print('SQUASH ------------------- SQUASH')
            pipe.squash()

        if self.executed[0] == CycleStatus.WAIT or status == CycleStatus.WAIT:
            self.decode.decode_cycle(CycleStatus.WAIT, pc, core)
        else:
            executed_to_return = CycleStatus.WAIT, self.executed[1]
            self.executed = self.decode.decode_cycle(CycleStatus.DONE, pc, core)
            return executed_to_return

    def squash(self):
        if self.executed is not None:
            self.executed = None

class MemoryStage:

    def __init__(self, execute):
        self.execute = execute
        self.memorized = None

    def memory_cycle(self, status, pc, core, pipe):
        if self.memorized is None:
            self.memorized = self.execute.execute_cycle(CycleStatus.DONE, pc, core, pipe)
            return None

        if (self.memorized[0] == CycleStatus.DONE or self.memorized[0] == CycleStatus.SQUASH) and status == CycleStatus.WAIT:
            self.execute.execute_cycle(CycleStatus.WAIT, pc, core, pipe)
            return None
        
        print(f"passing {self.memorized} to memory")

        self.memorized = load_store(self.memorized[1], core)

        if self.memorized[0] == CycleStatus.WAIT or status == CycleStatus.WAIT:
            self.execute.execute_cycle(CycleStatus.WAIT, pc, core, pipe)
        else:
            memorized_to_return = CycleStatus.WAIT, self.memorized[1]
            self.memorized = self.execute.execute_cycle(CycleStatus.DONE, pc, core, pipe)
            return memorized_to_return


class WritebackStage:

    def __init__(self, memory, fetch):
        self.memory = memory
        self.fetch = fetch
        self.written = None
        self.enabled = True

    def writeback_cycle(self, pc, core, pipe):
        print(f"passing {self.written} to writeback")

        if self.written is not None:
            self.written = write_back(self.written[1], core)
            print('cond1')

        print(f'SELF WRITTEN: {self.written}')

        if self.written is not None and self.written[0] == CycleStatus.WAIT:
            self.memory.memory_cycle(CycleStatus.WAIT, pc, core, pipe)
            print('cond2')

        else:
            if not self.enabled and self.written is not None and self.written[1] is not None:
                self.fetch.raise_fetch_flag()
            written_to_return = self.written
            self.written = self.memory.memory_cycle(CycleStatus.DONE, pc, core, pipe)
            print('cond3')
            return written_to_return

    def toggle_enabled(self, val):
        self.enabled = val
        print(f'wstage enabled: {self.enabled}')
        return self.enabled

class Pipeline:

    def __init__(self, memory, core):
        self.fstage = FetchStage(memory)
        self.dstage = DecodeStage(self.fstage)
        self.estage = ExecuteStage(self.dstage)
        self.mstage = MemoryStage(self.estage)
        self.wstage = WritebackStage(self.mstage, self.fstage)
        self.core = core
        self.dependency_table = []

    def run_cycle(self, pc, core):
        self.wstage.writeback_cycle(pc, core, self)

    def toggle_enabled(self, val):
        return self.fstage.toggle_enabled(val), self.wstage.toggle_enabled(val)

    def squash(self):
        self.fstage.squash()
        self.dstage.squash()
        self.core.memory.squash()
        self.fstage.raise_fetch_flag()
        # print('SQUASH WAS CALLED')
        #self.estage.squash()

    def add_dependency(self, register):
        if register not in self.dependency_table:
            self.dependency_table.append(register)
    
    def remove_dependency(self, register):
        if register in self.dependency_table:
            self.dependency_table.remove(register)
    
    def check_dependency(self, register):
        if register in self.dependency_table:
            return True
        return False