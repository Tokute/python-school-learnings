# Code By: Ned Markus S. Basilio | CS-201

newline = lambda: output_file.write("\n")

def print_dict(given_dict, values_only=False):
    # Header row
    if not values_only:
        header_line = ", ".join(given_dict.keys())
        output_file.write(header_line)
        newline()

    cols = list(given_dict.values())
    num_cols = len(cols)
    num_rows = len(cols[0])
    #print(given_dict)

    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append(str(cols[j][i]))
        output_file.write(f"{', '.join(row)}")
        newline()

def add_info_to_dict(*values):  # IN ORDER: stud_id, full_name, prelim, midterm, finals
    if len(values) > len(stud_records):
        print("Error exceeded maximum number of data. 5 only.")
        print("IN ORDER: stud_id, full_name, prelim, midterm, finals")
        return

    for key, value in zip(stud_records.keys(), values):
        stud_records[key].append(value)
        
output_file = open("dict_output.txt", "w")
output_file.write("Code By: Ned Markus S. Basilio | CS-201")
newline()

stud_records = {
    "stud_id": [1234, 2354, 5715],
    "full_name": ["Harry Style", "Liam Payene", "Zyan Malik"],
    "prelim": [85, 89, 88],
    "midterm": [75, 72, 80],
    "finals": [85, 78, 83]
}

output_file.write("Created a dictionary named: stud_records:\n")
print_dict(stud_records)

newline()
output_file.write("1. Add a new student record with the given data.")
add_info_to_dict(2564, "Ariana Grande", 75, 85, 95) # IN ORDER: stud_id, full_name, prelim, midterm, finals

print_dict(stud_records)
newline()

output_file.write("2. Use input function to enter provided to the dictionary (use '-' to separate values).\n")
to_input = input("Enter values (use '-' to separate values): ").split("-") # 4030-Jessie James-90-85-75

for i in range(len(to_input)):
    if to_input[i].isnumeric():
        to_input[i] = int(to_input[i])

output_file.write(f"Values received: {to_input}\n")
add_info_to_dict(*to_input)

newline()
output_file.write("Updated Dictionary:\n")
print_dict(stud_records)

newline()
output_file.write("3. Modify/Update dictionary following given elements:\n")
output_file.write("1111, Simon Howel, 90, 80, 70 From 0:4 to 4:0 (bottom-left to top-right)\n")

for i, (key, value) in enumerate(zip(stud_records.keys(), [1111, "Simon Howell", 90, 80, 70]), start=1):
    stud_records[key][-i] = value
stud_records["full_name"][1] = "Niall"

newline()
output_file.write("Updated Dictionary:\n")
print_dict(stud_records)
newline()

newline()
output_file.write("4. Iterate through the dictionary and display only the values (lists of student inforamtion):\n")

newline()
print_dict(stud_records, values_only=True)

newline()
output_file.write("5. Remove the student information with the name \"Niall\".\n")
newline()

for i in range(len(stud_records["full_name"])):
    if stud_records['full_name'][i] == "Niall":
        index_to_remove = i
        break

for key in stud_records.keys():
    stud_records[key].pop(index_to_remove)

output_file.write("Updated Dictionary:\n")
print_dict(stud_records)
newline()

newline()
output_file.write("6. Remove the entire elements of 2345\n")
output_file.write("**Also removed in the 5th step\n")
newline()

output_file.write("Dictionary:\n")
print_dict(stud_records)

newline()
output_file.write("7. Add another key named average and compute for the average of all elements.")

averages = []
values_only = list(stud_records.values())
values_only = list(zip(*values_only)) # transpose to match table-form

#print(values_only)

for scores in values_only:
    averages.append(round(sum(scores[2:]) / len(scores[2:]), 3))

stud_records["average"] = list(averages)

newline()
output_file.write("Updated Dictionary:\n")
newline()
print_dict(stud_records)

newline()
output_file.write("8. Compute for the average of Prelim (column)\n")

#print(list(stud_records.values()))

prelim_scores = stud_records["prelim"]
prelim_average = sum(prelim_scores) / len(prelim_scores)

output_file.write(f"Prelim Average (column): {prelim_average:.3f}\n")

output_file.close()