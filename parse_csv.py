import csv

while True:
    try:
        heatinput = int(input("Enter Heat (1500–4000): "))
        if 1500 <= heatinput <= 4000:
            break
        else:
            print("Heat out of range. Please enter a value between 1500 and 4000.")
    except ValueError:
        print("Invalid Heat input. Please enter an integer.")

while True:
    try:
        excessinput = int(input("Enter Excess (14000–30000): "))
        if 14000 <= excessinput <= 30000:
            break
        else:
            print("Excess out of range. Please enter a value between 14000 and 30000.")
    except ValueError:
        print("Invalid Excess input. Please enter an integer.")

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