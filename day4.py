#!/usr/bin/python3

# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?

# Your puzzle input is 171309-643603.

# First value: 177777
# Last value: 639999

def check_password_match(password: str):
    double = False
    last_digit = 0
    for char in password:
        digit = int(char)
        if last_digit == digit:
            double = True
        if digit < last_digit:
            return False
        last_digit = digit
    return double

if __name__ == "__main__":
    count = 0
    for password in range(171309, 643603):
        match = check_password_match(str(password))
        if match:
            count += 1
    print(count)