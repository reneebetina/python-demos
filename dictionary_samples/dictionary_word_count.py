#!/bin/python3
import sys

commands = []

for line in sys.stdin:
    commands.append(line)
    t = int(commands[0])

try:
    if t < 1 or t > 100000:
        raise Exception("T error")
except Exception as e:
    print(e)
    sys.exit()

words = {}
count = 0
for a in range(len(commands) - 1):
    wval = (str(commands[a + 1]).strip())

    if wval not in words:
        words[wval] = 1
    else:
        count = words[wval] + 1
        words[wval] = count

print(len(words))

for val in words.values():
    print(val, end=" ")

# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output
# 3
# 2 1 1