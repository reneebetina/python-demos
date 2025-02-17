# Input (stdin)
# Hello this is my string

# Your Output (stdout)
# gnirts ym si siht olleH

def string_reverse(line):
    # write your code here
    # i have used slicing method here
    # slicing concept can be done with lists or strings
    # SYNTAX is [start:stop:step]
    return str(line[::-1])


if __name__ == '__main__':
    print("##################################################################")
    print("Enter a string to reverse: ")
    line = input()
    result = string_reverse(line)
    print(result)