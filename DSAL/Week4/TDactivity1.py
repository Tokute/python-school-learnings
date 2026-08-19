output_file = open("output.txt", "w")
newline = lambda: output_file.write("\n")

lstA = [2, 5, 6, 9, 8]
output_file.write(f"lstA: {str(lstA)}")
newline()

lstB = [7, 3, 6, 8, 4]
output_file.write(f"lstB: {str(lstB)}")
newline()

lstC = [5, 9, 1, 3, 4]
output_file.write(f"lstC: {str(lstC)}")
newline()

LstTD = [[0 for _ in range(5)] for _ in range(5)]
output_file.write(f"LstTD:\n{str(LstTD)}")
newline()

newline()
LstTD[1] = list(lstA)
output_file.write("1. Copy the elements of lstA to row 1 of LstTD\n")
output_file.write(f"LstTD:\n{str(LstTD)}")
newline()

newline()
lstB.reverse()
output_file.write("2. Reverse lstB:\n")
output_file.write(str(lstB))
newline()

newline()
LstTD[2] = list(lstB)
output_file.write("3. Copy the elements of lstB to row2 LstTD:\n")
output_file.write(str(LstTD))
newline()

newline()
lstC.sort()
output_file.write("4. Sort lstC:\n")
output_file.write(str(lstC))
newline()

newline()
output_file.write("5. Copy the elements of lstC to row 3 of LstTD:\n")
LstTD[3] = list(lstC)
output_file.write(str(LstTD))
newline()

newline()
output_file.write("6. Input the following values to row 4 of LstTD: 2, 6, 4, 9, 8\n")
for i in range(len([2, 6, 4, 9, 8])):
    LstTD[4][i] = int(input(f"Enter value {i+1}: "))
output_file.write(str(LstTD))
newline()

newline()
output_file.write("7. Compute for the sum of row1 except row 4 and store in row 4 column 0:\n")
LstTD[4][0] = sum(LstTD[1])
output_file.write(f"LstTD[4][0] = {sum(LstTD[1])}\n")
output_file.write(f"LstTD:\n{str(LstTD)}")
newline()

newline()
output_file.write("8. Compute for the sum of column 1 an store in row 4 column 1\n")
value_sum = 0

for i in range(len(LstTD)):
    value_sum += LstTD[i][1]
LstTD[4][1] = value_sum
output_file.write(f"Sum of column 1 in all rows: {str(value_sum)}\n")
output_file.write(f"LstTD:\n{str(LstTD)}")
newline()

newline()
output_file.write("9. Assign in row 4 col 2, the highest element in row 3\n")
LstTD[4][2] = max(LstTD[3])
output_file.write(f"Highest value in row 3: {str(max(LstTD[3]))}\n")
output_file.write(f"LstTD:\n{str(LstTD)}")
newline()

newline()
output_file.write("10. Assign in row 4 col 3 the lowest element in row 4\n")
LstTD[4][3] = min(LstTD[4])
output_file.write(f"Lowest element in row 4: {str(min(LstTD[4]))}\n")
output_file.write(f"LstTD:\n{str(LstTD)}")
newline()

newline()
output_file.write("11. Assign in row 4 col 4 the sum of TD[0][0] and TD[3][3]\n")
LstTD[4][4] = LstTD[0][0] + LstTD[3][3]
output_file.write(f"LstTD[4][4] = {str(LstTD[0][0])} + {str(LstTD[3][3])}\n")
output_file.write(f"LstTD:\n{str(LstTD)}")
newline()

newline()
output_file.write("12. Count the odd and even number of elements in TD\n")
odd = 0
even = 0
for i in range(len(LstTD)):
    for j in range(len(LstTD[0])):
        if LstTD[i][j] % 2 == 0:
            even += 1
        else:
            odd += 1
output_file.write(f"Evens: {even} | Odds: {odd}")
newline()

newline()
output_file.write("Code By: Ned Markus S. Basilio | CS-201")
output_file.close()