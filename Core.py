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

        self.pipeline = Pipeline(self.memory)

        self.cycles = 0

    def run_cycles(self, num_cycles):
        for i in range(num_cycles):
            self.pipeline.run_cycle(self.pc, self)
            self.pc.write(self.pc.read() + 1)
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
        return command

if __name__ == '__main__':
    main_core = Core(12, 4, 12, 16, {"layers":2,"sizes":[16,64]})

    if len(sys.argv) >= 2:
        with open(dir_path + '\\' + sys.argv[1], 'r') as f:
            main_core.memory = jsonpickle.decode(f.read())

    gui = GUI(main_core)
    gui.start()