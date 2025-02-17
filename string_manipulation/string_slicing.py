#Enter any word:
#powerpoint
#** String Length is  10
#** First character is index 0
#** Last character is index  9
##################################################################
#Enter START of slice:
#1
#Enter END of slice:
#8
#Enter STEP to take after every slice:
#2
#OUTPUT: oepi

def string_slice(line,start,stop,step):
    # write your code here
    # i have used slicing method here
    # slicing concept can be done with lists or strings
    # SYNTAX is [start:stop:step]

    return str(line[start:stop:step])


if __name__ == '__main__':
    print("##################################################################")
    print("Enter any word: ")
    line = input()
    lineLength = len(line)
    lastIndex = int(lineLength)-1
    print("** String Length is ", lineLength)
    print("** First character is index 0")
    print("** Last character is index ", str(lastIndex))
    print("##################################################################")
    print("Enter START of slice: ")
    start = int(input())
    print("Enter END of slice: ")
    stop = int(input())
    print("Enter STEP to take after every slice: ")
    step = int(input())

    result = string_slice(line,start,stop,step)
    print("OUTPUT: " + result)
