import struct
import sys
import os

if os.name == 'Windows':
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\assembler'
    path_denom = '\\'
else:
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/assembler'
    path_denom = '/'

def float_to_bin(num):
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary)))[0]

def file_values_to_float(afile):

    with open(dir_path + path_denom + afile, 'r') as arrayf:
        lines = arrayf.readlines()

    newlines = []

    for line in lines:
        newlines.append(int(float_to_bin(float(line)),2))

    with open(dir_path + path_denom + afile + '2', 'w') as af:
        for line in newlines:
            af.write(str(line) + '\n')

if __name__ == '__main__':
    '''inp = ''
    while inp != 'q':
        inp = input()
        if inp == 'q':
            continue
        else:
            print(int(float_to_bin(float(inp)),2))'''

    file_values_to_float(sys.argv[1])