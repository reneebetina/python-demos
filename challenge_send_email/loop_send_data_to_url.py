import os
import requests

#BASEPATH_SUPPLIER_TEXT_DES = os.path.expanduser('~') + '/data/descriptions/'
BASEPATH_SUPPLIER_TEXT_DES = 'data/descriptions/'
list_text_files = os.listdir(BASEPATH_SUPPLIER_TEXT_DES)

#BASEPATH_SUPPLIER_IMAGE = os.path.expanduser('~') + '/data/new_images/'
BASEPATH_SUPPLIER_IMAGE = 'data/new_images/'
list_image_files = os.listdir(BASEPATH_SUPPLIER_IMAGE)
list_images = [image_name for image_name in list_image_files if '.jpg' in image_name]

list = []
for text_file in list_text_files:
    with open(BASEPATH_SUPPLIER_TEXT_DES + text_file, 'r') as f:
        data = {"name": f.readline().rstrip("\n"),
                "weight": int(f.readline().rstrip("\n").split(' ')[0]),
                "description": f.readline().rstrip("\n")}

        for image_file in list_images:
            if image_file.split('.')[0] in text_file.split('.')[0]:
                data['image_name'] = image_file

        list.append(data)

for item in list:
    resp = requests.post('https://run.mocky.io/v3/aad94fc1-6d77-4621-a808-429e1834730e', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    #print('Created feedback ID: {}'.format(resp.json()["id"]))
    else:
        print(item)
        print(resp.status_code)