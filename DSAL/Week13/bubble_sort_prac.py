arr = [13, 30, 98, 45, 10, 65, 20, 81]
arr2 = ['K', 'F', 'B', 'E', 'X', 'P', 'T', 'A', 'M', 'Q', 'Z', 'G', 'O']

def bubble_sort(arr):
    for i in range(len(arr)):
        print("Loop", i+1, end="")
        print(arr)
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

#bubble_sort(arr)

def selection_sort(arr):
    for i in range(len(arr)):
        minimum_index = i
        print("Loop", i+1, end=" ")

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum_index]:
                minimum_index = j

        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
        print(arr)

    return arr

selection_sort(arr2)
