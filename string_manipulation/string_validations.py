if __name__ == '__main__':
    s = input()
    alnum_flag = False
    alpha_flag = False
    digit_flag = False
    lower_flag = False
    upper_flag = False
    # check if any char will meet condition
    for char in s:
        if char.isalnum():
            alnum_flag = True
        if char.isalpha():
            alpha_flag = True
        if char.isdigit():
            digit_flag = True
        if char.islower():
            lower_flag = True
        if char.isupper():
            upper_flag = True

    print(alnum_flag)
    print(alpha_flag)
    print(digit_flag)
    print(lower_flag)
    print(upper_flag)



# Input
# qA2

# Output
# True
# True
# True
# True
# True