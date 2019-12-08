#!/usr/bin/python3

from typing import List

program_1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
program_2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
program_3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
program_4 = [3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

def run_program(program_inputs: List[int], memory: List[int]):
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
    input_counter = 0
    output = None
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
            memory[parameter_1] = program_inputs[input_counter]
            # print('Inputting', program_inputs[input_counter])
            program_counter += 2
            input_counter += 1
        elif opcode == 4:
            # Output
            parameter_1: int = get_parameter(memory, parameter_modes, 0, program_counter+1, True)
            print('Output at pos', program_counter+1, ':', parameter_1)
            output = parameter_1
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
    return output

if __name__ == "__main__":
    loaded_program = program_4
    largest_signal = -1
    for phase_a in range(5):
        output_a = run_program([phase_a, 0], loaded_program[:])

        for phase_b in set(range(5)) - set([phase_a]):
            output_b = run_program([phase_b, output_a], loaded_program[:])

            for phase_c in set(range(5)) - set([phase_a, phase_b]):
                output_c = run_program([phase_c, output_b], loaded_program[:])

                for phase_d in set(range(5)) - set([phase_a, phase_b, phase_c]):
                    output_d = run_program([phase_d, output_c], loaded_program[:])

                    for phase_e in set(range(5)) - set([phase_a, phase_b, phase_c, phase_d]):
                        output_e = run_program([phase_e, output_d], loaded_program[:])

                        if output_e > largest_signal:
                            largest_signal = output_e
                            print('Signal', largest_signal, 'achieved with', [phase_a, phase_b, phase_c, phase_d, phase_e])
    print('Final signal:', largest_signal)