# Input Format
# The first line contains an integer,N, denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.

# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


# Sample Output 0
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())

    mylist = []
    for i in range(N):
        line = input()
        command = line.split()
        operation = command[0]

        # Declare variables that will hold the values. You can declare as string or int
        # We will use str type to showcase type casting in the next lines
        x = ""
        y = ""
        # EXECUTE COMMANDS
        if operation.lower() == 'insert':
            x = command[1]
            y = command[2]
            mylist.insert(int(x), int(y))

        elif operation.lower() == 'remove' or operation.lower() == 'append':
            x = command[1]
            y = ""
            if operation.lower() == 'remove':
                mylist.remove(int(x))
                # print("output:", mylist)
            if operation.lower() == 'append':
                mylist.append(int(x))
        elif operation.lower() == 'print':
            print(mylist)
        elif operation.lower() == 'pop':
            mylist.pop()
        elif operation.lower() == 'sort':
            mylist.sort()
            # another approach
            # mylist = sorted(mylist)
        elif operation.lower() == 'reverse':
            mylist.reverse()