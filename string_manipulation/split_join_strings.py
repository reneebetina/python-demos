# Input (stdin)
# this is a string

# Your Output (stdout)
# this-is-a-string

def split_and_join(line):
    # write your code here
    myList = []
    myList = line.split(" ")
    # print(myList)

    # join elements with a "-"
    myList = "-".join(myList)

    return str(myList)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)