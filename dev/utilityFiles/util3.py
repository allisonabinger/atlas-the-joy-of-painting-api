#!/usr/bin/env python3

# Converts subjects into JSON data and inserts into paintings.json


import csv
import json

csv_file_path_subjects = 'subject_matter.csv'
json_file_path_input = 'paintings_0.json'
json_file_path_output = 'paintings_1.json'


def format_subject_name(name):
    # replaces _ with a space and only capitalize the first letter
    name_with_spaces = name.replace('_', ' ')
    return name_with_spaces.title()


def read_subjects_file(file_path):
    subjects_dict = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            episode = row['EPISODE']
            # include only subjects with value 1 and format the subject names
            subjects = {format_subject_name(k): "present" for k, v in row.items() if k not in ('EPISODE', 'TITLE') and v == '1'}
            subjects_dict[episode] = subjects
    return subjects_dict


def update_json_with_subjects(input_file, output_file, subjects_dict):
    with open(input_file, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for item in data.get('paintings', []):
        episode = item.get('episode')
        if episode in subjects_dict:
            item['subjects'] = subjects_dict[episode]

    with open(output_file, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


subjects_dict = read_subjects_file(csv_file_path_subjects)

update_json_with_subjects(json_file_path_input, json_file_path_output, subjects_dict)
