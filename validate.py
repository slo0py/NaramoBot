import csv
import os

file_path = 'trainingdata.csv'

def validate_file(file_path):
    valid = True
    issues = []

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        line_num = 1

        # Skip the header row
        header = next(reader, None)
        if header is not None:
            line_num += 1  # Adjust line counter

        for row in reader:
            if len(row) != 2:
                valid = False
                issues.append(f"Line {line_num}: Expected 2 columns, found {len(row)}.")
            else:
                heat, excess = row
                if not heat.strip().isdigit():
                    valid = False
                    issues.append(f"Line {line_num}: Heat '{heat}' is not a valid integer.")
                if not excess.strip().isdigit():
                    valid = False
                    issues.append(f"Line {line_num}: Excess '{excess}' is not a valid integer.")
            line_num += 1

    # Check if file ends with a newline
    with open(file_path, 'rb') as f:
        f.seek(-1, os.SEEK_END)
        last_char = f.read(1)
        if last_char != b'\n':
            valid = False
            issues.append("File does not end with a newline character.")

    if valid:
        print("Validation passed. The file is correctly formatted.")
    else:
        print("Validation failed. Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    
    return valid

if __name__ == '__main__':
    validate_file(file_path)
