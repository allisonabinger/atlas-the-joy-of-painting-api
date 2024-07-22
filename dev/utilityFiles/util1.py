#!/usr/bin/env python3

# Contains utlity function to add the episodeID
import csv

# File paths
destination_csv_file = 'episode_dates.csv'  # The CSV file with title, air_date, special_guest
source_csv_file = 'subject_matter.csv'  # The additional CSV file with EPISODE and TITLE columns
final_output_csv_file = 'paintings.csv'



# Read the EPISODE column from the source CSV file
episode_data = []
with open(source_csv_file, 'r') as source_file:
    source_reader = csv.DictReader(source_file)
    for row in source_reader:
        episode_data.append(row['EPISODE'])

# Read the destination CSV file and write EPISODE column to it
with open(destination_csv_file, 'r') as dest_file, open(final_output_csv_file, 'w', newline='') as final_file:
    dest_reader = csv.DictReader(dest_file)
    fieldnames = dest_reader.fieldnames + ['EPISODE']
    final_writer = csv.DictWriter(final_file, fieldnames=fieldnames)
    
    final_writer.writeheader()
    
    for i, row in enumerate(dest_reader):
        if i < len(episode_data):
            row['EPISODE'] = episode_data[i]
        else:
            row['EPISODE'] = 'Unknown'
        final_writer.writerow(row)
