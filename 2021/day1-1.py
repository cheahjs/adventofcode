
input = [int(l) for l in open('day1-1.txt').readlines()]

increase_count = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        increase_count += 1

print(increase_count)
