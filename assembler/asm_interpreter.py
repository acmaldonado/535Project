def interpret_asm_line(line):
    tokens = line.lower().split(' ')

    print(tokens)

    if tokens[0] == 'mov':
        if len(tokens) < 3:
            raise Exception(f"Invalid command \'{line}\'")

        instr_type = '000'
        instr_opcode = '0000'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[1][0]}\'")
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1][0]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '019b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2][0]}\'")
            else:
                value = format(value, '019b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2][0]}\'")

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
            raise Exception(f"Invalid destination register \'{tokens[1][0]}\'")
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1][0]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '016b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2][0]}\'")
            else:
                value = format(value, '016b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2][0]}\'")

        command = instr_type + immediate + instr_opcode + destination + value + '00000'
        return command
        
    elif tokens[0] == 'str':
        if len(tokens) < 3:
            raise Exception(f"Invalid command \'{line}\'")

        instr_type = '011'
        instr_opcode = '001'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[1][0]}\'")
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[1][0]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '016b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[2][0]}\'")
            else:
                value = format(value, '016b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[2][0]}\'")

        command = instr_type + immediate + instr_opcode + destination + value + '00000'
        return command
        
    elif tokens[0] == 'add':
        if len(tokens) < 4:
            raise Exception(f"Invalid command \'{line}\'")
        
        instr_type = '000'
        instr_opcode = '0001'

        if tokens[1][0] != 'r':
            raise Exception(f"Invalid operand register \'{tokens[1][0]}\'")
        operand1 = int(tokens[1][1:])
        if operand1 > 11:
            raise Exception(f"Invalid operand register \'{tokens[1][0]}\'")
        else:
            operand1 = format(operand1, '04b')

        if tokens[2][0] != 'r':
            raise Exception(f"Invalid destination register \'{tokens[2][0]}\'")
        destination = int(tokens[2][1:])
        if destination > 11:
            raise Exception(f"Invalid destination register \'{tokens[2][0]}\'")
        else:
            destination = format(destination, '04b')

        if tokens[3][0] == '#':
            value = format(int(tokens[3][1:]), '015b')
            immediate = '1'
            
        elif tokens[3][0] == 'r':
            value = int(tokens[3][1:])
            if value > 11:
                raise Exception(f"Invalid value register \'{tokens[3][0]}\'")
            else:
                value = format(value, '015b')
            immediate = '0'
        else:
            raise Exception(f"Invalid value \'{tokens[3][0]}\'")

        signal = '0'
        if len(tokens) > 4:
            if tokens[4] == '1' or tokens[4] == 'true':
                signal = '1'

        command = instr_type + immediate + instr_opcode + signal + operand1 + destination + value
        return command

    elif tokens[0] == 'end':
        return '11111111111111111111111111111111'

    else:
        return "unknown command"

if __name__ == '__main__':
    test_command = None

    while test_command != 'quit':

        test_command = input('input asm command:')
        if test_command == 'quit':
            continue
        output = interpret_asm_line(test_command)
        print(f'Binary value: {output}, Int value: {int(output, 2)}')


        
