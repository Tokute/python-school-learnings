# Ned Markus S. Basilio | CS-201

import random

random_nums = [random.randint(1, 20) for _ in range(10)]
newline = lambda: file.write("\n")

def bubble_sort(arr, ascending=True):
    print("Bubble Sort Chosen.")
    file.write("Bubble Sort Chosen.\n")

    if ascending:
        file.write("Sorting in Ascending Order:\n")
    else:
        file.write("Sorting in Descending Order:\n")

    newline()
    size = len(arr)

    for i in range(size):
        for j in range(0, size - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                file.write("* ")
                print("* ", end="")
            file.write(f"Iteration {i + 1}.{j + 1}: " + ", ".join(map(str, arr)) + "\n")
            print(f"Iteration {i + 1}.{j + 1}: " + ", ".join(map(str, arr)))
    newline()

    return arr

def selection_sort(arr, ascending=True):
    print("Selection Sort Chosen.")
    file.write("Selection Sort Chosen.\n")
    if ascending:
        file.write("Sorting in Ascending Order:\n")
    else:
        file.write("Sorting in Descending Order:\n")
    newline()
    size = len(arr)

    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if (ascending and arr[j] < arr[min_index]) or (not ascending and arr[j] > arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        file.write(f"Iteration {i + 1}: " + ", ".join(map(str, arr)) + "\n")
        print(f"Iteration {i + 1}: " + ", ".join(map(str, arr)))
    newline()

    return arr

with open("display.txt", "w") as file:
    file.write("Random Numbers:\n")
    file.write(", ".join(map(str, random_nums)) + "\n")
    newline()

    print("Random Numbers:")
    print(", ".join(map(str, random_nums)))
    print()

    print("CHOOSE TEST-CASE OR INTERACTIVE INPUTS:")
    print("[1] Test-Case Scenario")
    print("[2] Interactive Inputs")

    choice = input("Input Option (1/2): ")

    if choice == "1":
        print("THIS IS A TEST-CASE SCENARIO.")
        file.write("THIS IS A TEST-CASE SCENARIO.\n")
        print("* = A swapped has occurred in this iteration.")
        file.write("* = A swapped has occurred in this iteration.\n")
        print()

        # Bubble Ascending Sort
        sorted_nums = bubble_sort(list(random_nums), ascending=True)
        print("=" * 50)
        file.write("=" * 50 + "\n")
        # Bubble Descending Sort
        sorted_nums = bubble_sort(list(random_nums), ascending=False)
        print("=" * 50)
        file.write("=" * 50 + "\n")

        # Selection Ascending Sort
        sorted_nums = selection_sort(list(random_nums), ascending=True)
        print("=" * 50)
        file.write("=" * 50 + "\n")
        # Selection Descending Sort
        sorted_nums = selection_sort(list(random_nums), ascending=False)
        print("=" * 50)
        file.write("=" * 50 + "\n")
    elif choice == "2":
        print("Random Numbers:")
        print(", ".join(map(str, random_nums)))
        print()

        print("Algorithm Option:")
        print("[1] Bubble Sort")
        print("[2] Selection Sort")
        sort_algo = input("Input Option (1/2): ")

        print("Sorting Option:")
        print("[1] Ascending")
        print("[2] Descending")
        sort_option = input("Input Option (1/2): ")
        print()

        if sort_algo == "1":
            sorted_nums = bubble_sort(list(random_nums), ascending=(sort_option == "1"))
            file.write("Bubble Sort:\n")
            file.write(", ".join(map(str, sorted_nums)) + "\n")
            newline()

            newline()
            print()
            print("Bubble Sort:")
            print(", ".join(map(str, sorted_nums)))
            print()
        elif sort_algo == "2":
            sorted_nums = selection_sort(list(random_nums), ascending=(sort_option == "1"))
            file.write("Selection Sort:\n")
            file.write(", ".join(map(str, sorted_nums)) + "\n")
            newline()

            newline()
            print()
            print("Selection Sort:")
            print(", ".join(map(str, sorted_nums)))
            print()
