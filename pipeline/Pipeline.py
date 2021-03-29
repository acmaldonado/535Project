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
    

    def fetch_cycle(self, status, pc, core):
        print(f'fetching cycle instr: {self.instruction}, enabled: {self.enabled}, fetch_flag: {self.fetch_flag}, ended: {self.ended}, stat: {status}, pc: {pc.read()}')

        if not self.enabled and not self.fetch_flag:
            return CycleStatus.WAIT, None

        if self.ended:
            return CycleStatus.WAIT, None

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
            return CycleStatus.WAIT, None 

        curr_instruction = self.instruction
        self.instruction = core.memory.query(pc.read())
        if self.instruction[0] != CycleStatus.WAIT:
            pc.write(pc.read() + 1)
            if self.instruction[1] == 4294967295:
                self.ended = True

        if not self.enabled:
            self.fetch_flag = False
        return CycleStatus.WAIT, curr_instruction[1]

    def toggle_enabled(self):
        self.enabled = not self.enabled

    def raise_fetch_flag(self):
        self.fetch_flag = True

    def squash(self):
        if instruction is not None:
            instruction = None

class DecodeStage:

    def __init__(self, fetch):
        self.fetch = fetch
        self.decoded = None

    def decode_cycle(self, status, pc, core):
        if self.decoded is None:
            self.decoded = self.fetch.fetch_cycle(CycleStatus.DONE, pc, core)
            return None

        if self.decoded[0] == CycleStatus.DONE and status == CycleStatus.WAIT:
            self.fetch.fetch_cycle(CycleStatus.WAIT, pc, core)
            return None

        print(f"passing {self.decoded} to decode")

        self.decoded = decode(self.decoded[1])

        if self.decoded[0] == CycleStatus.WAIT or status == CycleStatus.WAIT:
            self.fetch.fetch_cycle(CycleStatus.WAIT, pc, core)
            return None
        else:
            decoded_to_return = CycleStatus.WAIT, self.decoded[1]
            self.decoded = self.fetch.fetch_cycle(CycleStatus.DONE, pc, core)
            return decoded_to_return
    
    def squash(self):
        if self.decoded is not None:
            self.decoded = None
        

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

        if self.written is not None and self.written[0] == CycleStatus.WAIT:
            self.memory.memory_cycle(CycleStatus.WAIT, pc, core, pipe)
        else:
            if not self.enabled:
                self.fetch.raise_fetch_flag()
            written_to_return = self.written
            self.written = self.memory.memory_cycle(CycleStatus.DONE, pc, core, pipe)
            return written_to_return

    def toggle_enabled(self):
        self.enabled = not self.enabled

class Pipeline:

    def __init__(self, memory):
        self.fstage = FetchStage(memory)
        self.dstage = DecodeStage(self.fstage)
        self.estage = ExecuteStage(self.dstage)
        self.mstage = MemoryStage(self.estage)
        self.wstage = WritebackStage(self.mstage, self.fstage)

    def run_cycle(self, pc, core):
        self.wstage.writeback_cycle(pc, core, self)

    def toggle_pipeline(self):
        self.fstage.toggle_enabled()
        self.wstage.toggle_enabled()

    def squash(self):
        self.fstage.squash()
        self.dstage.squash()
        self.estage.squash()