#!/usr/bin/python3

from typing import List


def run_program(memory: List[int]):
    program_counter = 0
    while True:
        op: int = memory[program_counter]
        if op == 1:
            # Addition
            operand_1: int = memory[memory[program_counter+1]]
            operand_2: int = memory[memory[program_counter+2]]
            store_location: int = memory[program_counter+3]
            value = operand_1 + operand_2
            memory[store_location] = value
            program_counter += 4
        elif op == 2:
            # Multiplication
            operand_1: int = memory[memory[program_counter+1]]
            operand_2: int = memory[memory[program_counter+2]]
            store_location: int = memory[program_counter+3]
            value = operand_1 * operand_2
            memory[store_location] = value
            program_counter += 4
        elif op == 99:
            # Halt
            break
        else:
            print('Encountered unknown opcode: ', op)
            break


def brute_force():
    initial_program_state: List[int] = [1, 999, 999, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 10, 19, 23, 1, 23, 9, 27, 1, 5, 27, 31, 2, 31, 13, 35, 1, 35, 5, 39, 1, 39, 5, 43, 2, 13, 43, 47, 2, 47, 10, 51, 1, 51, 6, 55, 2, 55, 9, 59, 1, 59, 5, 63, 1, 63, 13, 67, 2, 67, 6, 71, 1, 71, 5, 75, 1, 75, 5, 79, 1, 79, 9, 83, 1, 10, 83, 87, 1, 87, 10, 91, 1, 91, 9, 95, 1, 10, 95, 99, 1, 10, 99, 103, 2, 103, 10, 107, 1, 107, 9, 111, 2, 6, 111, 115, 1, 5, 115, 119, 2, 119, 13, 123, 1, 6, 123, 127, 2, 9, 127, 131, 1, 131, 5, 135, 1, 135, 13, 139, 1, 139, 10, 143, 1, 2, 143, 147, 1, 147, 10, 0, 99, 2, 0, 14, 0]
    for noun in range(100):
        for verb in range(100):
            copy_state: List[int] = initial_program_state[:]
            copy_state[1] = noun
            copy_state[2] = verb
            run_program(copy_state)
            end_result = copy_state[0]
            if end_result == 19690720:
                print('Correct result: Noun', noun, 'and verb', verb)
                print('100 * noun + verb =', 100 * noun + verb)
                return
            else:
                print('Wrong result: Noun', noun, 'and verb',
                      verb, 'produce:', end_result)


if __name__ == "__main__":
    brute_force()
