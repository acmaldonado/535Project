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

  
def decode(instr: int, CORE):
    if instr is None:
        return CycleStatus.DONE, None

    instruction = {
        'execute': {},
        'memory': {},
        'writeback': {},
        'squashed': False,
        'result': None
    }

    # INSTRUCTION: END
    instr = format(instr, '032b')
    
    if instr == '11111111111111111111111111111111':
        instruction['execute'] = {
            'code': 'END',
            'timer': CycleTimer(1)
        }
        return (CycleStatus.DONE, instruction)
    
    type_code = instr[0:3]
    
    # Data type_code
    if type_code == '000':

        opcode = instr[4:8]

        # INSTRUCTION: MOV
        if opcode == '0000':
            
            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[9:13], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
            else:
                operand = instr[13:32]


            instruction['execute'] = {}
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'MOV',
                'Rd': int(instr[9:13], 2),
                'immediate': int(instr[3], 2),
                'set_status': int(instr[8], 2),
                'operand': operand,
                'timer': CycleTimer(1)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[9:13], 2))
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

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[9:13], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
            else:
                operand = instr[13:32]

            instruction['execute'] = {
                'code': 'CMP',
                'immediate': int(instr[3], 2),
                'set_status': int(instr[8], 2),
                'Rn': CORE.GRegisters.set_and_read(int(instr[9:13], 2)),
                'operand': operand,
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {
                'code': 'CMP',
                'set_status': int(instr[8], 2),
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {}
            # Add dependencies
            CORE.pipeline.add_dependency(CORE.status)
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

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[9:13], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if CORE.pipeline.check_dependency(int(instr[13:17], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
            else:
                operand = instr[18:32]

            instruction['execute'] = {
                'code': 'SHT',
                'immediate': int(instr[3], 2),
                'set_status': int(instr[8], 2),
                'Rn': CORE.GRegisters.set_and_read(int(instr[9:13], 2)),
                'arithmethic': int(instr[17], 2),
                'operand': operand,
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'SHT',
                'Rd': int(instr[13:17], 2),
                'timer': CycleTimer(1)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[13:17], 2))
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

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[9:13], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if CORE.pipeline.check_dependency(int(instr[13:17], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
            else:
                operand = instr[19:32]

            instruction['execute'] = {
                'code': 'LGC',
                'immediate': int(instr[3], 2),
                'set_status': int(instr[8], 2),
                'Rn': CORE.GRegisters.set_and_read(int(instr[9:13], 2)),
                'logic': int(instr[17:19], 2),
                'operand': operand,
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'LGC',
                'Rd': int(instr[13:17], 2),
                'timer': CycleTimer(1)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[13:17], 2))
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
            if opcode == '0001':

                # If register is in use
                if CORE.pipeline.check_dependency(int(instr[9:13], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                if CORE.pipeline.check_dependency(int(instr[13:17], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                if int(instr[3], 2) == 0:
                    if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                        return (CycleStatus.WAIT, int(instr , 2))
                    else:
                        operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
                else:
                    operand = instr[17:32]
                
                instruction['execute'] = {
                'code': 'ADD',
                'immediate': int(instr[3], 2),
                'set_status': int(instr[8], 2),
                'Rn': CORE.GRegisters.set_and_read(int(instr[9:13], 2)),
                'operand': operand,
                'timer': CycleTimer(1)
                }
                instruction['memory'] = {}
                instruction['writeback'] = {
                    'code': 'ADD',
                    'Rd': int(instr[13:17], 2),
                    'timer': CycleTimer(1)
                }
                # Add dependencies
                CORE.pipeline.add_dependency(int(instr[13:17], 2))
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

            # INSTRUCTION: MUL
            elif opcode == '0111':

                # If register is in use
                if CORE.pipeline.check_dependency(int(instr[9:13], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                if CORE.pipeline.check_dependency(int(instr[13:17], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                if int(instr[3], 2) == 0:
                    if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                        return (CycleStatus.WAIT, int(instr , 2))
                    else:
                        operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
                else:
                    operand = instr[17:32]
                
                instruction['execute'] = {
                'code': 'MUL',
                'immediate': int(instr[3], 2),
                'set_status': int(instr[8], 2),
                'Rn': CORE.GRegisters.set_and_read(int(instr[9:13], 2)),
                'operand': operand,
                'timer': CycleTimer(1)
                }
                instruction['memory'] = {}
                instruction['writeback'] = {
                    'code': 'MUL',
                    'Rd': int(instr[13:17], 2),
                    'timer': CycleTimer(1)
                }
                # Add dependencies
                CORE.pipeline.add_dependency(int(instr[13:17], 2))
                '''
                code = 'MUL'
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
    elif type_code == '001':  
        
        opcode = instr[4:7]

        # INSTRUCTION: VMUL
        if opcode == '100':

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[7:11], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if CORE.pipeline.check_dependency(int(instr[11:15], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.VRegisters.set_and_read(int(instr[28:32], 2))
            else:
                operand = instr[15:32]

            instruction['execute'] = {
                'code': 'VMUL',
                'immediate': int(instr[3], 2),
                'Rn': CORE.VRegisters.set_and_read(int(instr[7:11], 2)),
                'operand': operand,
                'timer': CycleTimer(3)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'VMUL',
                'Rd': int(instr[11:15], 2),
                'timer': CycleTimer(3)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[11:15], 2))

    # Float type_code    
    elif type_code == '010':
        pass

    # Load/Store type_code
    elif type_code == '011':
        
        opcode = instr[4:7]

        # INSTRUCTION: LDR
        if opcode == '000':

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[7:11], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[23:27], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[23:27], 2))
            else:
                operand = instr[11:27]

            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'LDR',
                'immediate': int(instr[3], 2),
                'operand': operand,
                'offset': int(instr[27:32], 2),
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {
                'code': 'LDR',
                'Rd': int(instr[7:11], 2),
                'timer': CycleTimer(1)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[7:11], 2))
            '''
            code = 'LDR'
            Rd = instr >> 7 & 0b1111
            immediate = instr >> 3 & 1
                1 - Immediate addressing
                0 - Register direct
            operand = instr >> 11 & 0b1111111111111111
            offset = instr >> 27 & 0b11111
            '''

        # INSTRUCTION: LDRV
        elif opcode == '010':

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[6:10], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if CORE.pipeline.check_dependency(int(instr[22:26], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            else:
                operand = CORE.GRegisters.set_and_read(int(instr[22:26], 2))

            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'LDRV',
                'operand': operand,
                'vector': [0] * 64,
                'index': 0,
                'counter': int(instr[26:32], 2),
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {
                'code': 'LDRV',
                'Rd': int(instr[6:10], 2),
                'timer': CycleTimer(1)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[6:10], 2))

        # INSTRUCTION: LDRF
        elif opcode == '100':

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[7:9], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[23:25], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[23:25], 2))
            else:
                operand = instr[9:25]

            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'LDRF',
                'immediate': int(instr[3], 2),
                'operand': operand,
                'offset': int(instr[25:32], 2),
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {
                'code': 'LDR',
                'Rd': int(instr[7:9], 2),
                'timer': CycleTimer(1)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[7:9], 2))

        # INSTRUCTION: STR
        elif opcode == '001':

            if CORE.pipeline.check_dependency(int(instr[7:11], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[23:27], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[23:27], 2))
            else:
                operand = instr[11:27]

            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'STR',
                'Rn': CORE.GRegisters.set_and_read(int(instr[7:11], 2)),
                'immediate': int(instr[3], 2),
                'operand': operand,
                'offset': int(instr[27:32], 2),
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

        # INSTRUCTION: STRV
        elif opcode == '011':

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[6:10], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if CORE.pipeline.check_dependency(int(instr[22:26], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            else:
                operand = CORE.GRegisters.set_and_read(int(instr[22:26], 2))

            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'STRV',
                'Rn': CORE.VRegisters.set_and_read(int(instr[6:10], 2)),
                'operand': operand,
                'offset': int(instr[26:32], 2),
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {}

        # INSTRUCTION: STRF
        elif opcode == '101':

            # If register is in use
            if CORE.pipeline.check_dependency(int(instr[7:9], 2)):
                return (CycleStatus.WAIT, int(instr , 2))
            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[23:25], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.FRegisters.set_and_read(int(instr[23:25], 2))
            else:
                operand = instr[9:25]

            instruction['execute'] = {}
            instruction['memory'] = {
                'code': 'STR',
                'Rn': CORE.FRegisters.set_and_read(int(instr[7:9], 2)),
                'immediate': int(instr[3], 2),
                'operand': operand,
                'offset': int(instr[25:32], 2),
                'timer': CycleTimer(1)
            }
            instruction['writeback'] = {}

    # Branch type_code
    elif type_code == '100':

        opcode = instr[3:6]

        # INSTRUCTION: BX
        if opcode == '001':

            if int(instr[6:8], 2) == 1:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
            elif int(instr[6:8], 2) == 2:
                print('lol no (register indirect)')
            else:
                operand = instr[8:32]

            instruction['execute'] = {
                'code': 'BX',
                'addressing': int(instr[6:8], 2),
                'operand': operand,
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {}
            '''
            code = 'BX'
            addressing = instr >> 6 & 0b11
                00 - Immediate
                01 -  Register direct
                10 - Register indirect
                11 - PC + immediate
            operand = instr >> 8 & 0b111111111111111111111111
            '''

        # INSTRUCTION: BC
        elif opcode == '010':

            if int(instr[6:8], 2) == 1:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    operand = CORE.GRegisters.set_and_read(int(instr[28:32], 2))
            elif int(instr[6:8], 2) == 2:
                print('lol no (register indirect)')
            else:
                operand = instr[13:32]

            instruction['execute'] = {
                'code': 'BC',
                'addressing': instr[6:8],
                'operand1': instr[8:13],
                'operand2': instr[13:32],
                'timer': CycleTimer(1)
            }
            instruction['memory'] = {}
            instruction['writeback'] = {}
            # Add dependencies
            CORE.pipeline.add_dependency(CORE.status)
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

    # Register Transfer
    elif type_code == '101':

        opcode = instr[3:5]

        # INSTRUCTION: FTOV
        if opcode == '00': 

            if CORE.pipeline.check_dependency(int(instr[6:8], 2)):
                return (CycleStatus.WAIT, int(instr, 2))
            if CORE.pipeline.check_dependency(int(instr[8:12], 2)):
                return (CycleStatus.WAIT, int(instr, 2))
            if CORE.pipeline.check_dependency(int(instr[24:28], 2)):
                return (CycleStatus.WAIT, int(instr, 2))

            if int(instr[3], 2) == 0:
                if CORE.pipeline.check_dependency(int(instr[28:32], 2)):
                    return (CycleStatus.WAIT, int(instr , 2))
                else:
                    offset = CORE.GRegisters.set_and_read(int(instr[24:28], 2))
            else:
                offset = int(instr[20:28], 2)

            instruction['execute'] = {}
            instruction['memory'] = {}
            instruction['writeback'] = {
                'code': 'FTOV',
                'immediate': int(instr[3], 2),
                'Rn': CORE.FRegisters.set_and_read(int(instr[6:8], 2)),
                'Rd': int(instr[8:12], 2),
                'offset': offset,
                'timer': CycleTimer(1)
            }
            # Add dependencies
            CORE.pipeline.add_dependency(int(instr[8:12], 2))

    else:
        print("Invalid type code")
        return (CycleStatus.DONE, None)

    return (CycleStatus.DONE, instruction)    



def execute(instruction: dict, CORE):
    if instruction is None:
        return (CycleStatus.DONE, None)

    if instruction['execute'] == {}:
        return (CycleStatus.DONE, instruction)

    if instruction['squashed'] == True:
        return (CycleStatus.DONE, instruction)

    if instruction['execute']['timer'].check_on(3735928559) == CycleStatus.WAIT:
        return (CycleStatus.WAIT, instruction)
    
    # EXECUTE: END
    if instruction['execute']['code'] == 'END':
        status_reg = CORE.status.read()
        status_reg = format(status_reg, '032b')

        # Set the status register at index 32 to true
        status_reg = status_reg[:31] + '1'

        status_reg = int(status_reg, 2)
        CORE.status.write(status_reg)
        instruction['squashed'] = True

        return (CycleStatus.SQUASH, instruction)

    # EXECUTE: ADD
    elif instruction['execute']['code'] == 'ADD':
        # value at register 1
        val1 = instruction['execute']['Rn']
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = int(instruction['execute']['operand'], 2)
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = instruction['execute']['operand']
        else:
            raise Exception("Wrong addressing mode")

        instruction['result'] = CORE.GALU.add(val1, val2)

    # EXECUTE: MUL
    elif instruction['execute']['code'] == 'MUL':
        # value at register 1
        val1 = instruction['execute']['Rn']
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = int(instruction['execute']['operand'], 2)
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = instruction['execute']['operand']
        else:
            raise Exception("Wrong addressing mode")

        instruction['result'] = CORE.GALU.mul(val1, val2)

    # EXECUTE: VMUL
    elif instruction['execute']['code'] == 'VMUL':
        # value at register 1
        val1 = instruction['execute']['Rn']
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = int(instruction['execute']['operand'], 2)
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = instruction['execute']['operand']
        else:
            raise Exception("Wrong addressing mode")

        instruction['result'] = CORE.VALU.vmul(val1, val2)

    # CMP
    elif instruction['execute']['code'] == 'CMP':
        # value at register 1
        val1 = instruction['execute']['Rn']
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = int(instruction['execute']['operand'], 2)
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = instruction['execute']['operand']
        else:
            raise Exception("Wrong addressing mode")

        instruction['result'] = CORE.GALU.comp(val1, val2)
        
    # SHT
    elif instruction['execute']['code'] == 'SHT':
        # value at register 1
        val1 = instruction['execute']['Rn']
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = int(instruction['execute']['operand'], 2)
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = instruction['execute']['operand']
        else:
            raise Exception("Wrong addressing mode")
        
        arithmethic = instruction['execute']['arithmethic']

        instruction['result'] = CORE.GALU.sht(arithmethic, val1, val2)

    # LGC
    elif instruction['execute']['code'] == 'LGC':
        # value at register 1
        val1 = instruction['execute']['Rn']
        # If it is immediate
        if instruction['execute']['immediate'] == 1:
            val2 = int(instruction['execute']['operand'], 2)
        # If it is register direct
        elif instruction['execute']['immediate'] == 0:
            val2 = instruction['execute']['operand']
        else:
            raise Exception("Wrong addressing mode")

        logic = instruction['execute']['logic']

        instruction['result'] = CORE.GALU.lgc(logic, val1, val2)

    # BX
    elif instruction['execute']['code'] == 'BX':
        # If it is immediate
        if instruction['execute']['addressing'] == 0:
            address = int(instruction['execute']['operand'], 2)
        # If it is Register direct
        elif instruction['execute']['addressing'] == 1:
            address = instruction['execute']['operand']
        # If it is Register indirect
        elif instruction['execute']['addressing'] == 2:
            print('lol no')
        # If it is PC + immediate
        elif instruction['execute']['addressing'] == 3:
            address = CORE.pc.read() + int(instruction['execute']['operand'], 2)
        else:
            raise Exception("Wrong addressing mode")

        instruction['squashed'] = True

        # Write into Program Counter
        CORE.pc.write(address)

        return (CycleStatus.SQUASH, instruction)

    # BC
    elif instruction['execute']['code'] == 'BC':
        # Check if condition is true
        status_bit_offset = int(instruction['execute']['operand1'], 2)
        status = CORE.status.read()
        status = format(status, '032b')
        if status[status_bit_offset] != '1':
            return (CycleStatus.DONE, instruction)

        # If it is immediate
        if instruction['execute']['addressing'] == '00':
            address = int(instruction['execute']['operand2'], 2)
        # If it is Register direct
        elif instruction['execute']['addressing'] == '01':
            address = instruction['execute']['operand2']
        # If it is Register indirect
        elif instruction['execute']['addressing'] == '10':
            print('lol no')
        # If it is PC + immediate
        elif instruction['execute']['addressing'] == '11':
            address = CORE.pc.read() + int(instruction['execute']['operand2'], 2)
        else:
            raise Exception("Wrong addressing mode")

        instruction['squashed'] = True 

        # Write into Program Counter
        CORE.pc.write(address)

        # Release status register
        CORE.pipeline.remove_dependency(CORE.status)

        return (CycleStatus.SQUASH, instruction)

    else:
        raise Exception("Invalid instruction")
        
    return (CycleStatus.DONE, instruction)


def load_store(instruction: dict, CORE):
    if instruction is None:
        return (CycleStatus.DONE, None)

    if instruction['memory'] == {}:
        return (CycleStatus.DONE, instruction)

    if instruction['squashed'] == True:
        return (CycleStatus.DONE, instruction)

    if instruction['memory']['timer'].check_on(3735928559) == CycleStatus.WAIT:
        return (CycleStatus.WAIT, instruction)

    # STR (write)
    if instruction['memory']['code'] == 'STR':
        val = instruction['memory']['Rn']
        # If it is immediate
        if instruction['memory']['immediate'] == 1:
            address = int(instruction['memory']['operand'], 2)
        # If it is register direct
        elif instruction['memory']['immediate'] == 0:
            address = instruction['memory']['operand']
        else:
            raise Exception("Wrong addressing mode")

        # Write
        status = CORE.memory.store(address, val)
        return (status, instruction)

    # STRV (write vector)
    elif instruction['memory']['code'] == 'STRV':
        if instruction['memory']['offset'] == 0:    
            vector = instruction['memory']['Rn']
        else:
            vector = instruction['memory']['Rn']
            vector[instruction['memory']['offset']:64] = 0

        address = instruction['memory']['operand']

        # Write
        status = CORE.memory.store(address, vector)
        return (status, instruction)

    # STRF (write float)
    if instruction['memory']['code'] == 'STRF':
        val = instruction['memory']['Rn']
        # If it is immediate
        if instruction['memory']['immediate'] == 1:
            address = int(instruction['memory']['operand'], 2)
        # If it is register direct
        elif instruction['memory']['immediate'] == 0:
            address = instruction['memory']['operand']
        else:
            raise Exception("Wrong addressing mode")

        # Write
        status = CORE.memory.store(address, val)
        return (status, instruction)

    # LDR (read)
    elif instruction['memory']['code'] == 'LDR':
        # If it is immediate
        if instruction['memory']['immediate'] == 1:
            address = int(instruction['memory']['operand'], 2)
        # If it is register direct
        elif instruction['memory']['immediate'] == 0:
            address = instruction['memory']['operand']
        else:
            raise Exception("Wrong addressing mode")

        # Read
        results = CORE.memory.query(address)
        instruction['result'] = results[1]
        return (results[0], instruction)

    # LDRV (read vector)
    elif instruction['memory']['code'] == 'LDRV':
        address = instruction['memory']['operand']

        # Read
        if instruction['memory']['index'] <= instruction['memory']['counter']:
            results = CORE.memory.query(address)
            if results[0] == CycleStatus.DONE:
                instruction['memory']['vector'][instruction['memory']['index']] = results[1]
                instruction['memory']['index'] += 1
                return (CycleStatus.WAIT, instruction)
            else:
                return (CycleStatus.WAIT, instruction)
        else:
            instruction['result'] =  instruction['memory']['vector']
            return (CycleStatus.DONE, instruction)

    # LDRF (read float)
    elif instruction['memory']['code'] == 'LDRF':
        # If it is immediate
        if instruction['memory']['immediate'] == 1:
            address = int(instruction['memory']['operand'], 2)
        # If it is register direct
        elif instruction['memory']['immediate'] == 0:
            address = instruction['memory']['operand']
        else:
            raise Exception("Wrong addressing mode")

        # Read
        results = CORE.memory.query(address)
        instruction['result'] = results[1]
        return (results[0], instruction)

    # CMP TODO: fix compares
    elif instruction['memory']['code'] == 'CMP':
        result = instruction['result']
        status_reg = CORE.status.read()
        status_reg = format(status_reg, '032b')
        
        if result == 1:
            status_reg = '011010' + status_reg[6:] #0(EQ)1(NEQ)1(GT)0(LT)1(GE)0(LE)
        elif result == -1:
            status_reg = '010101' + status_reg[6:] #0(EQ)1(NEQ)0(GT)1(LT)0(GE)1(LE)
        elif result == 0:
            status_reg = '100011' + status_reg[6:] #1(EQ)0(NEQ)0(GT)0(LT)1(GE)1(LE)
        
        status_reg = int(status_reg, 2)
        result = CORE.status.write(status_reg)

        # Release status register
        CORE.pipeline.remove_dependency(CORE.status)

        return (result, instruction)

    else:
        raise Exception("Invalid instruction")


def write_back(instruction: dict, CORE):
    if instruction is None:
        return (CycleStatus.DONE, None)

    if instruction['writeback'] == {}:
        return (CycleStatus.DONE, instruction)

    if instruction['squashed'] == True:
        return (CycleStatus.DONE, instruction)

    if instruction['writeback']['timer'].check_on(3735928559) == CycleStatus.WAIT:
        return (CycleStatus.WAIT, instruction)

    # MOV
    if instruction['writeback']['code'] == 'MOV':
        if instruction['writeback']['immediate'] == 1:
            val = int(instruction['writeback']['operand'], 2)
        # If it is register direct
        elif instruction['writeback']['immediate'] == 0:
            val = instruction['writeback']['operand']
        else:
            raise Exception("Wrong addressing mode")

        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], val)
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # ADD
    elif instruction['writeback']['code'] == 'ADD':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # MUL
    elif instruction['writeback']['code'] == 'MUL':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # VMUL
    elif instruction['writeback']['code'] == 'VMUL':
        CORE.VRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # SHT
    elif instruction['writeback']['code'] == 'SHT':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # LGC
    elif instruction['writeback']['code'] == 'LGC':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # LDR
    elif instruction['writeback']['code'] == 'LDR':
        CORE.GRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # LDRV
    elif instruction['writeback']['code'] == 'LDRV':
        CORE.VRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # LDRF
    elif instruction['writeback']['code'] == 'LDRF':
        CORE.FRegisters.set_and_write(instruction['writeback']['Rd'], instruction['result'])
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    # FTOV
    elif instruction['writeback']['code'] == 'FTOV':
        # Read vector register 
        vector = CORE.VRegisters.set_and_read(instruction['writeback']['Rd'])
        # Modify float at offset
        vector[instruction['writeback']['offset']] = instruction['writeback']['Rn']
        # Write into vector register
        CORE.VRegisters.set_and_write(instruction['writeback']['Rd'], vector)
        # Remove depencencies
        CORE.pipeline.remove_dependency(instruction['writeback']['Rd'])

    return (CycleStatus.DONE, instruction)
