import struct

def float_to_bin(num):
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]


class GeneralALU:

    def add(self, val1: int, val2: int) -> int:
        return val1 + val2

    def sub(self, val1: int, val2: int) -> int:
        return val1 - val2
    
    def rsub(self, val1: int, val2: int) -> int:
        return self.sub(val2, val1)

    def mod(self, val1: int, val2: int) -> int:
        return val1 % val2
    
    def div(self, val1: int, val2: int) -> int:
        return val1 // val2
    
    def mul(self, val1: int, val2: int) -> int:
        return val1 * val2

    def sht(self, a: bool, val1: int, val2: int) -> int:
        if a:
            val = val1
            for i in range(val2):
                val = val // 10
            return val
        else:
            return val1 >> val2

    def comp(self, val1: int, val2: int) -> int:
        sub = val1 - val2
        if sub > 0:
            return 1
        elif sub < 0:
            return -1
        else:
            return 0
    
    def lgc(self, l: int, val1: int, val2: int) -> int:
        if l == 0:
            return ~val1
        elif l == 1:
            return ~(val1 & val2)
        elif l == 2:
            return val1 & val2
        else:
            return val1 | val2

class FloatALU:

    def fadd(self, val1: int, val2: int) -> int:
        fval1 = bin_to_float(val1)
        fval2 = bin_to_float(val2)
        return float_to_bin(fval1 + fval2)

    def fsub(self, val1: int, val2: int) -> int:
        fval1 = bin_to_float(val1)
        fval2 = bin_to_float(val2)
        return float_to_bin(fval1 - fval2)
    
    def frsub(self, val1: int, val2: int) -> int:
        return self.fsub(val2, val1)

    def fmod(self, val1: int, val2: int) -> int:
        fval1 = bin_to_float(val1)
        fval2 = bin_to_float(val2)
        return float_to_bin(fval1 % fval2)
    
    def fdiv(self, val1: int, val2: int) -> int:
        fval1 = bin_to_float(val1)
        fval2 = bin_to_float(val2)
        return float_to_bin(fval1 / fval2)
    
    def fmul(self, val1: int, val2: int) -> int:
        fval1 = bin_to_float(val1)
        fval2 = bin_to_float(val2)
        return float_to_bin(fval1 * fval2)

    def fcomp(self, val1: int, val2: int) -> int:
        fval1 = bin_to_float(val1)
        fval2 = bin_to_float(val2)
        sub = fval1 - fval2
        if sub > 0:
            return 1
        elif sub < 0:
            return -1
        else:
            return 0

class VectorALU:

    def convert_binv_to_fltv(self, val: list):
        fval = []
        for v in val:
            fval.append(bin_to_float(v))
        return fval

    def vadd(self, val1: list, val2: list) -> list:
        fval1 = self.convert_binv_to_fltv(val1)

        fval2 = self.convert_binv_to_fltv(val2)

        rval = []
        for i in range(len(fval1)):
            rval.append(float_to_bin(fval1[i] + fval2[i]))
        return rval

    def vsub(self, val1: list, val2: list) -> list:
        fval1 = self.convert_binv_to_fltv(val1)

        fval2 = self.convert_binv_to_fltv(val2)

        rval = []
        for i in range(len(fval1)):
            rval.append(float_to_bin(fval1[i] - fval2[i]))
        return rval