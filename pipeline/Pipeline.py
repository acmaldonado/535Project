from enum import Enum

class FetchStage:

    def __init__(self, memory):
        self.memory = memory
        self.instruction = None
        self.enabled = True
        self.fetch_flag = True
    
    def fetch_cycle(self, pc):
        if not self.enabled and ~self.fetch_flag:
            return None

        curr_instruction = self.instruction
        self.instruction = self.memory.query(pc)
        if not self.enabled:
            self.fetch_flag = False
        return curr_instruction

    def toggle_enabled(self):
        self.enabled = not self.enabled

    def raise_fetch_flag(self):
        self.fetch_flag = True

class DecodeStage:

    def __init__(self, fetch):
        self.fetch = fetch
        self.decoded = None

    def decode_cycle(self, pc, core):
        instruction = self.fetch.fetch_cycle(pc)
        curr_decoded = self.decoded

        #decode here

        return curr_decoded
        

class ExecuteStage:

    def __init__(self, decode):
        self.decode = decode
        self.executed = None

    def execute_cycle(self, pc, core):
        curr_executed = self.executed
        self.executed = self.decode.decode_cycle(pc, core)
        #execute here
        return curr_executed

class MemoryStage:

    def __init__(self, execute):
        self.execute = execute
        self.memorized = None

    def memory_cycle(self, pc, core):
        curr_memorized = self.memorized
        self.memorized = self.execute.execute_cycle(pc, core)
        #access memory here
        return curr_memorized

class WritebackStage:

    def __init__(self, memory, fetch):
        self.memory = memory
        self.fetch = fetch
        self.written = None
        self.enabled = True

    def writeback_cycle(self, pc, core):
        curr_written = self.written
        self.written = self.memory.memory_cycle(pc, core)
        #writeback here
        if not self.enabled:
            self.fetch.raise_fetch_flag()
        return curr_written

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
        self.wstage.writeback_cycle(pc, core)

    def toggle_pipeline(self):
        self.fstage.toggle_enabled()
        self.wstage.toggle_enabled()