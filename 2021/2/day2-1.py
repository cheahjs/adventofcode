
FORWARD="forward"
DOWN="down"
UP="up"

def parse(line):
    parts = line.split(' ')
    return (parts[0], int(parts[1]))

input = [parse(l) for l in open('day2-1.txt').readlines()]

pos = 0
depth = 0

for (action, amount) in input:
    if action == FORWARD:
        pos += amount
    elif action == UP:
        depth -= amount
    elif action == DOWN:
        depth += amount
    else:
        print(f"Unknown action: {action} {amount}")
        exit(2)

print(f"Postion: {pos}\tDepth: {depth}\tMultiple: {pos*depth}")
