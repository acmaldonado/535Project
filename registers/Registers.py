from enum import Enum
import struct

class Register:

    VECTOR_MAX_SIZE = 64

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

    def bin(self) -> str:
        return f'{self.data:#034b}'[2:]

    def hex(self) -> str:
        return f'{self.data:#010x}'

    def __str__(self):
        return self.hex()

    def __repr__(self):
        return str(self)


class FloatRegister(Register):

    def __init__(self):
        self.data = 0
        self.type = Register.Type.FLOAT
    
    def write(self, data: int) -> None:
        self.data = data
    
    def read(self) -> int:
        return self.data

    def hex(self) -> str:
        print(f'data: {self.data}, type: {type(self.data)}')
        return hex(struct.unpack('<I', struct.pack('<f', self.data))[0])

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)


class VectorRegister(Register):
    def __init__(self):
        self.data = [FloatRegister() for i in range(Register.VECTOR_MAX_SIZE)]
        self.type = Register.Type.VECT

    def write(self, data: list) -> None:
        for i in range(len(data)):
            self.data[i].write(data[i])

    def read(self) -> list:
        vals = []
        for i in range(len(self.data)):
            vals.append(self.data[i].read())
        return vals

    def hex(self) -> str:
        return ' '.join(x.hex() for x in self.data)

    def __str__(self):
        return str(' '.join(str(x) for x in self.data))

    def __repr__(self):
        return str(self)