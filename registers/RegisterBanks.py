from registers.Registers import GeneralRegister, FloatRegister, VectorRegister

class RegisterBank:

    def set_read_num(self, num: int) -> None:
        '''Sets the multiplexer to read from the register with number 'num' when read is called'''
        pass

    def read(self) -> int:
        '''Reads data from the specified register'''
        pass

    def set_write_num(self, num: int) -> None:
        '''Sets the multiplexer to write to the register with number 'num' when write is called'''
        pass

    def write(self) -> int:
        '''Writes data from the specified register'''
        pass


class GeneralRegisterBank(RegisterBank):

    def __init__(self, size):
        self.registers = [GeneralRegister() for i in range(size)]
        self.size = size
        self.write_register = 0
        self.read_register = 0

    def set_read_num(self, num: int) -> None:
        if num >= 0 and num < self.size:
            self.read_register = num

    def read(self) -> int:
        return self.registers[self.read_register]

    def set_and_read(self, num: int) -> int:
        self.set_read_num(num)
        return self.read()

    def set_write_num(self, num: int) -> None:
        if num >= 0 and num < self.size:
            self.write_register = num

    def write(self, data: int) -> None:
        self.registers[self.write_register] = data

    def set_and_write(self, num: int, data: int) -> None:
        self.set_write_num(num)
        self.write(data)

    def __str__(self):
        pass


class FloatRegisterBank(RegisterBank):

    def __init__(self, size):
        self.registers = [FloatRegister() for i in range(size)]
        self.size = size
        self.write_register = 0
        self.read_register = 0

    def set_read_num(self, num: int) -> None:
        if num >= 0 and num < self.size:
            self.read_register = num

    def read(self) -> int:
        return self.registers[self.read_register]

    def set_and_read(self, num: int) -> int:
        self.set_read_num(num)
        return self.read()

    def set_write_num(self, num: int) -> None:
        if num >= 0 and num < self.size:
            self.write_register = num

    def write(self, data: int) -> None:
        self.registers[self.write_register] = data

    def set_and_write(self, num: int, data: int) -> None:
        self.set_write_num(num)
        self.write(data)


class VectorRegisterBank(RegisterBank):

    def __init__(self, size):
        self.registers = [VectorRegister() for i in range(size)]
        self.size = size
        self.write_register = 0
        self.read_register = 0

    def set_read_num(self, num: int) -> None:
        if num >= 0 and num < self.size:
            self.read_register = num

    def read(self) -> int:
        return self.registers[self.read_register]

    def set_and_read(self, num: int) -> int:
        self.set_read_num(num)
        return self.read()

    def set_write_num(self, num: int) -> None:
        if num >= 0 and num < self.size:
            self.write_register = num

    def write(self, data: int) -> None:
        self.registers[self.write_register] = data

    def set_and_write(self, num: int, data: int) -> None:
        self.set_write_num(num)
        self.write(data)