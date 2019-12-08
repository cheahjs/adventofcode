#!/usr/bin/python3

from typing import List

program_1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
program_2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
program_3 = [3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

class Program:
    def __init__(self, memory):
        self.memory = memory
        self.program_counter = 0
        self.halted = False
        self.inputs = []
        self.input_counter = 0
    
    def get_parameter(self, raw_mode: int, parameter_index: int, pointer: int, indirect: bool):
        mode: int = int(raw_mode / (10**parameter_index)) % 10
        if mode == 0:
            if indirect:
                return self.memory[self.memory[pointer]]
            else:
                return self.memory[pointer]
        elif mode == 1:
            return self.memory[pointer]
        else:
            print('Encountered unknown mode', mode, 'at pos', pointer, self.memory)
            return None

    def add_input(self, inp):
        self.inputs.append(inp)

    def has_halted(self):
        return self.halted

    def run_program(self):
        if self.halted:
            return (None, True)
        while True:
            op: int = self.memory[self.program_counter]
            opcode: int = op % 100
            parameter_modes: int = int(op / 100)
            if opcode == 1:
                # Addition
                parameter_1: int = self.get_parameter(parameter_modes, 0, self.program_counter+1, True)
                parameter_2: int = self.get_parameter(parameter_modes, 1, self.program_counter+2, True)
                store_location: int = self.get_parameter(parameter_modes, 2, self.program_counter+3, False)
                value = parameter_1 + parameter_2
                self.memory[store_location] = value
                self.program_counter += 4
            elif opcode == 2:
                # Multiplication
                parameter_1: int = self.get_parameter(parameter_modes, 0, self.program_counter+1, True)
                parameter_2: int = self.get_parameter(parameter_modes, 1, self.program_counter+2, True)
                store_location: int = self.get_parameter(parameter_modes, 2, self.program_counter+3, False)
                value = parameter_1 * parameter_2
                self.memory[store_location] = value
                self.program_counter += 4
            elif opcode == 3:
                # Input
                parameter_1: int = self.memory[self.program_counter+1]
                self.memory[parameter_1] = self.inputs[self.input_counter]
                self.program_counter += 2
                self.input_counter += 1
            elif opcode == 4:
                # Output
                parameter_1: int = self.get_parameter(parameter_modes, 0, self.program_counter+1, True)
                print('Output at pos', self.program_counter+1, ':', parameter_1)
                output = parameter_1
                self.program_counter += 2
                return output
            elif opcode == 5:
                # Jump if true
                parameter_1: int = self.get_parameter(parameter_modes, 0, self.program_counter+1, True)
                parameter_2: int = self.get_parameter(parameter_modes, 1, self.program_counter+2, True)
                if parameter_1 != 0:
                    self.program_counter = parameter_2
                else:
                    self.program_counter += 3
            elif opcode == 6:
                # Jump if false
                parameter_1: int = self.get_parameter(parameter_modes, 0, self.program_counter+1, True)
                parameter_2: int = self.get_parameter(parameter_modes, 1, self.program_counter+2, True)
                if parameter_1 == 0:
                    self.program_counter = parameter_2
                else:
                    self.program_counter += 3
            elif opcode == 7:
                # Less than
                parameter_1: int = self.get_parameter(parameter_modes, 0, self.program_counter+1, True)
                parameter_2: int = self.get_parameter(parameter_modes, 1, self.program_counter+2, True)
                store_location: int = self.get_parameter(parameter_modes, 2, self.program_counter+3, False)
                if parameter_1 < parameter_2:
                    self.memory[store_location] = 1
                else:
                    self.memory[store_location] = 0
                self.program_counter += 4
            elif opcode == 8:
                # Equal
                parameter_1: int = self.get_parameter(parameter_modes, 0, self.program_counter+1, True)
                parameter_2: int = self.get_parameter(parameter_modes, 1, self.program_counter+2, True)
                store_location: int = self.get_parameter(parameter_modes, 2, self.program_counter+3, False)
                if parameter_1 == parameter_2:
                    self.memory[store_location] = 1
                else:
                    self.memory[store_location] = 0
                self.program_counter += 4
            elif opcode == 99:
                # Halt
                self.halted = True
                break
            else:
                print('Encountered unknown opcode: ', opcode)
                break
        print('Final self.memory contents: ', self.memory)
        return None

if __name__ == "__main__":
    loaded_program = program_3
    largest_signal = -1

    for phase_a in range(5, 10):
        for phase_b in set(range(5, 10)) - set([phase_a]):
            for phase_c in set(range(5, 10)) - set([phase_a, phase_b]):
                for phase_d in set(range(5, 10)) - set([phase_a, phase_b, phase_c]):
                    for phase_e in set(range(5, 10)) - set([phase_a, phase_b, phase_c, phase_d]):
                        print([phase_a, phase_b, phase_c, phase_d, phase_e])
                        output_e = 0

                        amp_a = Program(loaded_program[:])
                        amp_b = Program(loaded_program[:])
                        amp_c = Program(loaded_program[:])
                        amp_d = Program(loaded_program[:])
                        amp_e = Program(loaded_program[:])

                        amp_a.add_input(phase_a)
                        amp_b.add_input(phase_b)
                        amp_c.add_input(phase_c)
                        amp_d.add_input(phase_d)
                        amp_e.add_input(phase_e)
                        while True:
                            amp_a.add_input(output_e)
                            output_a = amp_a.run_program()
                            if amp_a.has_halted():
                                break
                            amp_b.add_input(output_a)
                            output_b = amp_b.run_program()
                            if amp_b.has_halted():
                                break
                            amp_c.add_input(output_b)
                            output_c = amp_c.run_program()
                            if amp_c.has_halted():
                                break
                            amp_d.add_input(output_c)
                            output_d = amp_d.run_program()
                            if amp_d.has_halted():
                                break
                            amp_e.add_input(output_d)
                            output_e = amp_e.run_program()
                            if amp_e.has_halted():
                                break

                            if output_e > largest_signal:
                                largest_signal = output_e
                                print('Signal', largest_signal, 'achieved with', [phase_a, phase_b, phase_c, phase_d, phase_e])
    print('Largest signal:', largest_signal)
