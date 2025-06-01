import csv

while True:
    try:
        heatinput = int(input("Enter Heat (1500-4000): "))
        if 1500 <= heatinput <= 4000:
            break
        else:
            print("Heat out of range. Please enter a value between 1500 and 4000.")
    except ValueError:
        print("Invalid Heat input. Please enter an integer.")

def get_excess_input():
    excess_values = []
    print("Enter Excess values at *stable Heat* (press Enter without typing to finish):")
    while True:
        excess_input = input("Excess: ").strip()
        if excess_input == "":
            break
        try:
            excess_value = int(excess_input)
            excess_values.append(excess_value)
        except ValueError:
            print("Invalid excess value. Please enter an integer.")
    
    if len(excess_values) == 0:
        print("No valid Excess values entered. Defaulting to 0.")
        return 0
    
    mean_excess = sum(excess_values) / len(excess_values)
    print(f"Using mean Excess value: {mean_excess:.2f}")
    return round(mean_excess)

excessinput = get_excess_input()

new_row = [heatinput, excessinput]
    
new_row = [heatinput, excessinput]

with open('trainingdata.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(new_row)


# with open('trainingdata.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     #next(csv_reader) #skips fields 

#     for line in csv_reader:
#         print(line)