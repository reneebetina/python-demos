def count_substring(string, sub_string):
    count = 0
    # 1. slice the original string by 3 or len(sub_string)
    # 2. if slice == substring : count as 1 match
    # 3. move to the next index and repeat step 1 (slice then find)
    for index, char in enumerate(string):
        my_slice = string[index:index + len(sub_string)]

        if my_slice == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# Input (stdin)
# ABCDCDC
# CDC

# Expected Output
# 2