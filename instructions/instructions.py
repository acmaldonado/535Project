import struct
from enum import Enum
from memory.main import CycleTimer
from memory.main import CycleStatus
from alus.ALU import *
from registers.RegisterBanks import *

'''
Instruction format

/////////////////////////////////////////////////////////////
type_code /// misc /// Opcode /// Register /// misc /// operand
   ###    ///  #   ///  ####  ///  ####    ///  #   ///  remaining
/////////////////////////////////////////////////////////////

Instruction type_codes:
Data: 000
Vector: 001
Float: 010
Load/Store: 011
Branch: 100
'''

  
def decode(instr: int):
    if instr is None:
        return CycleStatus.DONE, None

    instruction = {
        'execute': {},
        'memory': {},
        'writeback': {},
        'squashed': False,
        'result': None
    }

    instr = format(instr, '032b')
    print(instr)
    type_code = instr[0:3]
    
    # Data type_code
    if type_code == '000':

        opcode = instr[4:8]

        # INSTRUCTION: MOV
        if opcode == '0000':
            instruction['execute'] = {}
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'MOV',
                'Rd': instr[9:13],
                'immediate': instr[3],
                'set_status': instr[8],
                'operand': instr[13:32],
                'timer': CycleTimer(1)
            }
            '''
            code = 'MOV'
            Rd = instr >> 9 & 0b1111
            immediate = instr >> 3 & 1
                1 - Immediate addressing
                0 - Register direct
            set_status = instr >> 8 & 1
            operand = instr >> 13 & 0b111111111111111111
            '''

        # INSTRUCTION: CMP
        elif opcode == '1001':
            instruction['execute'] = {
                'code': 'CMP',
                'immediate': instr[3],
                'set_status': instr[8],
                'Rn': instr[9:13],
                'operand': instr[13:32],
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {
                'code': 'CMP',
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {}
            '''
            code = 'CMP'
            Rn = instr >> 9 & 0b1111
            immediate = instr >> 3 & 1
                1 - Immediate addressing
                0 - Register direct
            set_status = instr >> 8 & 1
            operand = instr >> 13 & 0b1111111111111111111
            '''

        # INSTRUCTION: SHT
        elif opcode == '1000':
            instruction['execute'] = {
                'code': 'SHT',
                'immediate': instr[3],
                'set_status': instr[8],
                'Rn': instr[9:13],
                'arithmethic':[17],
                'operand': instr[18:32],
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'SHT',
                'Rd': instr[13:17],
                'timer': CycleTimer(1)
            }
            '''
            code = 'SHT'
            Rn = instr >> 9 & 0b1111
            Rd = instr >> 13 & 0b1111
            immediate = instr >> 3 & 1
                1 - Immediate addressing
                0 - Register direct
            set_status = instr >> 8 & 1
            arithmetic = instr >> 17 & 1
                0 - Logical shift
                1 - Arithmetic shift
            operand = instr >> 18 & 0b11111111111111
            '''
        
        # INSTRUCTION: LGC
        elif opcode == '1010':
            instruction['execute'] = {
                'code': 'LGC',
                'immediate': instr >> 3 & 1,
                'set_status': instr >> 8 & 1,
                'Rn': instr >> 9 & 0b1111,
                'logic': instr >> 17 & 0b11,
                'operand': instr >> 19 & 0b1111111111111,
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'LGC',
                'Rd': instr >> 13 & 0b1111,
                'timer': CycleTimer(1)
            }
            '''
            code = 'LGC'
            Rn = instr >> 9 & 0b1111
            Rd = instr >> 13 & 0b1111
            immediate = instr >> 3 & 1
                1 - Immediate addressing
                0 - Register direct
            set_status = instr >> 8 & 1
            logic = instr >> 17 & 0b11
                00 - NOT
                01 - NAND
                10 - AND
                11 - OR
            operand = instr >> 19 & 0b1111111111111
            '''
        
        # Any other opcode format 
        else:
            # INSTRUCTION: ADD
            if opcode == 0b0001:
                instruction['execute'] = {
                'code': 'ADD',
                'immediate': instr >> 3 & 1,
                'set_status': instr >> 8 & 1,
                'Rn': instr >> 9 & 0b1111,
                'operand': instr >> 17 & 0b111111111111111,
                'timer': CycleTimer(1)
                }
                instruction['memory'] = {}
                instruction['writeback'] = {
                    'code': 'ADD',
                    'Rd': instr >> 13 & 0b1111,
                    'timer': CycleTimer(1)
                }
                '''
                code = 'ADD'
                Rn = instr >> 9 & 0b1111
                Rd = instr >> 13 & 0b1111
                immediate = instr >> 3 & 1
                    1 - Immediate addressing
                    0 - Register direct
                set_status = instr >> 8 & 1
                operand = instr >> 17 & 0b111111111111111
                '''
            
            # TODO: Add more ALU instructions

    # Vector type_code    
    elif type_code == 0b001:
        pass

    # Float type_code    
    elif type_code == 0b010:
        pass

    # Load/Store type_code
    elif type_code == 0b011:
        
        opcode = instr >> 4 & 0b1111

        # INSTRUCTION: LDR
        if opcode == 0b000:
            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'LDR',
                'immediate': instr >> 3 & 1,
                'operand': instr >> 11 & 0b1111111111111111,
                'offset': instr >> 27 & 0b11111,
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {
                'code': 'LDR',
                'Rd': instr >> 7 & 0b1111,
                'timer': CycleTimer(1)
            }
            '''
            code = 'LDR'
            Rd = instr >> 7 & 0b1111
            immediate = instr >> 3 & 1
                1 - Immediate addressing
                0 - Register direct
            operand = instr >> 11 & 0b1111111111111111
            offset = instr >> 27 & 0b11111
            '''

        # INSTRUCTION: STR
        elif opcode == 0b001:
            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'LDR',
                'Rn': instr >> 7 & 0b1111,
                'immediate': instr >> 3 & 1,
                'operand': instr >> 11 & 0b1111111111111111,
                'offset': instr >> 27 & 0b11111,
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {}
            '''
            code = 'STR'
            Rn = instr >> 7 & 0b1111
            immediate = instr >> 3 & 1
                1 - Immediate addressing
                0 - Register direct
            operand = instr >> 11 & 0b1111111111111111
            offset = instr >> 27 & 0b11111
            '''

    # Branch type_code
    elif type_code == 0b100:

        opcode = instr >> 4 & 0b1111


        # INSTRUCTION: BX
        if opcode == 0b001:
            instruction['execute'] = {
                'code': 'BX',
                'addressing': instr >> 6 & 0b11,
                'operand': instr >> 8 & 0b111111111111111111111111,
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {}
            '''
            code = 'BX'
            addressing = instr >> 6 & 0b11
            operand = instr >> 8 & 0b111111111111111111111111
            '''

        # INSTRUCTION: BC
        elif opcode == 0b010:
            instruction['execute'] = {
                'code': 'BC',
                'addressing': instr >> 6 & 0b11,
                'operand1': instr >> 8 & 0b11111,
                'operand2': instr >> 13 & 0b1111111111111111111,
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {}
            '''
            code = 'BC'
            addressing = instr >> 6 & 0b11
                00 - Immediate
                01 -  Register direct
                10 - Register indirect
                11 - PC + immediate
            operand1 = instr >> 8 & 0b11111
            operand2 = instr >> 13 & 0b1111111111111111111
            '''

    else:
        print("Invalid type code")
        return (CycleStatus.DONE, None)

    return (CycleStatus.DONE, instruction)    



def execute(instruction: dict, CORE):
    if instruction is None:
        return (CycleStatus.DONE, None)

    if instruction['execute'] == {}:
        return (CycleStatus.DONE, instruction)

    if instruction['execute']['timer'].check_on() == CycleStatus.WAIT:
        return (CycleStatus.WAIT, instruction)
    
    # ADD
    if instruction['execute']['code'] == 'ADD':
        # value at register 1
        val1 = CORE.GRegisters.set_and_read(instruction['execute']['Rn'])
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = instruction['execute']['operand']
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = CORE.GRegisters.set_and_read(instruction['execute']['operand'] >> 27 & 0b1111)
        else:
            raise Exception("Wrong addressing mode")

        instruction['result'] = CORE.GALU.add(val1, val2)

    # CMP
    elif instruction['execute']['code'] == 'CMP':
        # value at register 1
        val1 = CORE.GRegisters.set_and_read(instruction['execute']['Rn'])
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = instruction['execute']['operand']
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = CORE.GRegisters.set_and_read(instruction['execute']['operand'] >> 27 & 0b1111)
        else:
            raise Exception("Wrong addressing mode")

        instruction['result'] = CORE.GALU.comp(val1, val2)

    # SHT
    elif instruction['execute']['code'] == 'SHT':
        # value at register 1
        val1 = CORE.GRegisters.set_and_read(instruction['execute']['Rn'])
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = instruction['execute']['operand']
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = CORE.GRegisters.set_and_read(instruction['execute']['operand'] >> 27 & 0b1111)
        else:
            raise Exception("Wrong addressing mode")
        
        arithmethic = instruction['execute']['arithmethic']

        instruction['result'] = CORE.GALU.sht(arithmethic, val1, val2)

    # LGC
    elif instruction['execute']['code'] == 'LGC':
        # value at register 1
        val1 = CORE.GRegisters.set_and_read(instruction['execute']['Rn'])
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = instruction['execute']['operand']
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = CORE.GRegisters.set_and_read(instruction['execute']['operand'] >> 27 & 0b1111)
        else:
            raise Exception("Wrong addressing mode")

        logic = int(instruction['execute']['logic'], 2)

        instruction['result'] = CORE.GALU.lgc(logic, val1, val2)

    # BX
    elif instruction['execute']['code'] == 'BX':
        # If it is immediate
        if instruction['execute']['addressing'] == 0b00:
            address = instruction['execute']['operand']
        # If it is Register direct
        elif instruction['execute']['addressing'] == 0b01:
            address = CORE.GRegisters.set_and_read(instruction['execute']['operand'] >> 27 & 0b1111)
        # If it is Register indirect
        elif instruction['execute']['addressing'] == 0b10:
            print('lol no')
        # If it is PC + immediate
        elif instruction['execute']['addressing'] == 0b11:
            address = CORE.pc.read() + instruction['execute']['operand']
        else:
            raise Exception("Wrong addressing mode")

        instruction['squashed'] = True

        # Write into Program Counter
        CORE.pc.write(address)

    # BC
    elif instruction['execute']['code'] == 'BC':
        # Check if condition is true
        status_bit_offset = instruction['execute']['operand1']
        status = CORE.status.read()
        if status >> status_bit_offset != 1:
            return (CycleStatus.DONE, None)

        # If it is immediate
        if instruction['execute']['addressing'] == 0b00:
            address = instruction['execute']['operand2']
        # If it is Register direct
        elif instruction['execute']['addressing'] == 0b01:
            address = CORE.GRegisters.set_and_read(instruction['execute']['operand2'] >> 27 & 0b1111)
        # If it is Register indirect
        elif instruction['execute']['addressing'] == 0b10:
            print('lol no')
        # If it is PC + immediate
        elif instruction['execute']['addressing'] == 0b11:
            address = CORE.pc.read() + instruction['execute']['operand2']
        else:
            raise Exception("Wrong addressing mode")

        instruction['squashed'] = True 

        # Write into Program Counter
        CORE.pc.write(address)

    else:
        raise Exception("Invalid instruction")
        
    return (CycleStatus.DONE, instruction)


def load_store(instruction: dict, CORE):
    if instruction is None:
        return (CycleStatus.DONE, None)

    if instruction['memory'] == {}:
        return (CycleStatus.DONE, instruction)

    if instruction['memory']['timer'].check_on() == CycleStatus.WAIT:
        return (CycleStatus.WAIT, instruction)

    # STR (write)
    if instruction['memory']['code'] == 'STR':
        val = CORE.GRegisters.set_and_read(instruction['memory']['Rn'])
        # If it is immediate
        if instruction['memory']['immediate'] == 1:
            address = instruction['memory']['operand']
        # If it is register direct
        elif instruction['memory']['immediate'] == 0:
            address = CORE.GRegisters.set_and_read(instruction['memory']['operand'] >> 22 & 0b1111)
        else:
            raise Exception("Wrong addressing mode")

        # Write
        CORE.memory.store(address, val)

    # LDR (read)
    elif instruction['memory']['code'] == 'LDR':
        # If it is immediate
        if instruction['memory']['immediate'] == 1:
            address = instruction['memory']['operand']
        # If it is register direct
        elif instruction['memory']['immediate'] == 0:
            address = CORE.GRegisters.set_and_read(instruction['memory']['operand'] >> 22 & 0b1111)
        else:
            raise Exception("Wrong addressing mode")

        # Read
        instruction['result'] = CORE.memory.query(address)

    else:
        raise Exception("Invalid instruction")

    return (CycleStatus.DONE, instruction)


def write_back(instruction: dict, CORE):
    if instruction is None:
        return (CycleStatus.DONE, None)

    if instruction['writeback'] == {}:
        return (CycleStatus.DONE, instruction)

    if instruction['writeback']['timer'].check_on() == CycleStatus.WAIT:
        return (CycleStatus.WAIT, instruction)

    # MOV
    if instruction['writeback']['code'] == 'MOV':
        if instruction['writeback']['immediate'] == '1':
            val = instruction['writeback']['operand']
        # If it is register direct
        elif instruction['writeback']['immediate'] == '0':
            val = CORE.GRegisters.set_and_read(instruction['writeback']['operand'][27:32])
        else:
            raise Exception("Wrong addressing mode")

        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], val)

    # ADD
    elif instruction['writeback']['code'] == 'ADD':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])

    # SHT
    elif instruction['writeback']['code'] == 'SHT':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])

    # LGC
    elif instruction['writeback']['code'] == 'LGC':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])

    # LDR
    elif instruction['writeback']['code'] == 'LDR':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])

    return (CycleStatus.DONE, instruction)
