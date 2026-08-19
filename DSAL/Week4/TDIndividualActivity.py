# Ned Markus S. Basilio | CS-201
tda = [
    [2, 6, 8, 1, 4, 3],
    [3, 6, 4, 5, 7, 1],
    [9, 3, 6, 4, 8, 5],
    [3, 6, 5, 8, 7, 5],
    [3, 6, 7, 4, 3, 5]
]

tdb = [
    [9, 5, 1, 7, 5, 3],
    [6, 8, 2, 1, 3, 4],
    [6, 9, 4, 3, 2, 1],
    [6, 2, 5, 4, 6, 3],
    [3, 3, 3, 3, 5, 3]
]

newline = lambda: output_file.write("\n")

def write_tdarray(tdarray):
    for row in tdarray:
        for element in row:
            output_file.write(f"{element} ")
        output_file.write("\n")


output_file = open("DATA1.txt", "w")

output_file.write("1. Declare the given two dimensional arrays\n")
output_file.write("TDA:\n")
write_tdarray(tda)
newline()
output_file.write("TDB:\n")
write_tdarray(tdb)
newline()

newline()
output_file.write("2. Copy the TDA column3 to TDB column5\n")

for i in range(len(tda)):
    tdb[i][5] = tda[i][3]
        
output_file.write("TDB:\n")
write_tdarray(tdb)
newline()

newline()

output_file.write("3. Copy the TDA row 4 to TDB column2\n")

temp_list = list(tda[4])

for i in range(len(tdb)):
    tdb[i][2] = temp_list[i]

output_file.write("TDB:\n")
write_tdarray(tdb)
newline()

newline()
output_file.write("4. Compute and display for the sum of TDA first column and TDB first row\n")
tda_first_col = 0

for i in range(len(tda)):
    tda_first_col += tda[i][0]
output_file.write(f"TDA Sum of first column: {str(tda_first_col)}\n")

tdb_sum_first_row = sum(tdb[0])
output_file.write(f"TDB Sum of first row: {str(tdb_sum_first_row)}\n")
output_file.write(f"Sum of TDA first column and TDB first row: {str(tda_first_col + tdb_sum_first_row)}")

newline()

newline()
output_file.write("5. Compute and display for the sum of TDA last row and TDA last column\n")
tda_sum_last_row = sum(tda[-1])
tda_sum_col = 0
for i in range(len(tda)):
    tda_sum_col += tda[i][-1]

output_file.write(f"Sum of TDA last row: {str(tda_sum_last_row)}\n")
output_file.write(f"Sum of TDA last column: {str(tda_sum_col)}\n")
output_file.write(f"Sum of TDA last row and TDA last column: {str(tda_sum_last_row + tda_sum_col)}")

newline()

newline()
output_file.write("6. Count the elements in TDA with values of 3\n")

counter_3 = 0
for i in range(len(tda)):
    for j in range(len(tda[0])):
        if tda[i][j] == 3:
            counter_3 += 1
            
output_file.write(f"Values of 3 in TDA: {str(counter_3)}")
newline()

newline()
output_file.write("7. Count the elements in TDB with values of 4\n")

counter_4 = 0
for i in range(len(tdb)):
    for j in range(len(tdb[0])):
        if tdb[i][j] == 4:
            counter_4 += 1

output_file.write(f"Values of 4 in TDB: {str(counter_4)}")
newline()

newline()
output_file.write("8. Assign a one-dimensional array that will store the value, if row 0 of TDA is greater than row 4 of TDB is TRUE store the value of TDA otherwise the value of TDB\n")


def number_8_algorithm(a, b):
    """
    if curr_list==None:
        curr_list = []
    else:
        curr_list=curr_list
    """
    
    if a > b:
        return a
    else:
        return b
    
number_8 = [number_8_algorithm(a, b) for (a, b) in zip(tda[0], tdb[4])]
output_file.write(f"One-dimensional array formed: {str(number_8)}")

newline()

newline()
output_file.write("9. Sort the values of TDA\n")
tda.sort()
output_file.write("TDA sorted:\n")
write_tdarray(tda)
newline()

newline()
output_file.write("10. Reverse the value of TDB\n")
tdb.reverse()
output_file.write("TDB reversed:\n")
write_tdarray(tdb)
newline()

newline()
output_file.write("11. Compute for the sum of all values greater than 5 in TDA\n")

number_11_sum = 0
for i in range(len(tda)):
    for j in range(len(tda[0])):
        if tda[i][j] > 5:
            number_11_sum += tda[i][j]
output_file.write(f"Sum of all values greater than 5 in TDA: {str(number_11_sum)}")

newline()

newline()
output_file.write("12. Compute for the sum of all values less than 6 in TDB\n")
number_12_sum = 0
for i in range(len(tdb)):
    for j in range(len(tdb[0])):
        if tdb[i][j] < 6:
            number_12_sum += tdb[i][j]
output_file.write(f"Sum of all values less than 6 in TDB: {str(number_12_sum)}")
newline()

newline()
output_file.write("13. Compute for the sum of TDA\n")
tda_sum = 0
for i in range(len(tda)):
    for j in range(len(tda[0])):
        tda_sum += tda[i][j]
output_file.write(f"Sum of TDA: {str(tda_sum)}")
newline()

newline()
output_file.write("14. Compute for the sum of TDA except all values row2\n")
num_14_sum = 0
for i in range(len(tda)):
    for j in range(len(tda[0])):
        if not i == 2:
            num_14_sum += tda[i][j]
output_file.write(f"Sum of TDA except row2: {str(num_14_sum)}")
newline()

newline()
output_file.write("Code By: Ned Markus S. Basilio | CS-201")
output_file.close()