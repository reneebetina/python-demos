#!/bin/python3
import sys

t = int(input("Input the desired length of your fibonacci series :  ").strip())
try:
    if t < 2 or t > 300:
        raise Exception("ERROR: Length must be greater than 1 or less than 300. If length is more than 300, computation will take long...")
except Exception as e:
    print(e)
    sys.exit()


fibo = [1,2]
pos = 0
val = 0
while len(fibo) < t:
    val = fibo[pos] + fibo[pos + 1]
    fibo.append(val)
    # move to next fibo value
    pos += 1

print("YOUR FIBONACCI SERIES:\n", fibo)

# Input: 10
# Output:
# [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Input: 20
# Output:
# [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]