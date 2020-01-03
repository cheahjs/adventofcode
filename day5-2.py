#!/usr/bin/python3

from typing import List

def run_program(program_input: int, memory: List[int]):
    def get_parameter(memory: List[int], raw_mode: int, parameter_index: int, pointer: int, indirect: bool):
        mode: int = int(raw_mode / (10**parameter_index)) % 10
        if mode == 0:
            if indirect:
                return memory[memory[pointer]]
            else:
                return memory[pointer]
        elif mode == 1:
            return memory[pointer]
        else:
            print('Encountered unknown mode', mode, 'at pos', pointer, memory)
            return None

    program_counter = 0
    while True:
        op: int = memory[program_counter]
        opcode: int = op % 100
        parameter_modes: int = int(op / 100)
        if opcode == 1:
            # Addition
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            parameter_2: int = get_parameter(memory, parameter_modes, 1, program_counter+2, True)
            store_location: int = get_parameter(memory, parameter_modes, 2, program_counter+3, False)
            value = parameter_1 + parameter_2
            memory[store_location] = value
            # print('Executing addition', memory[program_counter:program_counter+4])
            # print(parameter_1, parameter_2, value, store_location)
            program_counter += 4
        elif opcode == 2:
            # Multiplication
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            parameter_2: int = get_parameter(memory, parameter_modes, 1, program_counter+2, True)
            store_location: int = get_parameter(memory, parameter_modes, 2, program_counter+3, False)
            value = parameter_1 * parameter_2
            memory[store_location] = value
            # print(parameter_1, parameter_2, value, store_location)
            program_counter += 4
        elif opcode == 3:
            # Input
            parameter_1: int = memory[program_counter+1]
            memory[parameter_1] = program_input
            program_counter += 2
        elif opcode == 4:
            # Output
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            print('Output at pos', program_counter+1, ':', parameter_1)
            program_counter += 2
        elif opcode == 5:
            # Jump if true
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            parameter_2: int = get_parameter(memory, parameter_modes, 1, program_counter+2, True)
            if parameter_1 != 0:
                program_counter = parameter_2
            else:
                program_counter += 3
        elif opcode == 6:
            # Jump if false
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            parameter_2: int = get_parameter(memory, parameter_modes, 1, program_counter+2, True)
            if parameter_1 == 0:
                program_counter = parameter_2
            else:
                program_counter += 3
        elif opcode == 7:
            # Less than
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            parameter_2: int = get_parameter(memory, parameter_modes, 1, program_counter+2, True)
            store_location: int = get_parameter(memory, parameter_modes, 2, program_counter+3, False)
            if parameter_1 < parameter_2:
                memory[store_location] = 1
            else:
                memory[store_location] = 0
            program_counter += 4
        elif opcode == 8:
            # Equal
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            parameter_2: int = get_parameter(memory, parameter_modes, 1, program_counter+2, True)
            store_location: int = get_parameter(memory, parameter_modes, 2, program_counter+3, False)
            if parameter_1 == parameter_2:
                memory[store_location] = 1
            else:
                memory[store_location] = 0
            program_counter += 4
        elif opcode == 99:
            # Halt
            break
        else:
            print('Encountered unknown opcode: ', opcode)
            break
    print('Final memory contents: ', memory)

if __name__ == "__main__":
    # run_program(8, [3,3,1108,-1,8,3,4,3,99])
    # run_program(7, [3,3,1108,-1,8,3,4,3,99])
    # run_program(8, [3,3,1107,-1,8,3,4,3,99])
    # run_program(9, [3,3,1107,-1,8,3,4,3,99])
    # run_program(7, [3,3,1107,-1,8,3,4,3,99])
    # run_program(1, [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
    # run_program(1, [3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
    # run_program(7, [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    # run_program(8, [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    # run_program(9, [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    # run_program(10, [1002,4,3,4,33])
    # run_program(0, [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0])
    run_program(5, [3,225,1,225,6,6,1100,1,238,225,104,0,1101,9,90,224,1001,224,-99,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,26,62,225,1101,11,75,225,1101,90,43,225,2,70,35,224,101,-1716,224,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1101,94,66,225,1102,65,89,225,101,53,144,224,101,-134,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,16,32,224,101,-512,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1001,43,57,224,101,-147,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,36,81,225,1002,39,9,224,1001,224,-99,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1,213,218,224,1001,224,-98,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,102,21,74,224,101,-1869,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,25,15,225,1101,64,73,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,434,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,479,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,524,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1107,677,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,584,101,1,223,223,1108,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,614,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,629,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,644,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226])
