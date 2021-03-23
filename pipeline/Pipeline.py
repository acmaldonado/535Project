from enum import Enum

class FetchStage:

    def __init__(self, memory):
        self.memory = memory
        self.instruction = None
    
    def fetch_cycle(self, pc):
        curr_instruction = self.instruction
        self.instruction = self.memory.get_instruction(pc)
        return curr_instruction

class DecodeStage:

    def __init__(self, fetch):
        self.fetch = fetch
        self.decoded = None

    def decode_cycle(self, pc):
        instruction = self.fetch.fetch_cycle(pc)
        curr_decoded = self.decoded
        #decode here
        execute = {}


        memory = {}


        writeback = {}


        self.decoded = {'squashed': False, 'execute': execute, 'memory': memory, 'writeback': writeback}

        return curr_decoded
        

class ExecuteStage:

    def __init__(self, decode):
        self.decode = decode
        self.executed = None

    def execute_cycle(self, pc):
        curr_executed = self.executed
        self.executed = self.decode.decode_cycle(pc)
        #execute here
        return curr_executed

class MemoryStage:

    def __init__(self, execute):
        self.execute = execute
        self.memorized = None

    def memory_cycle(self, pc):
        curr_memorized = self.memorized
        self.memorized = self.execute.execute_cycle(pc)
        #access memory here
        return curr_memorized

class WritebackStage:

    def __init__(self, memory):
        self.memory = memory
        self.written = None

    def writeback_cycle(self, pc):
        curr_written = self.written
        self.written = self.memory.memory_cycle(pc)
        #writeback here
        return curr_written

class Pipeline:

    def __init__(self, memory):
        self.fstage = FetchStage(memory)
        self.dstage = DecodeStage(self.fstage)
        self.estage = ExecuteStage(self.dstage)
        self.mstage = MemoryStage(self.estage)
        self.wstage = WritebackStage(self.mstage)

    def run_cycle(self, pc):
        self.wstage.writeback_cycle(pc)