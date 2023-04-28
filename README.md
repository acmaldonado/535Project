# 535Project

# Project Report


# Overview

	This special purpose architecture will be focused in vector computations and the optimization of complex numbers and analysis.The architecture will feature vector operations, vector load and store, and vector pipeline improvement and it will be based on either a RISC architecture or some architecture which exploits vectorization like SIMD or RISCV. The architecture will have a word size of 32 bits.


# Supported Data Types



* Integer
* Scalar Floats 
* Cray Vectors


## Supported Operations by Type

	Data types will support bitwise operations and shifts (logical and arithmetic), basic arithmetic operations, and various vector oriented operations like gather, scatter, pack, unpack, compare, arithmetic, and mask.



* <span style="text-decoration:underline;">Int:</span> arithmetic, logic, shift, comparison
* <span style="text-decoration:underline;">Float:</span> arithmetic, comparison
* <span style="text-decoration:underline;">Vector:</span> gather, scatter, arithmetic, pop. count


## Condition Codes by Type



* <span style="text-decoration:underline;">Int:</span> overflow, zero, non-zero, sign, special state
* <span style="text-decoration:underline;">Float:</span> overflow, underflow, NaN, denormalized, infinity, zero, nonzero, mantissa sign, exponent sign
* <span style="text-decoration:underline;">Vector:</span> Equality, exceptions


# Registers

	32 registers total



* Reserved System Registers(PC, Link, Status) 3
* General purpose registers 12 (R0, … , R11)
* Specialized vector registers 12(R0, …, R11)
* Float register 4(R0, …, R3)

**NOTE: **Instructions are type specific, so each register bank indexes independently from each other. Any instructions that attempt to address registers that do not exist will result in a compilation error from the interpreter


## Status Register:

The status register will carry status bits which will be used for comparisons and branching on conditions. It will also be used to store exceptions and special conditions during processing if the status bit in the instruction is set to 1. The status bits are as follows:

	0: EQ, equality

	1: NEQ, not equal

2: GT, greater than


    3: LT, less than


    4:GE, greater than or equal to


    5: LE, less than or equal to


    6: OVF, overflow


    7: ZE, zero


    8: SGN, sign


    9: UDF, underflow


    10: NAN, not-a-number


    11: DNM, denormalized


    12: INF, infinity


    13: MSN, mantissa sign


    14: ESN, exponent sign


    15-30: UNDEFINED


    31: END, program terminated


# Miscellaneous



* 32-bit word size
* Princeton instruction set design
* Word addressing
* Support for:
    * Immediate
    * Register direct
    * PC + immediate
* Up to 3 operands per instruction


# Instruction Set

**NOTE:** For all instruction formats:


    **A** = Arithmetic mode: Determines if the shift is logical or arithmetic.


    **I** = Addressing mode: Determines if the addressing is immediate, register direct, or PC + immediate.


    **S** = Status bit: Determines if the operation changes the status register. 


## Instruction Types (With Addressing Modes):

**	**


<table>
  <tr>
   <td><strong>Type Code</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Addressing Modes</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>Data Processing
   </td>
   <td>Immediate, Register direct
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>Vector Processing
   </td>
   <td>Register direct
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Float Processing
   </td>
   <td>Immediate, Register direct
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Load/Store
   </td>
   <td>Immediate, Register direct, Register indirect, Register indirect base + index
   </td>
  </tr>
  <tr>
   <td>100
   </td>
   <td>Branch
   </td>
   <td>PC + immediate, Register direct, Register indirect
   </td>
  </tr>
  <tr>
   <td>101
   </td>
   <td>Register Transfer
   </td>
   <td>Register direct
   </td>
  </tr>
  <tr>
   <td>110
   </td>
   <td>Matrix Operation
   </td>
   <td>Register direct, Register Indirect
   </td>
  </tr>
  <tr>
   <td>111
   </td>
   <td>Reserved for future use
   </td>
   <td>
   </td>
  </tr>
</table>



### Data Processing: 4 bit opcode

**END**

A series of 32 f’s which indicate the end of execution that mark the fetch process to stop fetching.


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
  </tr>
</table>


**MOV: Opcode 0000**

Move. Operation copies the value contained in Operand2 into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="18" ><code>Operand 2</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**ADD: Opcode 0001**

Add. Arithmetic addition operation for 32-bit signed ints. Operation adds the value contained in Operand3 and Rn into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**SUB: Opcode 0010**

Subtract. Arithmetic subtraction operation for 32-bit signed ints (ints). Operation subtracts the value contained in Operand3 from Rn and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**RSUB: Opcode 0011**

Reverse Subtraction. Arithmetic subtraction operation using reverse subtraction algorithm for 32-bit signed ints (ints). Operation reverse subtracts the value contained in Operand3 from Rn and stores it into Rd. The ‘I’ bit specifies the addressing 

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**MOD: Opcode 0100**

Modulo. Arithmetic modulo operation for 32-bit signed ints  (ints). Operation returns the result of Rn % Operand3 and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**DIV: Opcode 0101**

Divide. Arithmetic division operation for 32-bit signed ints. Operation returns the result of Rn / Operand3 and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**MUL: Opcode 0111**

Multiply. Arithmetic multiplication operation for 32-bit signed ints. Operation returns the result of Rn * Operand3 and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**SHT: Opcode 1000**

Shift. Shift operation for 32-bit signed ints. The ‘A’ bit signifies whether or not the shift is arithmetic (as opposed to logical). Operations perform an (arithmetic or logical) shift on Rn with respect to Operand3 and stores the result in Rd.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct

 A-bit                            

0 - Logical shift

1 - Arithmetic shift


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="14" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**CMP: Opcode 1001**

Compare. Comparison operator for 32-bit signed ints. The operation compares the value from Rn to Operand2 for all possible status register statuses. It sets the appropriate status bit as indicated by the Status Register section and deletes any conflicting status bits. (AKA something cannot be > and &lt;)

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="19" ><code>Operand 2</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**LGC: Opcode 1010**

Logic. All logical operations for 32-bit signed ints fall under this (not, nand, and, or). Depending on what the L bits are set to, the appropriate logical operation will be selected. 

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct

L-bit: indicates the type of logic operation performed in the values.

00 - NOT

01 - NAND

10 - AND

11 - OR


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>L</code>
   </td>
   <td rowspan="2" colspan="13" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**Opcodes 1100-1111 UNDEFINED (NoOp)**


### **Vector Processing: 3 bit opcode**

**VMOV: Opcode 000**

Vector Move. Copies the vector in Rn into Rd


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="18" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VADD: Opcode 001**

Vector Add. Adds vector in Rn + Rm into Rd


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="14" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VSUB: Opcode 010**

Vector Subtract. Subtracts vector in Rn - Rm into Rd


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="14" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VTRP: Opcode 011**

Vector Transpose. Performs vector transpose on Rn


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="22" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VMUL: Opcode 100**

Vector Multiply. Performs vector multiply in Operand 3 multiply Rn into Rd

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="17" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**HALT: Opcode 111**

Halt. Halt all vector operations


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="26" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



### Float Processing: 3 bit opcode

**FMOV: Opcode 000**

Float Move. Operation copies the value of Rninto Rd. The ‘A’ bit specifies the addressing mode.


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="21" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FADD: Opcode 001**

Float Addition. Arithmetic addition operation for float scalar data types. Rn + Operand3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FSUB: Opcode 010**

Float Subtract. Arithmetic subtraction operation for float scalar data types Rn - Operand3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FRSUB: Opcode 011**

Float Reverse Subtract. Arithmetic subtraction operation using reverse subtraction algorithm for float scalar data types Rn reverse subtract Operand 3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FDIV: Opcode 100**

Float Divide. Arithmetic division operation for float scalar data types Rn / Operand 3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FMUL: Opcode 101**

Float Multiply. Arithmetic multiplication operation for float scalar data types Rn * Operand 3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FCMP: Opcode 110**

Float Compare. Comparison operator for 32-bit signed ints. Rn compared to Operand 2


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="21" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



### Load/Store: 3 bit opcode

**LDR: Opcode 000**

Load General. Load value into general register from memory. 


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="5" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rd: Destination Register
Operand 2: Memory Address or Register
```


**STR: Opcode 001**

Store General. Store value into memory from general register into memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="5" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rn: First Operand Register
Operand 2: Memory Address or Register
```


**LDRV: Opcode 010**

Load Vector. Load vector into vector register from memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="6" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
Rd: Destination Register
Operand 2: Register
```


**STRV: Opcode 011**

Store Vector. Store vector from vector register into memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="6" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
Rn: First Operand Register
Operand 2: Register
```


**LDRF: Opcode 100**

Load Float. Load float into float register from memory


<table>
  <tr>
   <td><code>3</code>
   </td>
   <td><code>3</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="7" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rd: Destination Register
Operand 2: Memory Address or Register
```


**STRF: Opcode 101**

Store Float. Store float from float register into memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="7" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rn: First Operand Register
Operand 2: Memory Address or Register
```



### Branch: 3 bit opcode

**BR: Opcode 000**

Branch. Loads a value into the PC register


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="6" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**BX: Opcode 001**

Branch Indirect. Loads a value into the PC register from a memory location held in another register


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="24" ><code>Operand 1</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**BC: Opcode 010**

Branch on Condition. Sets the program counter to a value iff the specified status bit is set to TRUE

**A:**

00 - Immediate

01 -  Register direct

10 - Register indirect

11 - PC + immediate


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="5" ><code>Operand 1</code>
   </td>
   <td rowspan="2" colspan="19" ><code>Operand 2</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
Operand 1: Bit number in status register to branch on
Operand 2: Address or register with address to branch to
```



#### **JMP: Opcode 011**

Jump. Stores the value in the PC register in the LR register and loads a value into the PC register from a memory location held in another register


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="18" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



### Register Transfer: 2 bit opcode


##### **FTOV: Opcode 00**

Float to Vector. Places a value from Rn in the Vector Rd at index of Offset


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Offset</code>
   </td>
   <td rowspan="2" colspan="5" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



##### **VTOF: Opcode 01**

Vector to Float. Places a value from Rd at index Operand 3 in Rn


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 3</code>
   </td>
   <td rowspan="2" colspan="5" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



# Work Division

The work has been divided in accordance with our strengths.  

**Manuel**: Memory (RAM and Cache), ALU instructions, Load instructions, Branching instructions, Pipeline stages (Decode, execute, memory, and writeback).

**Manav**: Memory (RAM and Cache), GUI for memory interpretation, GUI for memory settings, GUI for running through simulations, GUI for loading, storing, and writing instructions.

**Andrew: **Memory (RAM and Cache), ALU, Pipeline framework, fetching, Instruction Squashing, Register bank, Interpreter and assembler.


## Software Engineering Methods



* **Language:** Python 3
* **Team Organization: **Each team member took ownership of specific subsystems and files. Together the team would meet and decide which tasks needed to be completed before each major deadline, and break down what they planned to do for their subsystem and what needed to be done in other subsystems. Then at a planned date before a deadline the team would meet up to integrate changes, test the system as a whole, and debug where necessary.
* **Organizational Tools: **We used services like Slack and Discord to organize meetings, communicate changes, ask questions, and collaboratively work on the integration testing. Github Kanban was used for breaking up and keeping track of tasks that were being worked on.
* **Version Control:** GIT repositories were used locally, and Github was used for remote tracking.
* **Code Guidelines:** Used standard Python style for naming conventions, comments, and general program flow. Interfaces were documented using a consistent comment style to indicate the purpose, expected argument types, and the return type.


## Simulator

**How it works: **Custom assembly code is written which is later preprocessed, and interpreted into binary instructions which are then stored in memory. A “CORE” is initialized which has a memory(which includes main memory and caches), register banks, pipeline, and ALU associated with it. The pipeline fetches the instructions from memory which are sent to the decode stage. The decode stages decodes the instructions into Python dictionaries and extracts all values from the registers. At this stage, it records and checks for data dependencies in a dependency table. If there are no dependencies associated with this instruction, it packages the relevant data and sends the instruction to the execute state. The execute stage performs any necessary operations with help of the ALU, and packages the result into the instruction dictionary that is sent to the memory stage.The memory stage loads and stores values into memory if necessary, and sends the instruction forward to the writeback stage. And the writeback stage writes the result back into any registers passed by the instruction, and clears dependencies from the table. The pipeline stages ensure the system registers like the status registers and link register are updated accordingly in case of branching or comparisons. Meanwhile, the pipeline fetch updates the PC counter. Once an END instruction is processed by the execute stage, a flag is raised in the status register that indicates the program has terminated, and fetch will stop fetching instructions from memory.

**Writing Programs:** In order to write programs, there is an interpreter script located in the root directory named ‘asm_interpreter.py’. This script can be used to interpret a txt file containing assembly code, convert it into a txt file containing the program translated into integers representing binary, and finally create a json file which represents an empty memory with the program loaded in, starting from address 0. This same script also contains a utility for loading arrays of binary values into a memory json file, starting from a given starting address using a txt file with integer values representing binary for each desired value on a new line. The command format for using this script via the command line is as follows:

	

	**Interpret ASM to Memory:**

	asm_interpreter.py **int [ASM file location] [Desired name of binary and json]**

	**Load Array into Existing Memory:**

	asm_interpreter.py **arr [Mem File Location] [Array File Location] [Start Address]**

NOTE: The interpreter supports ASM programs written using tags for jumps and branches

where the tag is formatted as ‘[Tag Name]:’ on a line alone. This tag name can be used

in place of memory addresses or register numbers of a branch or jump instruction. The

interpreter also supports comments indicated by starting with ‘//’, and these lines will be

Ignored. Finally, the assembler supports use of acronyms for the status bits in comparison instructions. Refer to the [status register list] for the acronyms.

**Running Programs:** Once you have written a program and generated a memory file, you can start the User Interface by using the command line to run a script named ‘core.py’ in the root directory. The command format for running this script via the command line is as follows:

	

	**Running the Application GUI:**

	

	Core.py **[Mem File Location]**

This will launch a window that can be used for viewing or altering the state of the simulated machine at any given time, as well as for simulating cycles or running the loaded program to completion. The window is divided into five tabs: **Command Line, Memory, Registers, Diagnostic, and Pipeline**. The first tab you will see is the **Command Line** tab as shown below:



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


The command field is used for debug commands to manually send read or write requests to RAM, with the output from the command being displayed in the Output section. This tab was mainly used for GUI debugging, and is usually unimportant for running an application. The next tab is the **Memory** tab as shown below:



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


This tab shows the contents of the different levels of cache and the RAM. The label at the top indicates which level of memory is currently being viewed with it being an integer for cache level or RAM if main memory is being viewed instead. The level of cache being viewed can be changed by pressing the ‘Go up’ and ‘Go down’ buttons to navigate. The main window shows each line of cache or memory, with each word in hexadecimal format being separated by a space, as well as information such as the tag of the line being stored and the state of the valid bit. Even though tag and valid are present in RAM, they are not actually used. The text bar labeled ‘Go to address’ can be used to move the window to a specific memory location by inputting it into the text box and pressing ENTER. Finally, the checkboxes at the bottom labelled ‘Cache’ and ‘Pipeline’ are used to toggle whether or not the cache and the pipeline are used respectively. They both start as enabled by default. The next tab is the **Registers** tab as shown below:



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


This tab displays the contents of the various registers. The name of the register currently being viewed is the label at the top of the window, with registers being labelled as either a special register(PC, Status, LR, RET), or the type of register (General, Float, Vector) followed by the number of that particular register. The value or values contained in the register are shown in the box in the middle. The registers can be navigated using the ‘Previous’ and ‘Next’ buttons. The next tab is the **Diagnostic** tab as shown below:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


This tab is used to view the number of cycles run since the start of the machine and is used to continue the simulation. To run a specific number of cycles, type the number of cycles into the text box under the label ‘How many cycles to run’ and press ENTER. In order to have the simulation run to completion, press the button labeled ‘Run to completion’. The last tab is the **Pipeline** tab as shown below:



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


This tab is used to view the current state of the pipeline during execution. Each label represents a stage in the pipeline, and next to it is listed the instruction currently being held at that stage. This representation includes the control signals passed to each stage for each instruction.


## Benchmark Results

We ran three different benchmarks including: Exchange Sort, Matrix Multiply w/o Vectors, and Matrix Multiply with Vectors. Each was run on the following four settings: Pipeline and Cache(ppc), Cache only(c), Pipeline only(pp), and No Pipeline or Cache(n). All simulations were run with an L1 access time of 1 cycle, an L2 access time of 3 cycles, and a RAM access time of 100 cycles. The results of these benchmarks can be seen in the tables below:

**Exchange Sort: **Sorting 50 random integer values in memory


<table>
  <tr>
   <td><strong>Setting</strong>
   </td>
   <td><strong>Runtime(cycles)</strong>
   </td>
  </tr>
  <tr>
   <td>PPC
   </td>
   <td>170,673
   </td>
  </tr>
  <tr>
   <td>C
   </td>
   <td>205,826
   </td>
  </tr>
  <tr>
   <td>PP
   </td>
   <td>1,497,798
   </td>
  </tr>
  <tr>
   <td>N
   </td>
   <td>1,535,326
   </td>
  </tr>
</table>


**Matrix Multiply w/o Vectors: **Multiplying two 5x5 integer matrices in memory without using Vector instructions


<table>
  <tr>
   <td><strong>Setting</strong>
   </td>
   <td><strong>Runtime(cycles)</strong>
   </td>
  </tr>
  <tr>
   <td>PPC
   </td>
   <td>21,788
   </td>
  </tr>
  <tr>
   <td>C
   </td>
   <td>26,831
   </td>
  </tr>
  <tr>
   <td>PP
   </td>
   <td>217,227
   </td>
  </tr>
  <tr>
   <td>N
   </td>
   <td>224,231
   </td>
  </tr>
</table>


**Matrix Multiply with Vectors: **Multiplying two 5x5 float matrices in memory using Vector instructions


<table>
  <tr>
   <td><strong>Setting</strong>
   </td>
   <td><strong>Runtime(cycles)</strong>
   </td>
  </tr>
  <tr>
   <td>PPC
   </td>
   <td>7,771
   </td>
  </tr>
  <tr>
   <td>C
   </td>
   <td>7,856
   </td>
  </tr>
  <tr>
   <td>PP
   </td>
   <td>59,742
   </td>
  </tr>
  <tr>
   <td>N
   </td>
   <td>61,056
   </td>
  </tr>
</table>


**Results:** It seems from our simulations that in all three of the benchmarks, the speedup of cache is much more significant than the speedup from the pipeline. This is especially true for the Matrix Multiply with Vectors. The results also show that the matrix multiplication ran significantly faster using the Vector instructions than without with a max speedup of 3.67x for the No Cache or Pipeline condition, and an average speedup of 3.38x. It is also worth noting that because our Vectors are all float vectors, the vector arithmetic takes 3 cycles to compute rather than the 1 cycle computations with integers. The speedup we observe is in spite of the added cost of performing float calculations.


# What have we learned:

	There were many different concepts in the architecture of a processor that we got a greater understanding of from making this simulator. Some of the first things we learned had to do with the specifics regarding the memory subsystem. We already had some prior knowledge to the structure of data in caches and RAM due to experience in classes like CS230 and CS335, but there were several things that we gained a greater appreciation for. The first was the importance and surprising complexity of the address calculation step. This step is often brushed over in these classes as something that automatically happens, but we never had to do these steps ourselves. Secondly, we got a greater appreciation for how the almost recursive nature of the different levels of cache benefits a Write-Through cache. While not receiving the potential performance benefits of Write-Back, the simplicity of making a multi-level Write-Through proved to be a great advantage in terms of logic. Finally, while writing the memory subsystem we gained a greater appreciation for how long it actually takes to access memory in a program. Often it is something that is mentioned, but it is rather difficult to notice due to the speed of modern clocks. While writing the memory subsystem we noticed how much of a program’s execution time is spent in memory, even just to fetch instructions, and why a cache with large lines is extremely beneficial. This is also related to the pipeline and the various stages. Implementing the different stages improved the understanding of what each stage is responsible for, and how any single instruction is broken down into stages in order to take advantage of parallelism. Then getting each stage of the pipeline to work together concurrently proved to be a great challenge, and drove home the synchronization issues that arise from a deeply connected system like this. Finally, we learned about how different hazards in the pipeline can cause problems in program execution. We figured out how important it is to keep track of a dependency table for registers being used in the pipeline, and to stall the decode of instructions reading those registers. This small step in the pipeline proved to be crucial to ensuring the consistency and correctness of our programs. Lastly, we also learned about the difficulty of writing even a basic interpreter, and the importance of including quality-of-life features such as comments and tags. These seemingly unimportant features ended up being very helpful when writing actual programs such as the matrix multiplication.
Project Repo for CS535
<!-- Copy and paste the converted output. -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 1
* WARNINGs: 0
* ALERTS: 6

Conversion time: 23.394 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Fri Apr 28 2023 15:27:00 GMT-0700 (PDT)
* Source doc: Project Report
* Tables are currently converted to HTML tables.



# Project Report


# Overview

	This special purpose architecture will be focused in vector computations and the optimization of complex numbers and analysis.The architecture will feature vector operations, vector load and store, and vector pipeline improvement and it will be based on either a RISC architecture or some architecture which exploits vectorization like SIMD or RISCV. The architecture will have a word size of 32 bits.


# Supported Data Types



* Integer
* Scalar Floats 
* Cray Vectors


## Supported Operations by Type

	Data types will support bitwise operations and shifts (logical and arithmetic), basic arithmetic operations, and various vector oriented operations like gather, scatter, pack, unpack, compare, arithmetic, and mask.



* <span style="text-decoration:underline;">Int:</span> arithmetic, logic, shift, comparison
* <span style="text-decoration:underline;">Float:</span> arithmetic, comparison
* <span style="text-decoration:underline;">Vector:</span> gather, scatter, arithmetic, pop. count


## Condition Codes by Type



* <span style="text-decoration:underline;">Int:</span> overflow, zero, non-zero, sign, special state
* <span style="text-decoration:underline;">Float:</span> overflow, underflow, NaN, denormalized, infinity, zero, nonzero, mantissa sign, exponent sign
* <span style="text-decoration:underline;">Vector:</span> Equality, exceptions


# Registers

	32 registers total



* Reserved System Registers(PC, Link, Status) 3
* General purpose registers 12 (R0, … , R11)
* Specialized vector registers 12(R0, …, R11)
* Float register 4(R0, …, R3)

**NOTE: **Instructions are type specific, so each register bank indexes independently from each other. Any instructions that attempt to address registers that do not exist will result in a compilation error from the interpreter


## Status Register:

The status register will carry status bits which will be used for comparisons and branching on conditions. It will also be used to store exceptions and special conditions during processing if the status bit in the instruction is set to 1. The status bits are as follows:

	0: EQ, equality

	1: NEQ, not equal

2: GT, greater than


    3: LT, less than


    4:GE, greater than or equal to


    5: LE, less than or equal to


    6: OVF, overflow


    7: ZE, zero


    8: SGN, sign


    9: UDF, underflow


    10: NAN, not-a-number


    11: DNM, denormalized


    12: INF, infinity


    13: MSN, mantissa sign


    14: ESN, exponent sign


    15-30: UNDEFINED


    31: END, program terminated


# Miscellaneous



* 32-bit word size
* Princeton instruction set design
* Word addressing
* Support for:
    * Immediate
    * Register direct
    * PC + immediate
* Up to 3 operands per instruction


# Instruction Set

**NOTE:** For all instruction formats:


    **A** = Arithmetic mode: Determines if the shift is logical or arithmetic.


    **I** = Addressing mode: Determines if the addressing is immediate, register direct, or PC + immediate.


    **S** = Status bit: Determines if the operation changes the status register. 


## Instruction Types (With Addressing Modes):

**	**


<table>
  <tr>
   <td><strong>Type Code</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Addressing Modes</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>Data Processing
   </td>
   <td>Immediate, Register direct
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>Vector Processing
   </td>
   <td>Register direct
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Float Processing
   </td>
   <td>Immediate, Register direct
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Load/Store
   </td>
   <td>Immediate, Register direct, Register indirect, Register indirect base + index
   </td>
  </tr>
  <tr>
   <td>100
   </td>
   <td>Branch
   </td>
   <td>PC + immediate, Register direct, Register indirect
   </td>
  </tr>
  <tr>
   <td>101
   </td>
   <td>Register Transfer
   </td>
   <td>Register direct
   </td>
  </tr>
  <tr>
   <td>110
   </td>
   <td>Matrix Operation
   </td>
   <td>Register direct, Register Indirect
   </td>
  </tr>
  <tr>
   <td>111
   </td>
   <td>Reserved for future use
   </td>
   <td>
   </td>
  </tr>
</table>



### Data Processing: 4 bit opcode

**END**

A series of 32 f’s which indicate the end of execution that mark the fetch process to stop fetching.


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
  </tr>
</table>


**MOV: Opcode 0000**

Move. Operation copies the value contained in Operand2 into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="18" ><code>Operand 2</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**ADD: Opcode 0001**

Add. Arithmetic addition operation for 32-bit signed ints. Operation adds the value contained in Operand3 and Rn into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**SUB: Opcode 0010**

Subtract. Arithmetic subtraction operation for 32-bit signed ints (ints). Operation subtracts the value contained in Operand3 from Rn and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**RSUB: Opcode 0011**

Reverse Subtraction. Arithmetic subtraction operation using reverse subtraction algorithm for 32-bit signed ints (ints). Operation reverse subtracts the value contained in Operand3 from Rn and stores it into Rd. The ‘I’ bit specifies the addressing 

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**MOD: Opcode 0100**

Modulo. Arithmetic modulo operation for 32-bit signed ints  (ints). Operation returns the result of Rn % Operand3 and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**DIV: Opcode 0101**

Divide. Arithmetic division operation for 32-bit signed ints. Operation returns the result of Rn / Operand3 and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**MUL: Opcode 0111**

Multiply. Arithmetic multiplication operation for 32-bit signed ints. Operation returns the result of Rn * Operand3 and stores it into Rd. The ‘I’ bit specifies the addressing mode.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="15" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**SHT: Opcode 1000**

Shift. Shift operation for 32-bit signed ints. The ‘A’ bit signifies whether or not the shift is arithmetic (as opposed to logical). Operations perform an (arithmetic or logical) shift on Rn with respect to Operand3 and stores the result in Rd.

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct

 A-bit                            

0 - Logical shift

1 - Arithmetic shift


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="14" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**CMP: Opcode 1001**

Compare. Comparison operator for 32-bit signed ints. The operation compares the value from Rn to Operand2 for all possible status register statuses. It sets the appropriate status bit as indicated by the Status Register section and deletes any conflicting status bits. (AKA something cannot be > and &lt;)

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="19" ><code>Operand 2</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**LGC: Opcode 1010**

Logic. All logical operations for 32-bit signed ints fall under this (not, nand, and, or). Depending on what the L bits are set to, the appropriate logical operation will be selected. 

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct

L-bit: indicates the type of logic operation performed in the values.

00 - NOT

01 - NAND

10 - AND

11 - OR


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>L</code>
   </td>
   <td rowspan="2" colspan="13" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**Opcodes 1100-1111 UNDEFINED (NoOp)**


### **Vector Processing: 3 bit opcode**

**VMOV: Opcode 000**

Vector Move. Copies the vector in Rn into Rd


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="18" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VADD: Opcode 001**

Vector Add. Adds vector in Rn + Rm into Rd


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="14" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VSUB: Opcode 010**

Vector Subtract. Subtracts vector in Rn - Rm into Rd


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="14" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VTRP: Opcode 011**

Vector Transpose. Performs vector transpose on Rn


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="22" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**VMUL: Opcode 100**

Vector Multiply. Performs vector multiply in Operand 3 multiply Rn into Rd

Immediate addressing: The value is in Operand2

Register direct: The value is in the register address specified in last 4 bits of Operand2

I-bit

1 - Immediate addressing

0 - Register direct


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="17" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**HALT: Opcode 111**

Halt. Halt all vector operations


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="26" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



### Float Processing: 3 bit opcode

**FMOV: Opcode 000**

Float Move. Operation copies the value of Rninto Rd. The ‘A’ bit specifies the addressing mode.


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="21" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FADD: Opcode 001**

Float Addition. Arithmetic addition operation for float scalar data types. Rn + Operand3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FSUB: Opcode 010**

Float Subtract. Arithmetic subtraction operation for float scalar data types Rn - Operand3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FRSUB: Opcode 011**

Float Reverse Subtract. Arithmetic subtraction operation using reverse subtraction algorithm for float scalar data types Rn reverse subtract Operand 3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FDIV: Opcode 100**

Float Divide. Arithmetic division operation for float scalar data types Rn / Operand 3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FMUL: Opcode 101**

Float Multiply. Arithmetic multiplication operation for float scalar data types Rn * Operand 3


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rm</code>
   </td>
   <td rowspan="2" colspan="19" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**FCMP: Opcode 110**

Float Compare. Comparison operator for 32-bit signed ints. Rn compared to Operand 2


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>S</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="21" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



### Load/Store: 3 bit opcode

**LDR: Opcode 000**

Load General. Load value into general register from memory. 


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="5" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rd: Destination Register
Operand 2: Memory Address or Register
```


**STR: Opcode 001**

Store General. Store value into memory from general register into memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="5" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rn: First Operand Register
Operand 2: Memory Address or Register
```


**LDRV: Opcode 010**

Load Vector. Load vector into vector register from memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="6" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
Rd: Destination Register
Operand 2: Register
```


**STRV: Opcode 011**

Store Vector. Store vector from vector register into memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="6" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
Rn: First Operand Register
Operand 2: Register
```


**LDRF: Opcode 100**

Load Float. Load float into float register from memory


<table>
  <tr>
   <td><code>3</code>
   </td>
   <td><code>3</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>2</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td><code>1</code>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="7" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rd: Destination Register
Operand 2: Memory Address or Register
```


**STRF: Opcode 101**

Store Float. Store float from float register into memory


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>I</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="7" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
I: Immediate bit
Rn: First Operand Register
Operand 2: Memory Address or Register
```



### Branch: 3 bit opcode

**BR: Opcode 000**

Branch. Loads a value into the PC register


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 2</code>
   </td>
   <td rowspan="2" colspan="6" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**BX: Opcode 001**

Branch Indirect. Loads a value into the PC register from a memory location held in another register


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="24" ><code>Operand 1</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>


**BC: Opcode 010**

Branch on Condition. Sets the program counter to a value iff the specified status bit is set to TRUE

**A:**

00 - Immediate

01 -  Register direct

10 - Register indirect

11 - PC + immediate


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>A</code>
   </td>
   <td rowspan="2" colspan="5" ><code>Operand 1</code>
   </td>
   <td rowspan="2" colspan="19" ><code>Operand 2</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



```
Operand 1: Bit number in status register to branch on
Operand 2: Address or register with address to branch to
```



#### **JMP: Opcode 011**

Jump. Stores the value in the PC register in the LR register and loads a value into the PC register from a memory location held in another register


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="18" ><code>Operand 3</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



### Register Transfer: 2 bit opcode


##### **FTOV: Opcode 00**

Float to Vector. Places a value from Rn in the Vector Rd at index of Offset


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Offset</code>
   </td>
   <td rowspan="2" colspan="5" ><code>X</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



##### **VTOF: Opcode 01**

Vector to Float. Places a value from Rd at index Operand 3 in Rn


<table>
  <tr>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
   <td><p style="text-align: right">
<code>9</code></p>

   </td>
   <td><p style="text-align: right">
<code>8</code></p>

   </td>
   <td><p style="text-align: right">
<code>7</code></p>

   </td>
   <td><p style="text-align: right">
<code>6</code></p>

   </td>
   <td><p style="text-align: right">
<code>5</code></p>

   </td>
   <td><p style="text-align: right">
<code>4</code></p>

   </td>
   <td><p style="text-align: right">
<code>3</code></p>

   </td>
   <td><p style="text-align: right">
<code>2</code></p>

   </td>
   <td><p style="text-align: right">
<code>1</code></p>

   </td>
   <td><p style="text-align: right">
<code>0</code></p>

   </td>
  </tr>
  <tr>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" ><code>0</code>
   </td>
   <td rowspan="2" ><code>1</code>
   </td>
   <td rowspan="2" colspan="2" ><code>Rn</code>
   </td>
   <td rowspan="2" colspan="4" ><code>Rd</code>
   </td>
   <td rowspan="2" colspan="16" ><code>Operand 3</code>
   </td>
   <td rowspan="2" colspan="5" ><code>Offset</code>
   </td>
  </tr>
  <tr>
  </tr>
</table>



# Work Division

The work has been divided in accordance with our strengths.  

**Manuel**: Memory (RAM and Cache), ALU instructions, Load instructions, Branching instructions, Pipeline stages (Decode, execute, memory, and writeback).

**Manav**: Memory (RAM and Cache), GUI for memory interpretation, GUI for memory settings, GUI for running through simulations, GUI for loading, storing, and writing instructions.

**Andrew: **Memory (RAM and Cache), ALU, Pipeline framework, fetching, Instruction Squashing, Register bank, Interpreter and assembler.


## Software Engineering Methods



* **Language:** Python 3
* **Team Organization: **Each team member took ownership of specific subsystems and files. Together the team would meet and decide which tasks needed to be completed before each major deadline, and break down what they planned to do for their subsystem and what needed to be done in other subsystems. Then at a planned date before a deadline the team would meet up to integrate changes, test the system as a whole, and debug where necessary.
* **Organizational Tools: **We used services like Slack and Discord to organize meetings, communicate changes, ask questions, and collaboratively work on the integration testing. Github Kanban was used for breaking up and keeping track of tasks that were being worked on.
* **Version Control:** GIT repositories were used locally, and Github was used for remote tracking.
* **Code Guidelines:** Used standard Python style for naming conventions, comments, and general program flow. Interfaces were documented using a consistent comment style to indicate the purpose, expected argument types, and the return type.


## Simulator

**How it works: **Custom assembly code is written which is later preprocessed, and interpreted into binary instructions which are then stored in memory. A “CORE” is initialized which has a memory(which includes main memory and caches), register banks, pipeline, and ALU associated with it. The pipeline fetches the instructions from memory which are sent to the decode stage. The decode stages decodes the instructions into Python dictionaries and extracts all values from the registers. At this stage, it records and checks for data dependencies in a dependency table. If there are no dependencies associated with this instruction, it packages the relevant data and sends the instruction to the execute state. The execute stage performs any necessary operations with help of the ALU, and packages the result into the instruction dictionary that is sent to the memory stage.The memory stage loads and stores values into memory if necessary, and sends the instruction forward to the writeback stage. And the writeback stage writes the result back into any registers passed by the instruction, and clears dependencies from the table. The pipeline stages ensure the system registers like the status registers and link register are updated accordingly in case of branching or comparisons. Meanwhile, the pipeline fetch updates the PC counter. Once an END instruction is processed by the execute stage, a flag is raised in the status register that indicates the program has terminated, and fetch will stop fetching instructions from memory.

**Writing Programs:** In order to write programs, there is an interpreter script located in the root directory named ‘asm_interpreter.py’. This script can be used to interpret a txt file containing assembly code, convert it into a txt file containing the program translated into integers representing binary, and finally create a json file which represents an empty memory with the program loaded in, starting from address 0. This same script also contains a utility for loading arrays of binary values into a memory json file, starting from a given starting address using a txt file with integer values representing binary for each desired value on a new line. The command format for using this script via the command line is as follows:

	

	**Interpret ASM to Memory:**

	asm_interpreter.py **int [ASM file location] [Desired name of binary and json]**

	**Load Array into Existing Memory:**

	asm_interpreter.py **arr [Mem File Location] [Array File Location] [Start Address]**

NOTE: The interpreter supports ASM programs written using tags for jumps and branches

where the tag is formatted as ‘[Tag Name]:’ on a line alone. This tag name can be used

in place of memory addresses or register numbers of a branch or jump instruction. The

interpreter also supports comments indicated by starting with ‘//’, and these lines will be

Ignored. Finally, the assembler supports use of acronyms for the status bits in comparison instructions. Refer to the [status register list] for the acronyms.

**Running Programs:** Once you have written a program and generated a memory file, you can start the User Interface by using the command line to run a script named ‘core.py’ in the root directory. The command format for running this script via the command line is as follows:

	

	**Running the Application GUI:**

	

	Core.py **[Mem File Location]**

This will launch a window that can be used for viewing or altering the state of the simulated machine at any given time, as well as for simulating cycles or running the loaded program to completion. The window is divided into five tabs: **Command Line, Memory, Registers, Diagnostic, and Pipeline**. The first tab you will see is the **Command Line** tab as shown below:



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


The command field is used for debug commands to manually send read or write requests to RAM, with the output from the command being displayed in the Output section. This tab was mainly used for GUI debugging, and is usually unimportant for running an application. The next tab is the **Memory** tab as shown below:



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


This tab shows the contents of the different levels of cache and the RAM. The label at the top indicates which level of memory is currently being viewed with it being an integer for cache level or RAM if main memory is being viewed instead. The level of cache being viewed can be changed by pressing the ‘Go up’ and ‘Go down’ buttons to navigate. The main window shows each line of cache or memory, with each word in hexadecimal format being separated by a space, as well as information such as the tag of the line being stored and the state of the valid bit. Even though tag and valid are present in RAM, they are not actually used. The text bar labeled ‘Go to address’ can be used to move the window to a specific memory location by inputting it into the text box and pressing ENTER. Finally, the checkboxes at the bottom labelled ‘Cache’ and ‘Pipeline’ are used to toggle whether or not the cache and the pipeline are used respectively. They both start as enabled by default. The next tab is the **Registers** tab as shown below:



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


This tab displays the contents of the various registers. The name of the register currently being viewed is the label at the top of the window, with registers being labelled as either a special register(PC, Status, LR, RET), or the type of register (General, Float, Vector) followed by the number of that particular register. The value or values contained in the register are shown in the box in the middle. The registers can be navigated using the ‘Previous’ and ‘Next’ buttons. The next tab is the **Diagnostic** tab as shown below:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


This tab is used to view the number of cycles run since the start of the machine and is used to continue the simulation. To run a specific number of cycles, type the number of cycles into the text box under the label ‘How many cycles to run’ and press ENTER. In order to have the simulation run to completion, press the button labeled ‘Run to completion’. The last tab is the **Pipeline** tab as shown below:



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


This tab is used to view the current state of the pipeline during execution. Each label represents a stage in the pipeline, and next to it is listed the instruction currently being held at that stage. This representation includes the control signals passed to each stage for each instruction.


## Benchmark Results

We ran three different benchmarks including: Exchange Sort, Matrix Multiply w/o Vectors, and Matrix Multiply with Vectors. Each was run on the following four settings: Pipeline and Cache(ppc), Cache only(c), Pipeline only(pp), and No Pipeline or Cache(n). All simulations were run with an L1 access time of 1 cycle, an L2 access time of 3 cycles, and a RAM access time of 100 cycles. The results of these benchmarks can be seen in the tables below:

**Exchange Sort: **Sorting 50 random integer values in memory


<table>
  <tr>
   <td><strong>Setting</strong>
   </td>
   <td><strong>Runtime(cycles)</strong>
   </td>
  </tr>
  <tr>
   <td>PPC
   </td>
   <td>170,673
   </td>
  </tr>
  <tr>
   <td>C
   </td>
   <td>205,826
   </td>
  </tr>
  <tr>
   <td>PP
   </td>
   <td>1,497,798
   </td>
  </tr>
  <tr>
   <td>N
   </td>
   <td>1,535,326
   </td>
  </tr>
</table>


**Matrix Multiply w/o Vectors: **Multiplying two 5x5 integer matrices in memory without using Vector instructions


<table>
  <tr>
   <td><strong>Setting</strong>
   </td>
   <td><strong>Runtime(cycles)</strong>
   </td>
  </tr>
  <tr>
   <td>PPC
   </td>
   <td>21,788
   </td>
  </tr>
  <tr>
   <td>C
   </td>
   <td>26,831
   </td>
  </tr>
  <tr>
   <td>PP
   </td>
   <td>217,227
   </td>
  </tr>
  <tr>
   <td>N
   </td>
   <td>224,231
   </td>
  </tr>
</table>


**Matrix Multiply with Vectors: **Multiplying two 5x5 float matrices in memory using Vector instructions


<table>
  <tr>
   <td><strong>Setting</strong>
   </td>
   <td><strong>Runtime(cycles)</strong>
   </td>
  </tr>
  <tr>
   <td>PPC
   </td>
   <td>7,771
   </td>
  </tr>
  <tr>
   <td>C
   </td>
   <td>7,856
   </td>
  </tr>
  <tr>
   <td>PP
   </td>
   <td>59,742
   </td>
  </tr>
  <tr>
   <td>N
   </td>
   <td>61,056
   </td>
  </tr>
</table>


**Results:** It seems from our simulations that in all three of the benchmarks, the speedup of cache is much more significant than the speedup from the pipeline. This is especially true for the Matrix Multiply with Vectors. The results also show that the matrix multiplication ran significantly faster using the Vector instructions than without with a max speedup of 3.67x for the No Cache or Pipeline condition, and an average speedup of 3.38x. It is also worth noting that because our Vectors are all float vectors, the vector arithmetic takes 3 cycles to compute rather than the 1 cycle computations with integers. The speedup we observe is in spite of the added cost of performing float calculations.


# What have we learned:

	There were many different concepts in the architecture of a processor that we got a greater understanding of from making this simulator. Some of the first things we learned had to do with the specifics regarding the memory subsystem. We already had some prior knowledge to the structure of data in caches and RAM due to experience in classes like CS230 and CS335, but there were several things that we gained a greater appreciation for. The first was the importance and surprising complexity of the address calculation step. This step is often brushed over in these classes as something that automatically happens, but we never had to do these steps ourselves. Secondly, we got a greater appreciation for how the almost recursive nature of the different levels of cache benefits a Write-Through cache. While not receiving the potential performance benefits of Write-Back, the simplicity of making a multi-level Write-Through proved to be a great advantage in terms of logic. Finally, while writing the memory subsystem we gained a greater appreciation for how long it actually takes to access memory in a program. Often it is something that is mentioned, but it is rather difficult to notice due to the speed of modern clocks. While writing the memory subsystem we noticed how much of a program’s execution time is spent in memory, even just to fetch instructions, and why a cache with large lines is extremely beneficial. This is also related to the pipeline and the various stages. Implementing the different stages improved the understanding of what each stage is responsible for, and how any single instruction is broken down into stages in order to take advantage of parallelism. Then getting each stage of the pipeline to work together concurrently proved to be a great challenge, and drove home the synchronization issues that arise from a deeply connected system like this. Finally, we learned about how different hazards in the pipeline can cause problems in program execution. We figured out how important it is to keep track of a dependency table for registers being used in the pipeline, and to stall the decode of instructions reading those registers. This small step in the pipeline proved to be crucial to ensuring the consistency and correctness of our programs. Lastly, we also learned about the difficulty of writing even a basic interpreter, and the importance of including quality-of-life features such as comments and tags. These seemingly unimportant features ended up being very helpful when writing actual programs such as the matrix multiplication.
