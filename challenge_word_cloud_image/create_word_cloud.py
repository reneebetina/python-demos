#! /usr/bin/env python3

import os
import csv

import wordcloud  # pip install wordcloud will auto install numpy, matplotlib
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

description_path = 'data/descriptions/'
list_files = os.listdir(description_path)

req_list = []
#PROCESS DESCRIPTION
for file in list_files:
        #print("text_file = ", str(file))
        with open(description_path + file, 'r') as f:
                csv_f = csv.reader(f)
                header = csv_f.__next__() # to ignore header line and proceed to row 1
                for row in csv_f:
                        req_list.append(row)
        #print("=============================================================================")
print("successfully opened: ", len(req_list), " lines")

#count person per country
dictionary_of_countries = {}
for person in req_list:
        country_name = person[6]

        if country_name not in dictionary_of_countries:
                dictionary_of_countries[country_name]=1
        else:
                current_count = dictionary_of_countries[country_name]
                dictionary_of_countries[country_name] = current_count + 1

#wordcloud
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(dictionary_of_countries)

myimage = cloud.to_array()
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

#uniquefilename

current_time = datetime.now()
time_stamp = current_time.timestamp()
print("timestamp:-", time_stamp)

date_time = datetime.fromtimestamp(time_stamp)
str_date = date_time.strftime("%B %d %Y %I%p %H_%M_%S")
print("Date", str_date)

filename = str_date +'.pdf'
plt.imsave(filename,myimage)