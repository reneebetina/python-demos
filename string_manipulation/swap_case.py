def swap_case(s):
    result=""
    for char in s:
        if char.islower():
            char = char.upper()
        else:
            char = char.lower()
        result += char
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)