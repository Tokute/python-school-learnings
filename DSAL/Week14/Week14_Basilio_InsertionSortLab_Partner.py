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

if __name__ == "__main__":
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
                print_arr(arr)
            case 2:
                insertion_sort(arr)
                print("======= Sorted List (Ascending) =======")
                print_arr(arr)
            case 3:
                insertion_sort(arr, ascending=False)
                print("======= Sorted List (Descending) =======")
                print_arr(arr)
            case 4:
                print("Thank you for using the program.")
                print("Ned Markus S. Basilio | CS-201")
                break
