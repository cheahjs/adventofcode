#!/usr/bin/python3

from typing import List
from enum import Enum
from collections import defaultdict
import sys
import term


paint_program = [3,8,1005,8,301,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,29,1,1103,7,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,54,2,103,3,10,2,1008,6,10,1006,0,38,2,1108,7,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,91,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,114,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,136,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,158,1,1009,0,10,2,1002,18,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,187,2,1108,6,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,213,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,236,1,104,10,10,1,1002,20,10,2,1008,9,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,269,1,102,15,10,1006,0,55,2,1107,15,10,101,1,9,9,1007,9,979,10,1005,10,15,99,109,623,104,0,104,1,21102,1,932700598932,1,21102,318,1,0,1105,1,422,21102,1,937150489384,1,21102,329,1,0,1105,1,422,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,46325083227,0,1,21102,376,1,0,1106,0,422,21102,3263269927,1,1,21101,387,0,0,1105,1,422,3,10,104,0,104,0,3,10,104,0,104,0,21102,988225102184,1,1,21101,410,0,0,1105,1,422,21101,868410356500,0,1,21102,1,421,0,1106,0,422,99,109,2,21202,-1,1,1,21102,1,40,2,21102,1,453,3,21102,1,443,0,1105,1,486,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,448,449,464,4,0,1001,448,1,448,108,4,448,10,1006,10,480,1102,1,0,448,109,-2,2106,0,0,0,109,4,1201,-1,0,485,1207,-3,0,10,1006,10,503,21101,0,0,-3,22101,0,-3,1,21201,-2,0,2,21102,1,1,3,21101,0,522,0,1105,1,527,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,550,2207,-4,-2,10,1006,10,550,22102,1,-4,-4,1105,1,618,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,569,1,0,1106,0,527,22101,0,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,588,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,610,21201,-1,0,1,21101,610,0,0,105,1,485,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
# paint_program = [3,100,104,1,104,0,3,100,104,0,104,0,3,100,104,1,104,0,3,100,104,1,104,0,3,100,104,0,104,1,3,100,104,1,104,0,3,100,104,1,104,0,99]

class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Op(Enum):
    ADDITION = 1
    MULTIPLICATION = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUAL = 8
    MODIFY_RELATIVE_BASE = 9
    HALT = 99


class Program:
    def __init__(self, memory):
        self.memory = defaultdict(int)
        for i in range(len(memory)):
            self.memory[i] = memory[i]
        self.program_counter = 0
        self.halted = False
        self.inputs = []
        self.relative_base = 0

    def read(self, mode: ParameterMode, pointer: int) -> int:
        if mode == ParameterMode.POSITION:
            return self.memory[self.memory[pointer]]
        elif mode == ParameterMode.IMMEDIATE:
            return self.memory[pointer]
        elif mode == ParameterMode.RELATIVE:
            return self.memory[self.relative_base+self.memory[pointer]]
        else:
            print('Encountered unknown mode', mode,
                  'at pos', pointer, self.memory)
            return None

    def write(self, mode: ParameterMode, pointer: int, value: int):
        if mode == ParameterMode.POSITION:
            self.memory[self.memory[pointer]] = value
        elif mode == ParameterMode.IMMEDIATE:
            print('IMMEDIATE WRITE NOT ALLOWED')
            return None
        elif mode == ParameterMode.RELATIVE:
            self.memory[self.relative_base+self.memory[pointer]] = value
        else:
            print('Encountered unknown mode', mode,
                  'at pos', pointer, self.memory)
            return None

    def add_input(self, inp: int):
        self.inputs.append(inp)

    def reset_input(self):
        self.inputs = []

    def has_halted(self) -> bool:
        return self.halted

    def run_program(self) -> int:
        if self.halted:
            return -999999
        while True:
            op: int = self.memory[self.program_counter]
            opcode: Op = Op(op % 100)

            if opcode == Op.ADDITION:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                parameter_2: int = self.read(ParameterMode(int(op//1000) % 10), self.program_counter+2)

                value = parameter_1 + parameter_2
                self.write(ParameterMode(int(op//10000) % 10), self.program_counter+3, value)
                self.program_counter += 4
            elif opcode == Op.MULTIPLICATION:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                parameter_2: int = self.read(ParameterMode(int(op//1000) % 10), self.program_counter+2)

                value = parameter_1 * parameter_2
                self.write(ParameterMode(int(op//10000) % 10), self.program_counter+3, value)
                self.program_counter += 4
            elif opcode == Op.INPUT:
                # inp = self.inputs.pop(0)
                inp = self.inputs[0]
                print('Reading input', inp)
                self.write(ParameterMode(int(op//100) % 10), self.program_counter+1, inp)
                self.program_counter += 2
            elif opcode == Op.OUTPUT:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                print('Output at pos', self.program_counter+1, ':', parameter_1)
                output = parameter_1
                self.program_counter += 2
                return output
            elif opcode == Op.JUMP_IF_TRUE:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                parameter_2: int = self.read(ParameterMode(int(op//1000) % 10), self.program_counter+2)
                if parameter_1 != 0:
                    self.program_counter = parameter_2
                else:
                    self.program_counter += 3
            elif opcode == Op.JUMP_IF_FALSE:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                parameter_2: int = self.read(ParameterMode(int(op//1000) % 10), self.program_counter+2)
                if parameter_1 == 0:
                    self.program_counter = parameter_2
                else:
                    self.program_counter += 3
            elif opcode == Op.LESS_THAN:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                parameter_2: int = self.read(ParameterMode(int(op//1000) % 10), self.program_counter+2)
                if parameter_1 < parameter_2:
                    self.write(ParameterMode(int(op//10000) % 10), self.program_counter+3, 1)
                else:
                    self.write(ParameterMode(int(op//10000) % 10), self.program_counter+3, 0)
                self.program_counter += 4
            elif opcode == Op.EQUAL:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                parameter_2: int = self.read(ParameterMode(int(op//1000) % 10), self.program_counter+2)
                if parameter_1 == parameter_2:
                    self.write(ParameterMode(int(op//10000) % 10), self.program_counter+3, 1)
                else:
                    self.write(ParameterMode(int(op//10000) % 10), self.program_counter+3, 0)
                self.program_counter += 4
            elif opcode == Op.MODIFY_RELATIVE_BASE:
                parameter_1: int = self.read(ParameterMode(int(op//100) % 10), self.program_counter+1)
                self.relative_base += parameter_1
                self.program_counter += 2
            elif opcode == Op.HALT:
                self.halted = True
                break
            else:
                print('Encountered unknown opcode: ', opcode)
                break

        # print('Final self.memory contents: ', self.memory)
        return -9999999


def paint(paint_map):
    term.clear()
    for pos, value in paint_map.items():
        term.pos(pos[0]+20, pos[1]+20)
        term.write('#' if value == 1 else ' ')

if __name__ == "__main__":
    loaded_program = paint_program

    # 0 = up
    # 1 = right
    # 2 = down
    # 3 = left
    direction = 0
    current_pos = [0,0]
    painted_map = {}


    program = Program(loaded_program[:])
    program.add_input(0)
    while True:
        paint_output = program.run_program()
        if program.has_halted():
            break

        turn_output = program.run_program()
        if program.has_halted():
            break

        pos = (current_pos[0], current_pos[1])
        painted_map[pos] = paint_output
        print('Painted', pos, 'with', paint_output)

        if turn_output == 0:
            # Left 90 degrees
            direction -= 1
            # print('turning left')
        else:
            # Right 90 degrees
            direction += 1
            # print('turning right')
        direction %= 4

        if direction == 0:
            # Up
            # print('Moving up')
            current_pos[1] += 1
        elif direction == 1:
            # Right
            # print('Moving right')
            current_pos[0] += 1
        elif direction == 2:
            # Down
            # print('Moving down')
            current_pos[1] -= 1
        elif direction == 3:
            # Left
            # print('Moving left')
            current_pos[0] -= 1
        
        pos = (current_pos[0], current_pos[1])
        current_color = 0 if pos not in painted_map else painted_map[pos]
        # print('Putting', current_color)
        program.reset_input()
        program.add_input(current_color)

    print(painted_map)
    print(len(painted_map))
    # paint(painted_map)
