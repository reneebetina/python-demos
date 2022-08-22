import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# start
matrix = list(zip(*matrix))

string1 = ""

for words in matrix:
    for char in words:
        string1 += char

final_string = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', string1)
print(final_string)