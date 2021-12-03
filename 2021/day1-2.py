
input = [int(l) for l in open('day1-1.txt').readlines()]

increase_count = 0
for i in range(3, len(input)):
    if input[i] > input[i-3]:
        increase_count += 1

print(increase_count)
