from registers import RegisterBanks
from alus import ALU
from memory import main
from pipeline import Pipeline

class Core:

    def __init__(self, sizeg, sizef, sizev, memsize, caches):
        self.GALU = ALU.GeneralALU()
        self.FALU = ALU.FloatALU()
        self.VALU = ALU.VectorALU()

        self.GRegisters = RegisterBanks.GeneralRegisterBank(sizeg)
        self.FRegisters = RegisterBanks.FloatRegisterBank(sizef)
        self.VRegisters = RegisterBanks.VectorRegisterBank(sizev)

        self.Memory = main.Memory(memsize, caches)

        self.Pipeline = Pipeline.Pipeline(self.Memory)

