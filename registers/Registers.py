from enum import Enum
import struct

class Register:

    class Type(Enum):
        GEN = 0
        FLOAT = 1
        VECT = 2

    def write(self, data) -> None:
        '''Writes data into the register'''
        pass

    def read(self):
        '''Reads data stored in the register'''
        pass

class GeneralRegister(Register):

    def __init__(self):
        self.data = 0
        self.type = Register.Type.GEN

    def write(self, data: int) -> None:
        self.data = data

    def read(self) -> int:
        return self.data

class FloatRegister(Register):

    def __init__(self):
        self.data = 0
        self.type = Register.Type.FLOAT
    
    def write(self, data: int) -> None:
        self.data = data
    
    def read(self) -> int:
        return self.data

class VectorRegister(Register):
    def __init__(self):
        self.data = 0
        self.type = Register.Type.GEN

    def write(self, data: int) -> None:
        self.data = data

    def read(self) -> int:
        return self.data