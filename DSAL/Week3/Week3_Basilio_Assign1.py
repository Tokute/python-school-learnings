# Code by: Ned Markus S. Basilio | CS-201
import array as arr
temp_celsius = arr.array('d', [27.2, 24.7, 29.4, 25.3, 26.5, 23.9, 27.8, 25.0, 28.2, 26.9])
def evaluate_temperatures(given_arr):
    threshold_temp = 26.0

    hot_days_arr = arr.array('d')
    non_hot_days_arr = arr.array('d')

    for temp in given_arr:
        if temp <= threshold_temp:
            non_hot_days_arr.append(temp)
        elif temp > threshold_temp:
            hot_days_arr.append(temp)
        else:
            print("Error evaluating temperature.")

    return hot_days_arr, non_hot_days_arr

def get_average(given_arr):
    average = 0
    for temp in given_arr:
        average += temp

    average /= len(given_arr)
    return average

output_file = open("tempoutput.txt", "w")
newline = lambda: output_file.write("\n")

output_file.write("Code by: Ned Markus S. Basilio | CS-201\n")
newline()

print("Test Case Values:")
output_file.write("Test Case Values:\n")
for temp in temp_celsius:
    print(format(temp, ".2f"), end="C ")
    output_file.write(f"{format(temp, ".2f")}C ")
print("\n")
newline()

hot_days_arr, non_hot_days_arr = evaluate_temperatures(temp_celsius)

newline()
print(f"Hot Days: {str(hot_days_arr)}")
output_file.write(f"Hot Days: {str(hot_days_arr)}\n")
print(f"Non-hot Days: {str(non_hot_days_arr)}")
output_file.write(f"Non-hot Days: {str(non_hot_days_arr)}\n")
print()

newline()
print("Number of hot days and non-hot days:", len(hot_days_arr) + len(non_hot_days_arr))
output_file.write(f"Number of hot days and non-hot days: {str(len(hot_days_arr) + len(non_hot_days_arr))}")
newline()
print("Number of hot days:", len(hot_days_arr))
output_file.write(f"Number of hot days: {str(len(hot_days_arr))}")
newline()
print("Number of non-hot days:", len(non_hot_days_arr))
output_file.write(f"Number of non-hot days: {str(len(non_hot_days_arr))}")
newline()
print()
newline()

print(f"Average temperature for hot days: {get_average(hot_days_arr):.2f}C")
output_file.write(f"Average temperature for hot days: {get_average(hot_days_arr):.2f}C")
newline()
print(f"Average temperature for non-hot days: {get_average(non_hot_days_arr):.2f}C")
output_file.write(f"Average temperature for non-hot days: {get_average(non_hot_days_arr):.2f}C")
newline()

output_file.close()