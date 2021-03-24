from registers import RegisterBanks, Registers
from alus import ALU
from memory import main
from pipeline import Pipeline

class Core:

    def __init__(self, sizeg, sizef, sizev, memsize, caches):
        self.GALU = ALU.GeneralALU()
        self.FALU = ALU.FloatALU()
        self.VALU = ALU.VectorALU()

        self.pc = Registers.GeneralRegister()
        self.status = Registers.GeneralRegister()
        self.lr = Registers.GeneralRegister()
        self.ret = Registers.GeneralRegister()

        self.GRegisters = RegisterBanks.GeneralRegisterBank(sizeg)
        self.FRegisters = RegisterBanks.FloatRegisterBank(sizef)
        self.VRegisters = RegisterBanks.VectorRegisterBank(sizev)

        self.memory = main.Memory(memsize, caches)

        self.pipeline = Pipeline.Pipeline(self.memory)

        self.cycles = 0

    def run_cycles(self, num_cycles):
        for i in range(num_cycles):
            self.pipeline.run_cycle(self.pc.data, self)
            self.pc.write(self.pc.read + 1)
            cycles += 1

    def memory_array():
        return ['Cache level 0', 'Cache level 1', 'RAM']

    def register_array():
        return [f'Register {i}' for i in range(32)]

    def interpret_command(self, command):
        return command

if __name__ == '__main__':
    main_core = Core(12, 4, 12, 16, {"layers":2,"sizes":[16,64]})