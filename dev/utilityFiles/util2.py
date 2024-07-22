#!/usr/bin/env python3

# Converts exists paintings.csv into JSON objects


import csv
import json


csv_file_path = 'paintings.csv'
json_file_path = 'paintings.json'

data_list = []

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    id_counter = 1

    for row in csv_reader:
        item = {
            'id': id_counter,
            'title': row['title'],
            'air_date': row['air_date'],
            'special_guest': row['special_guest'] if row['special_guest'] else 'None',
            'episode': row['episode']
        }
        data_list.append(item)
        id_counter +=1

with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump({'paintings': data_list}, json_file, indent=4)
