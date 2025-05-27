import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python append_data.py input_file.csv")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = 'trainingdata.csv'

try:
    # Load existing data to check for duplicates
    existing_data = set()
    with open(output_file_path, 'r', newline='') as outfile:
        reader = csv.reader(outfile)
        next(reader, None)  # Skip header if it exists
        for row in reader:
            if row:  # Skip blank lines
                existing_data.add(tuple(row))

    with open(input_file_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        next(reader, None)  # Skip header

        new_rows = []
        for row in reader:
            if len(row) != 2 or not row[0] or not row[1]:
                print(f"Error: Invalid formatting in row: {row}")
                sys.exit(1)
            if tuple(row) in existing_data:
                print(f"Skipping duplicate row: {row}")
            else:
                new_rows.append(row)

    # Append new rows after validation
    with open(output_file_path, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        for row in new_rows:
            writer.writerow(row)
            print(f"Appended: {row}")

    print(f"All valid data from {input_file_path} has been appended to {output_file_path}.")

except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
