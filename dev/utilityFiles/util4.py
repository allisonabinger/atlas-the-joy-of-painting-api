#!/usr/bin/env python3

# extracts the image and the youtube links and inserts them into the JSON data


import csv
import json

csv_file_path = 'colors_used.csv'
json_file_path_input = 'paintings_1.json'
json_file_path_output = 'paintings_2.json'

def read_data_file(file_path):
    data_list = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append({
                'imageURL': row['img_src'],
                'videoURL': row['youtube_src']
            })
    return data_list


def update_json_with_data(input_file, output_file, data_list):
    with open(input_file, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    paintings = data.get('paintings', [])

    if len(paintings) != len(data_list):
        raise ValueError("The number fo rows in the csv file don't match")
    
    for i, item in enumerate(paintings):
        item.update(data_list[i])
    
    with open(output_file, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


data_list = read_data_file(csv_file_path)


update_json_with_data(json_file_path_input, json_file_path_output, data_list)
