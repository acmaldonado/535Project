def interpret_asm_line(line):
    tokens = line.lower().split(' ')

    print(tokens)

    if tokens[0] == 'mov':
        if len(tokens) < 3:
            raise Exception("Invalid command")

        instr_type = '000'
        instr_opcode = '0000'

        if tokens[1][0] != 'r':
            raise Exception("Invalid destination register")
        destination = int(tokens[1][1:])
        if destination > 11:
            raise Exception("Invalid destination register")
        else:
            destination = format(destination, '04b')

        if tokens[2][0] == '#':
            value = format(int(tokens[2][1:]), '019b')
            immediate = '1'
            
        elif tokens[2][0] == 'r':
            value = int(tokens[2][1:])
            if value > 11:
                raise Exception("Invalid value register")
            else:
                value = format(value, '019b')
            immediate = '0'
        else:
            raise Exception("Invalid value")

        signal = '0'
        if len(tokens) > 3:
            if tokens[3] == '1' or tokens[3] == 'true':
                signal = '1'
        
        command = instr_type + immediate + instr_opcode + signal + destination + value
        return command
    else:
        return "unknown command"

if __name__ == '__main__':
    test_command = input('input asm command:')
    output = interpret_asm_line(test_command)
    print(f'Binary value: {output}, Int value: {int(output, 2)}')


        
