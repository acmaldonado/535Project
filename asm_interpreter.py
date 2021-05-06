import sys
import os
from memory.main import *

STATUS_SYMB = {
    'eq': 0,
    'neq': 1,
    'gt': 2,
    'lt': 3,
    'ge': 4,
    'le': 5,
    'ovf': 6,
    'ze': 7,
    'sgn': 8,
    'udf': 9,
    'nan': 10,
    'dnm': 11,
    'inf': 12,
    'msn': 13,
    'esn': 14
}

if os.name == 'Windows':
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\assembler'
    path_denom = '\\'
else:
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/assembler'
    path_denom = '/'

def proccess_text_asm(file):

    with open(dir_path + path_denom + file, 'r') as asmf:
        lines = asmf.readlines()

    tags = {}
    counter = 0

    new_lines = []

    for line in lines:
        if '//' in line or line.strip() == '':
            continue
        elif ':' in line:
            tokens = line.split(':')
            tags[tokens[0]] = counter
            continue
        else:
            new_lines.append(line.rstrip())
            counter+=1
    print(new_lines, tags)

    return new_lines, tags

def interpret_asm_line(line, tags):
    tokens = line.lower().split(' ')

    print(tokens)

    if tokens[0] == 'mov':
        if len(tokens) < 3:
            raise Exception(f"Invalid command \'{line}\'")

        instr_type = '000'
        instr_opcode = '0000'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '019b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2]}\'")
            else:
                value = format(value, '019b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2]}\'")

        signal = '0'
        if len(tokens) > 3:
            if tokens[3] == '1' or tokens[3] == 'true':
                signal = '1'
        
        command = instr_type + immediate + instr_opcode + signal + destination + value
        return command

    elif tokens[0] == 'ldr':
        if len(tokens) < 3:
            raise Exception(f"Invalid command \'{line}\'")

        instr_type = '011'
        instr_opcode = '000'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '016b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2]}\'")
            else:
                value = format(value, '016b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2]}\'")

        command = instr_type + immediate + instr_opcode + destination + value + '00000'
        return command
        
    elif tokens[0] == 'str':
        if len(tokens) < 3:
            raise Exception(f"Invalid command \'{line}\'")

        instr_type = '011'
        instr_opcode = '001'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '016b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2]}\'")
            else:
                value = format(value, '016b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2]}\'")

        command = instr_type + immediate + instr_opcode + destination + value + '00000'
        return command
        
    elif tokens[0] == 'add':
        if len(tokens) < 4:
            raise Exception(f"Invalid command \'{line}\'")
        
        instr_type = '000'
        instr_opcode = '0001'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        operand1 = int(tokens[1][1:])
        if operand1 > 11:
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        else:
            operand1 = format(operand1, '04b')

        if tokens[2][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        destination = int(tokens[2][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[3][0] == '#':
            value = format(int(tokens[3][1:]), '015b')
            immediate = '1'
            
        elif tokens[3][0] == 'r':
            value = int(tokens[3][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[3]}\'")
            else:
                value = format(value, '015b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[3]}\'")

        signal = '0'
        if len(tokens) > 4:
            if tokens[4] == '1' or tokens[4] == 'true':
                signal = '1'

        command = instr_type + immediate + instr_opcode + signal + operand1 + destination + value
        return command

    elif tokens[0] == 'mul':
        if len(tokens) < 4:
            raise Exception(f"Invalid command \'{line}\'")
        
        instr_type = '000'
        instr_opcode = '0111'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        operand1 = int(tokens[1][1:])
        if operand1 > 11:
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        else:
            operand1 = format(operand1, '04b')

        if tokens[2][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        destination = int(tokens[2][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[3][0] == '#':
            value = format(int(tokens[3][1:]), '015b')
            immediate = '1'
            
        elif tokens[3][0] == 'r':
            value = int(tokens[3][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[3]}\'")
            else:
                value = format(value, '015b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[3]}\'")

        signal = '0'
        if len(tokens) > 4:
            if tokens[4] == '1' or tokens[4] == 'true':
                signal = '1'

        command = instr_type + immediate + instr_opcode + signal + operand1 + destination + value
        return command


    elif tokens[0] == 'cmp':
        if len(tokens) < 3:
            raise Exception(f"Invalid command \'{line}\'")

        instr_type = '000'
        instr_opcode = '1001'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        operand1 = int(tokens[1][1:])
        if operand1 > 11:
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        else:
            operand1 = format(operand1, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '019b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2]}\'")
            else:
                value = format(value, '019b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2]}\'")

        signal = '0'
        if len(tokens) > 3:
            if tokens[3] == '1' or tokens[3] == 'true':
                signal = '1'
        
        command = instr_type + immediate + instr_opcode + signal + operand1 + value
        return command

    elif tokens[0] == 'bc':
        if len(tokens) < 4:
            raise Exception(f"Invalid command \'{line}\'")
        
        instr_type = '100'
        instr_opcode = '010'

        if tokens[1][0] != '#':
            raise Exception(f"Invalid addressing mode \'{tokens[1]}\'")
        mode = int(tokens[1][1:])
        if mode > 3:
            raise Exception(f"Invalid addressing mode \'{tokens[1]}\'")
        mode = format(mode, '02b')

        if tokens[2][0] == '#':
            status = int(tokens[2][1:])
        elif tokens[2] in STATUS_SYMB:
            status = STATUS_SYMB[tokens[2]]
        else:
            raise Exception(f"Invalid status bit \'{tokens[2]}\'")
        if status > 31:
            raise Exception(f"Invalid addressing mode \'{tokens[2]}\'")
        status = format(status, '05b')

        if tokens[3][0] == '#' or tokens[3][0] == 'r':
            address = format(int(tokens[3][1:]), '019b')
        elif tokens[3] in tags:
            address = format(int(tags[tokens[3]]), '019b')
        else:
            raise Exception(f"Invalid address \'{tokens[3]}\'")

        command = instr_type + instr_opcode + mode + status + address
        return command

    elif tokens[0] == 'ldrv':
        if len(tokens) < 3:
            raise Exception(f'Invalid Command \'{line}\'')

        instr_type = '011'
        instr_opcode = '010'

        if tokens[1][0] != 'r':
            raise Exception(f'Invalid register address \'{tokens[1]}\'')
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '016b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2]}\'")
            else:
                value = format(value, '016b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2]}\'")
        
        if len(tokens) > 3:
            if tokens[3][0] != '#':
                raise Exception(f'Invalid offset \'{tokens[3]}\'')
            offset = format(int(tokens[3][1:]), '06b')
        else:
            offset = '000000'

        command = instr_type + instr_opcode + destination + value + offset
        return command

    elif tokens[0] == 'strv':
        if len(tokens) < 3:
            raise Exception(f'Invalid Command \'{line}\'')

        instr_type = '011'
        instr_opcode = '011'

        if tokens[1][0] != 'r':
            raise Exception(f'Invalid register address \'{tokens[1]}\'')
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '016b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2]}\'")
            else:
                value = format(value, '016b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2]}\'")
        
        if len(tokens) > 3:
            if tokens[3][0] != '#':
                raise Exception(f'Invalid offset \'{tokens[3]}\'')
            offset = format(int(tokens[3][1:]), '06b')
        else:
            offset = '000000'

        command = instr_type + instr_opcode + destination + value + offset
        return command

    elif tokens[0] == 'vmul':
        if len(tokens) < 4:
            raise Exception(f"Invalid command \'{line}\'")
        
        instr_type = '001'
        instr_opcode = '100'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        operand1 = int(tokens[1][1:])
        if operand1 > 11:
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        else:
            operand1 = format(operand1, '04b')

        if tokens[2][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        destination = int(tokens[2][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[3][0] == '#':
            value = format(int(tokens[3][1:]), '017b')
            immediate = '1'
            
        elif tokens[3][0] == 'r':
            value = int(tokens[3][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[3]}\'")
            else:
                value = format(value, '017b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[3]}\'")

        command = instr_type + immediate + instr_opcode + operand1 + destination + value
        return command

    elif tokens[0] == 'ftov':
        if len(tokens) < 4:
            raise Exception(f"Invalid command \'{line}\'")

        instr_type = '101'
        instr_opcode = '00'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        operand1 = int(tokens[1][1:])
        if operand1 > 3:
            raise Exception(f"Invalid operand register \'{tokens[1]}\'")
        else:
            operand1 = format(operand1, '02b')

        if tokens[2][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        destination = int(tokens[2][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[2]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[3][0] == '#':
            value = format(int(tokens[3][1:]), '016b')
            immediate = '1'
        elif tokens[3][0] == 'r':
            value = int(tokens[3][1:])
            if value > 11:
                raise Exception(f"Invalid destination register \'{tokens[3]}\'")
            value = format(value, '016b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[3]}\'")

        command = instr_type + immediate + instr_opcode + operand1 + destination + value + '0000'
        return command
        


    elif tokens[0] == 'end':
        return '11111111111111111111111111111111'

    else:
        return "unknown command"

def translate_asm_to_bin(asm_file, bin_file):
    
    lines, tags = proccess_text_asm(asm_file)

    with open(dir_path + path_denom + bin_file, 'w') as binf:
        count = 0
        for line in lines:
                binf.write(f'{count} {int(interpret_asm_line(line, tags), 2)}\n')
                count+=1
    
def generate_memory_from_bin(bin_file):
    memory_system = Memory(16, {"layers":2,"sizes":[8,16]})

    if os.name == 'Windows':
        path_denom = '\\'
    else:
        path_denom = '/'


    with open(dir_path + path_denom + bin_file, 'r') as binf:
        lines = binf.readlines()
    
    for line in lines:
        inp = line.split(' ')
        result = None
        while result != CycleStatus.DONE:
            result = memory_system.store(int(inp[0]), int(inp[1]))

    parsed_bin = bin_file[:len(bin_file)-4] + '.json'

    with open(dir_path + path_denom + parsed_bin, 'w') as pbinf:
        pbinf.write(jsonpickle.encode(memory_system))

def asm_to_memory(asm_file, bin_file):
    translate_asm_to_bin(asm_file, bin_file)
    generate_memory_from_bin(bin_file)
    
def load_memory_with_array(memfile, arrayfile, startaddress):
    with open(dir_path + path_denom + memfile, 'r') as memf:
        memory = jsonpickle.decode(memf.read())

    counter = startaddress

    with open(dir_path + path_denom + arrayfile, 'r') as arrayf:
        lines = arrayf.readlines()

    for line in lines:
        result = None
        while result != CycleStatus.DONE:
            result = memory.store(counter, int(line))
        counter += 1

    with open(dir_path + path_denom + memfile, 'w') as memf:
        memf.write(jsonpickle.encode(memory))

if __name__ == '__main__':
    if sys.argv[1] == 'int':
        asm_to_memory(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'arr':
        load_memory_with_array(sys.argv[2], sys.argv[3], int(sys.argv[4]))


        
