from registers.RegisterBanks import GeneralRegisterBank, FloatRegisterBank, VectorRegisterBank
from registers.Registers import GeneralRegister
from alus.ALU import GeneralALU, FloatALU, VectorALU
from memory.main import Memory
from pipeline.Pipeline import Pipeline

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

        self.pipeline = Pipeline(self.memory)

        self.cycles = 0

    def run_cycles(self, num_cycles):
        for i in range(num_cycles):
            self.pipeline.run_cycle(self.pc, self)
            self.pc.write(self.pc.read + 1)
            cycles += 1


if __name__ == '__main__':
    mainCore = Core(12, 4, 12, 16, {"layers":2,"sizes":[16,64]})