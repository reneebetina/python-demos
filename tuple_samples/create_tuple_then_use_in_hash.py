# Input Format
# The first line contains an integer,n, denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .
#
# Output Format
# Print the result of hash(tuple)

# Sample Input 0
# 2
# 1 2

# Sample Output 0
# 3713081631934410656

if __name__ == '__main__':
    # accept 1st line
    n = int(input())
    # accept 2nd line
    integer_list = map(int, input().split())

    # transform list to a tuple object
    myTuple = tuple(integer_list)

    print(hash(myTuple))