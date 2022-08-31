#!/usr/bin/env python3

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/" # use a URL that accepts files/images


#os_user = os.path.expanduser('~')
path = 'data/new_images/'
list_image = os.listdir(path)
jpeg_images = [image_name for image_name in list_image if '.jpg' in image_name]

for image in jpeg_images:
  with open(path + image, 'rb') as opened:
    r = requests.post(url, files={'file': opened})