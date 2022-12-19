import sys
from xml.etree import ElementTree
import csv

res_line = {}
list_of_dictionaries_res_line = []
output = []

def read_xml(input_file_path):
    print("Reading XML...")
    tree = ElementTree.parse(input_file_path)
    root = tree.getroot()

    for food in root:
        id = food.find("id").text
        name = food.find("name").text
        price = food.find("price").text
        description = food.find("description").text
#        print(f"{id},{name},{price},{description}")
        # always reset res_line so new entry will not overwrite the existing
        res_line={}
        res_line["id"] = int(id)
        res_line["name"] = str(name)
        res_line["price"] = str(price)
        res_line["description"] = str(description).strip()
        list_of_dictionaries_res_line.append(res_line)

    #print(list_of_dictionaries_res_line)

    write_csv(list_of_dictionaries_res_line, 'process/data.csv', False)

def write_csv(data_dict, file_path, customHeader=False):
    try:
        #keys below will be the headers
        keys = ["id", "name", "price", "description"]
        custom_keys = ["name","description"]
        # Python 3 syntax in writing files, mode=w and newline='' are REQUIRED
        with open(file_path, mode='w', newline='') as wfile:
            if customHeader ==True:
                writer = csv.DictWriter(wfile, fieldnames=custom_keys)
                writer.writeheader()
            else:
                writer = csv.DictWriter(wfile,fieldnames=keys)
                writer.writeheader()

           # print("********[INFO] Now writing to csv ... ")
            # for debugging purposes you can check print all rows to be written using WRITEROWS
           # for pos in data_dict:
           #     print(pos)
            #dictwriter only accepts dictionary so make sure your list_of_dictionaries is correct and complete
            writer.writerows(data_dict)
           # print("********[INFO] Writing Complete!")
    except Exception as e :
        print("***Error encountered: ", e)
        sys.exit()

def extract_data(input_file_path, output_file_path):
    #get id and name
    print("********[INFO] EXTRACTING DATA ...")

    with open(input_file_path, mode='r', encoding='UTF-8') as file:
        file.__next__()
        for line in file.readlines():
            data = line.split(',')
            #print(data[0],data[1])
            extracted_data = {}
            #extracted_data["id"] = data[0]
            extracted_data["name"] = data[1].strip()
            extracted_data["description"] = data[3].strip()
            output.append(extracted_data)
        print(output)
    write_csv(output, output_file_path, True)

if __name__ == '__main__':
    # read file then transform to csv
    read_xml('input/foodmenu.xml')
    extract_data('process/data.csv','output/matches.csv')
    print("********[INFO] OUTPUT GENERATED")