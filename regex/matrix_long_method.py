#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
pointer = 0
accepted_values = []
arranged_values = []
transformed_values = []

for l in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

    # print("********* line number: ",l, "/",n-1)
    # print(">>> ", matrix_item)

    # ACCEPT VALUES
    for char in matrix_item:
        accepted_values.append(char)

    # after accpeting all, create a copy then ARRANGE

# print(accepted_values)
arranged_values = accepted_values.copy()

start = 0
for loc in range(n):
    # print(loc)
    if loc != 0:
        start = loc * m
    # print()
    pos = loc
    for letter in (accepted_values[start:start + m]):
        # print("insert: ", str(letter), "at:", pos)
        arranged_values.pop(pos)
        arranged_values.insert(pos, str(letter))
        pos += n

# print(arranged_values)

valid_symbols = ['!', '@', '#', '$', '%', '&', ' ']

# TRANSFORM
string1 = ""
for char in arranged_values:
    if char.isalnum or char in valid_symbols:
        string1 += char
# print(string1)

regex = '([ !@#$%&]{2})([aA-zZ0-9])'

sres = re.split(regex, string1)
# print(sres)
matches = re.findall(regex, string1)
# print(matches)
list_of_matches_to_replace = []

for g in matches:
    list_of_matches_to_replace.append(g[0])
# print(list_of_matches_to_replace)

for index, val in enumerate(sres):
    if val in list_of_matches_to_replace:
        sres.pop(index)
        sres.insert(index, " ")

final_string = ""
for v in sres:
    final_string += v

print(final_string)