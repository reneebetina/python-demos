#!/bin/python3
import sys

t = int(input("Test Count: ").strip())
try:
    if t < 1 or t > 100000:
        raise Exception("T error")
except Exception as e:
    print(e)
    sys.exit()

for a0 in range(t):
    n = int(input("Value {}: ".format(a0+1)).strip())
    try:
        if n < 10 or n > 40000000000000000:
            raise Exception("N error")
    except Exception as e:
        print(e)
        sys.exit()

    fibo = [1, 2]
    even_fibo = [2]
    pos = 0
    val = 0
    res = 2
    while val <= n:
        val = fibo[pos] + fibo[pos + 1]
        if val <= n:
            fibo.append(val)

        if val % 2 == 0 and val <= n:
            even_fibo.append(val)
            res += val
            # move to next fibo value
        pos += 1

    #    print("fibo: ",fibo)
    #    print("even_fibo: ",even_fibo)
    print(res)

# Input:
# 2
# 10
# 100
#
# Output:
# 10
# 44
