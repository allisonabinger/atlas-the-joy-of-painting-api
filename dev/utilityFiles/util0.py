#!/usr/bin/env python3

# Contains utlity function to make episode_dates.txt into a readable csv file.
# Adds the title, air_date(MM/DD/YYYY), and special_guest
import csv
import re
from datetime import datetime


# date formatter
def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%B %d, %Y')
    return date_obj.strftime('%m/%d/%y')


# converts txt to csv
input_file = 'episode_dates.txt'
output_file = 'episode_dates.csv'

pattern = re.compile(r'^"(.+)" \((.+)\)(.*)?$')

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(["title", "air_date", "special_guest"])

    for line in infile:
        match = pattern.match(line.strip())
        if match:
            title = match.group(1)
            air_date = format_date(match.group(2))
            special_guest = match.group(3) if match.group(3) else 'None'
            csv_writer.writerow([title, air_date, special_guest])
