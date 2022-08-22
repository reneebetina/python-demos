import sys
import csv

def check_type(a,b,c):
    res =""
    if (a==b and b==c and c==a): res="Equilateral"
    elif ( a+b>c and (a==b and a!=c)or(a==c and b!=c)or(b==c and a!=b) ): res="Isosceles"
    elif ( a+b>=c and (a!=b and a!=c and b!=c) ): res= "Scalene"
    else: res="Not A Triangle"
    return res

if __name__ == '__main__':
    # read text file
    # for every line, get a, b, c
    a = 1
    b = 1
    c = 1
    res_string = ""
    res_line = {}
    list_of_dictionaries_res_line = []
    with open('test_data/triangle.txt', mode='r', encoding='UTF-8') as file:
        for line in file.readlines():
            list_num = line.split(' ')
            #print(list_num)
            a = list_num[0]
            b = list_num[1]
            c = list_num[2].replace("\n","")
            # pass type to function
            triangle_type = check_type(a,b,c)

            #res_string = "{},{},{},{}".format(a,b,c,triangle_type)
            #print(res_string)
            #string is ok but dictionary is better in writing csvs with unique headers

            res_line["a"] = int(a)
            res_line["b"] = int(b)
            res_line["c"] = int(c)
            res_line["triangle_type"] = str(triangle_type).strip()

            list_of_dictionaries_res_line.append(res_line)
            # always reset res_line so new entry will not overwrite the existing

            res_line={}
        print(list_of_dictionaries_res_line)
    try:
        if len(list_of_dictionaries_res_line)==0:
            raise Exception("Custom ERROR - nothing to write ", sys.stderr)

        #declare keys aligned to exact keys you used in your dictionary
        keys = ["a","b","c","triangle_type"]
        # Python 3 syntax in writing files, mode=w and newline='' are REQUIRED
        with open('output/triangle_res.csv', mode='w', newline='') as wfile:
            writer = csv.DictWriter(wfile,fieldnames=keys)
            print("INFO: Now writing to csv ... ")
            writer.writeheader()
            # for debugging purposes you can check print all rows to be written using WRITEROWS
            for pos in list_of_dictionaries_res_line:
                print(pos)
            #dictwriter only accepts dictionary so make sure your list_of_dictionaries is correct and complete
            writer.writerows(list_of_dictionaries_res_line)
            print("INFO: Writing Complete!")
    except Exception as e :
        print("***Error encountered: ", e)
        sys.exit()

# EXPECTED OUTPUT
# 10 10 10 : Equilateral
# 11 11 11 : Equilateral
# 30 32 30 : Isosceles
# 40 40 40 : Equilateral
# 20 20 21 : Not A Triangle
# 21 21 21 : Equilateral
# 20 22 21 : Not A Triangle
# 20 20 40 : Not A Triangle
# 20 22 21 : Not A Triangle
# 30 32 41 : Not A Triangle
# 50 22 51 : Not A Triangle
# 20 12 61 : Not A Triangle
# 20 22 50 : Not A Triangle
# 50 52 51 : Not A Triangle
# 80 80 80 : Equilateral