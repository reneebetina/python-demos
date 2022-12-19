def main():
    try:
        random_numbers_file = open('numbers.txt', 'r')
        total = 0.0
        count = 0
        for line in random_numbers_file:
            number = float(line)
            count += 1
            total += number
        average = total / count
        print("Average:", format(average, '.2f'))
    except Exception as e:
        print(e)
        print("ERROR ENCOUNTERED: File is not found or value is non-numeric")

main()