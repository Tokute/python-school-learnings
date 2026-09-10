# Ned Markus S. Basilio | CS-201
import random

def insertion_sort(arr, ascending=True):
    if arr is None:
        print("Error no array given.")
        return

    for i in range(1, len(arr)):
        temp_num = arr[i]
        j = i - 1

        while (j >= 0 and ((arr[j] > temp_num and ascending) or (arr[j] < temp_num and not ascending))):
            arr[j + 1] = arr[j]
            j-= 1
        
        arr[j + 1] = temp_num
        # print_arr(arr)

def print_arr(arr):
    for num in arr:
        print(num, end=" ")
    print()

def write_arr(arr):
    for num in arr:
        file.write(f"{num} ")
    file.write("\n")

if __name__ == "__main__":
    file = open("output.txt", "w")
    while True:
        print("=" * 5, "Insertion Sort Program", "=" * 5)
        print("[1] Generate 10 Random Numbers")
        print("[2] Sort in Ascending")
        print("[3] Sort in Descending")
        print("[4] Exit")

        try:
            choice = int(input("Enter choice: "))
        except Exception as e:
            print("Error.")

        match choice:
            case 1:
                arr = [random.randint(1, 25) for _ in range(10)]
                print("======= Generated List =======")
                file.write("======= Generated List =======\n")
                print_arr(arr)
                write_arr(arr)
            case 2:
                insertion_sort(arr)
                print("======= Sorted List (Ascending) =======")
                file.write("======= Sorted List (Ascending) =======\n")
                print_arr(arr)
                write_arr(arr)
            case 3:
                insertion_sort(arr, ascending=False)
                print("======= Sorted List (Descending) =======")
                file.write("======= Sorted List (Descending) =======\n")
                print_arr(arr)
                write_arr(arr)
            case 4:
                print("Thank you for using the program.")
                print("Ned Markus S. Basilio | CS-201")
                break

    file.close()