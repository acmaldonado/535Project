import struct
from enum import Enum
from memory.main import CycleTimer
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

class InstructionStatus(Enum):
    WAIT = -1
    DONE = 1

class DecodeClass: 

    
    def decode(self, instr: int):
        instruction = {
            'execute': {},
            'memory': {},
            'writeback': {},
            'squashed': False,
            'result': None
        }

        type_code = instr & 0b111
        
        # Data type_code
        if type_code == 0b000:

            opcode = instr >> 4 & 0b1111

            # MOV
            if opcode == 0b0000:
                instruction['execute'] = {}
                instruction['memory'] = {}
                instruction['writeback'] = {
                    'code': 'MOV',
                    'Rd': instr >> 9 & 0b1111,
                    'immediate': instr >> 3 & 1,
                    'set_status': instr >> 8 & 1,
                    'operand': instr >> 14 & 0b111111111111111111,
                    'timer': CycleTimer(1)
                }
                '''
                code = 'MOV'
                Rd = instr >> 9 & 0b1111
                immediate = instr >> 3 & 1
                set_status = instr >> 8 & 1
                operand = instr >> 14 & 0b111111111111111111
                '''

            # CMP
            if opcode == 0b1001:
                instruction['execute'] = {
                    'code': 'CMP',
                    'immediate': instr >> 3 & 1,
                    'set_status': instr >> 8 & 1,
                    'operand': instr >> 13 & 0b1111111111111111111,
                    'timer': CycleTimer(1)
                }
                instruction['memory'] = {
                    'code': 'CMP',
                    'Rn': instr >> 9 & 0b1111,
                    'timer': CycleTimer(1)
                }
                instruction['writeback'] = {}
                '''
                code = 'CMP'
                Rn = instr >> 9 & 0b1111
                immediate = instr >> 3 & 1
                set_status = instr >> 8 & 1
                operand = instr >> 13 & 0b1111111111111111111
                '''

            # SHT
            if opcode == 0b1000:
                instruction['execute'] = {
                    'code': 'SHT',
                    'immediate': instr >> 3 & 1,
                    'set_status': instr >> 8 & 1,
                    'Rd': instr >> 13 & 0b1111,
                    'operand': instr >> 18 & 0b11111111111111,
                    'timer': CycleTimer(1)
                }
                instruction['memory'] = {
                    'code': 'SHT',
                    'Rn': instr >> 9 & 0b1111,
                    'addressing': instr >> 17 & 1,
                    'timer': CycleTimer(1)
                }
                instruction['writeback'] = {
                    'code': 'SHT',
                    'Rn': instr >> 9 & 0b1111,
                    'timer': CycleTimer(1)
                }
                '''
                code = 'SHT'
                Rn = instr >> 9 & 0b1111
                Rd = instr >> 13 & 0b1111
                immediate = instr >> 3 & 1
                set_status = instr >> 8 & 1
                addressing = instr >> 17 & 1
                operand = instr >> 18 & 0b11111111111111
                '''
            
            # LGC
            if opcode == 0b1010:
                instruction['execute'] = {
                    'code': 'LGC',
                    'immediate': instr >> 3 & 1,
                    'set_status': instr >> 8 & 1,
                    'Rd': instr >> 13 & 0b1111,
                    'shift': instr >> 17 & 0b11,
                    'operand': instr >> 19 & 0b1111111111111,
                    'timer': CycleTimer(1)
                }
                instruction['memory'] = {
                    'code': 'LGC',
                    'Rn': instr >> 9 & 0b1111,
                    'timer': CycleTimer(1)
                }
                instruction['writeback'] = {
                    'code': 'LGC',
                    'Rn': instr >> 9 & 0b1111,
                    'timer': CycleTimer(1)
                }
                '''
                code = 'LGC'
                Rn = instr >> 9 & 0b1111
                Rd = instr >> 13 & 0b1111
                immediate = instr >> 3 & 1
                set_status = instr >> 8 & 1
                shift = instr >> 17 & 0b11
                operand = instr >> 19 & 0b1111111111111
                '''
            
            # Any other opcode format 
            else:
                # ADD
                if opcode == 0b0001:
                    instruction['execute'] = {
                    'code': 'ADD',
                    'immediate': instr >> 3 & 1,
                    'set_status': instr >> 8 & 1,
                    'Rd': instr >> 13 & 0b1111,
                    'operand': instr >> 17 & 0b111111111111111,
                    'timer': CycleTimer(1)
                    }
                    instruction['memory'] = {
                        'code': 'ADD',
                        'Rn': instr >> 9 & 0b1111,
                        'timer': CycleTimer(1)
                    }
                    instruction['writeback'] = {
                        'code': 'ADD',
                        'Rn': instr >> 9 & 0b1111,
                        'timer': CycleTimer(1)
                    }
                    '''
                    code = 'ADD'
                    Rn = instr >> 9 & 0b1111
                    Rd = instr >> 13 & 0b1111
                    immediate = instr >> 3 & 1
                    set_status = instr >> 8 & 1
                    operand = instr >> 17 & 0b111111111111111
                    '''
                # Missing opcodes

        # Vector type_code    
        if type_code == 0b001:
            pass

        # Float type_code    
        if type_code == 0b010:
            pass

        # Load/Store type_code
        if type_code == 0b011:
            
            opcode = instr >> 4 & 0b1111

            # LDR
            if opcode == 0b000:
                instruction['execute'] = {}
                instruction['memory'] = {
                    'code': 'LDR',
                    'Rd': instr >> 7 & 0b1111,
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
                Rd = bin(instr >> 7 & 0b1111)
                immediate = instr >> 3 & 1
                operand = bin(instr >> 11 & 0b1111111111111111)
                offset = bin(instr >> 27 & 0b11111)
                '''

            # STR
            if opcode == 0b001:
                instruction['execute'] = {}
                instruction['memory'] = {
                    'code': 'LDR',
                    'Rn': bin(instr >> 7 & 0b1111),
                    'immediate': instr >> 3 & 1,
                    'operand': bin(instr >> 11 & 0b1111111111111111),
                    'offset': bin(instr >> 27 & 0b11111),
                    'timer': CycleTimer(1)
                }
                instruction['writeback'] = {
                    'code': 'LDR',
                    'Rn': bin(instr >> 7 & 0b1111),
                    'timer': CycleTimer(1)
                }
                '''
                code = 'STR'
                Rn = bin(instr >> 7 & 0b1111)
                immediate = instr >> 3 & 1
                operand = bin(instr >> 11 & 0b1111111111111111)
                offset = bin(instr >> 27 & 0b11111)
                '''

        # Branch type_code
        if type_code == 0b100:

            opcode = bin(instr >> 4 & 0b1111)

            # BC
            if opcode == 0b010:
                instruction['execute'] = {}
                instruction['memory'] = {
                    'code': 'BC',
                    'addressing': bin(instr >> 6 & 0b11),
                    'operand1': bin(instr >> 8 & 0b11111),
                    'operand2': bin(instr >> 13 & 0b1111111111111111111),
                    'timer': CycleTimer(1)
                }
                instruction['writeback'] = {
                    'code': 'BC',
                    'Rn': bin(instr >> 7 & 0b1111),
                    'timer': CycleTimer(1)
                }
                '''
                code = 'BC'
                addressing = bin(instr >> 6 & 0b11)
                operand1 = bin(instr >> 8 & 0b11111)
                operand2 = bin(instr >> 13 & 0b1111111111111111111)
                '''

        else:
            print("Invalid type code")

        return (CycleStatus.DONE, instruction)    


class Execute:
    
    def execute(self, instruction: dict, CORE):
        if instruction == None:
            return None

        if instruction['execute']['code'].check_on() == WAIT:
            return (CycleStatus.WAIT, instruction)

        if instruction['execute'] == {}:
            return (CycleStatus.DONE, instruction)
        
        # ADD
        if instruction['execute']['code'] == 'ADD':
            # value at register 1
            val1 = CORE.GRegisters.read(instruction['execute'].Rn)
            # If it is immediate
            if instruction['execute']['immediate'] == 1:
                val2 = instruction['execute']['operand']
            # If it is register direct
            if instruction['execute']['immediate'] == 0:
                val2 = CORE.GRegisters.read(bin(instruction['execute'].operand >> 27 & 0b1111))
            else:
                raise Exception("Wrong addressing mode")

            instruction['result'] = GeneralALU.add(instruction, val1, val2)

        # CMP
        if instruction['execute'].code == 'CMP':
            # value at register 1
            val1 = CORE.GRegisters.read(instruction['execute'].Rn)
            # If it is immediate
            if instruction['execute'].immediate == 0:
                val2 = instruction['execute'].operand
            # If it is register direct
            if instruction['execute'].immediate == 1:
                val2 = CORE.GRegisters.read(bin(instruction['execute'].operand >> 27 & 0b1111))
            else:
                raise Exception("Wrong addressing mode")

            instruction['result'] = GeneralALU.comp(instruction, val1, val2)
            
        return (CycleStatus.DONE, instruction)

class Memory:
    pass

class Write_Back:

    def write_back(self, instruction: dict, CORE):
        if instruction == None:
            return None

        if instruction['writeback'].timer.check_on() == WAIT:
            return (CycleStatus.WAIT, instruction)

        if instruction['writeback'] == {}:
            return (CycleStatus.DONE, instruction)

        # MOV
        if instruction['writeback'].code == 'MOV':
            if instruction['writeback'].immediate == 0:
                val = instruction['writeback'].operand
            # If it is register direct
            if instruction['writeback'].immediate == 1:
                val = CORE.GRegisters.read(bin(instruction['writeback'].operand >> 27 & 0b1111))
            else:
                raise Exception("Wrong addressing mode")

            CORE.GRegisters.set_and_write(instruction['writeback'].Rd, val)

        # ADD
        if instruction['writeback'].code == 'ADD':
            CORE.GRegisters.set_and_write(instruction['writeback'].Rd, instruction['result'])

        # LDR
        if instruction['writeback'].code == 'LDR':
            CORE.GRegisters.set_and_write(instruction['writeback'].Rd, instruction['result'])

        # STR
        if instruction['writeback'].code == 'STR':

        # BC
        if instruction['writeback'].code == 'BC':

        return (CycleStatus.DONE, instruction)


        '''
        TODO:
        * Change GeneralRegisters to CORE
        * Change Dictionary references to []
        * FUCKING DELETE BINS
        * Finish
        '''
