# You are given an immutable string, and you want to make changes to it.
# STRINGS - immutable
# LIST - mutable

# Input (stdin)
# abracadabra
# 5 k
#
# Expected Output
# abrackdabra

def mutate_string(string, position, character):
    myList = list(string)
    myList.pop(position)
    myList.insert(position, character)

    myString = ""
    for char in myList:
        myString += char

    return myString


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)