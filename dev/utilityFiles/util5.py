#!/usr/bin/env python3

# extracts the image and the youtube links and inserts them into the JSON data


import csv
import json

csv_file_path_colors = 'colors_used.csv'
json_file_path_input = 'paintings_2.json'
json_file_path_output = 'paintings_3.json'


def parse_json_like_string(s):
    try:
        return json.loads(s.replace("'", '"'))
    except json.JSONDecodeError:
        return []

# Function to read the color CSV file and convert it to a list of color dictionaries
def read_colors_file(file_path):
    colors_list = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            num_colors = row.get('num_colors')
            colors = parse_json_like_string(row.get('colors', '[]'))
            color_hex = parse_json_like_string(row.get('color_hex', '[]'))
            color_info = [
                {"name": color_name.strip(), "hex": hex_code}
                for color_name, hex_code in zip(colors, color_hex)
            ]
            colors_list.append({
                'num_colors': int(num_colors),
                'colors': color_info
            })
    return colors_list

# Function to update the JSON data with color information
def update_json_with_colors(input_file, output_file, colors_list):
    try:
        with open(input_file, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        paintings = data.get('paintings', [])
        
        # Check if the number of color entries matches the number of paintings
        if len(paintings) != len(colors_list):
            raise ValueError("The number of paintings and color entries do not match.")

        # Update each painting with its corresponding color information
        for item, color_info in zip(paintings, colors_list):
            item.update(color_info)
        
        with open(output_file, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f'JSON data has been successfully updated with colors and saved to {output_file}.')
    except Exception as e:
        print(f"An error occurred: {e}")

# Read the colors CSV file
colors_list = read_colors_file(csv_file_path_colors)

# Update the existing JSON data with color information
update_json_with_colors(json_file_path_input, json_file_path_output, colors_list)
