print("Name: Ned Markus S. Basilio\nSection: CS-201")

# 1. Declare

List1 = ['a','b','c','d','e']
List2 = [i for i in range (2, 11, 2)]
Tuple1 = ('v','w','x','y','z')
Tuple2 = (1,3,5,7,9)
Sets1 = {'q','e','i','o','u'}
Sets2 = {'a','e'}

# 2. Combine and Display

combined_data_structures = [
    [List1, "List1"],
    [List2, "List2"],
    [Tuple1, "Tuple1"],
    [Tuple2, "Tuple2"],
    [Sets1, "Sets1"],
    [Sets2, "Sets2"]
]

print("\n2. Combined values of all data structures:")

for i in range(len(combined_data_structures)):
    for element in combined_data_structures[i][0]:
        print(element, end=" ")
print()

# 3. Display the items of the collections

def determine_data_structure_type(data_structure, var_name="current"):
    if isinstance(data_structure, list):
        return f"The {var_name} data structure is a list."
    elif isinstance(data_structure, tuple):
        return f"The {var_name} data structure is a tuple."
    elif isinstance(data_structure, set):
        return f"The {var_name} data structure is a set."
    else:
        return f"Could not determine {var_name} type. Missing object: {type(data_structure)}"

def display_collection(data_structure):
    for index, element in enumerate(data_structure):
        print(f"index {index}: {element}")

# 3. Display items of the collection

print("\n3. Display the items of the collection:")

for i in range(len(combined_data_structures)):
    print(determine_data_structure_type(combined_data_structures[i][0], var_name=combined_data_structures[i][1]))
    display_collection(combined_data_structures[i][0])
    print()

print("List1 from index 2 up to last item:")
print(List1[2:])

print("Tuple1 from index 1 to index 3:")
print(Tuple1[1:4])

print()

# 4. Display total items of each collection.

print("4. Display the total items of each collection.")
total = 0
for i in range(len(combined_data_structures)):
    print(f"The total items of the {combined_data_structures[i][1]} data structure is: {len(combined_data_structures[i][0])}")
    total += len(combined_data_structures[i][0])
print("Total items across all collections: " + str(total))
print()
# 5. Update index 2 of all collections to 'A'. Display the items of the collections.

print("5. Updated index 2 of collections to 'A'.")


print()
List1[2] = 'A'
List2[2] = 'A'

temp_list = list(Tuple1)
temp_list[2] = 'A'
combined_data_structures[2][0] = tuple(temp_list)
del(temp_list)

temp_list = list(Tuple2)
temp_list[2] = 'A'
combined_data_structures[3][0] = tuple(temp_list)
del(temp_list)

Sets1.remove('i')
Sets1.add('A')
Sets2.add('A')
# Sets are unordered, tuples are immutable?? Unless java if using a LinkedHashSet.

for i in range(len(combined_data_structures)):
        print(combined_data_structures[i][1])
        display_collection(combined_data_structures[i][0])
        print()

# 6. Remove the items and display the remaining items of the collections
print()
print("6. Remove the items and display the remaining items of the collections.")

to_remove = ['d', 10, 'w', 5]

for i in range(len(combined_data_structures)):
    if (0 <= i <= 1) or (4 <= i <= 5):
        for element in to_remove:
            if element in combined_data_structures[i][0]:
                combined_data_structures[i][0].remove(element)
                if isinstance(combined_data_structures[i][0], list) and (len(combined_data_structures[i][0]) > 2):
                    combined_data_structures[i][0].pop(0)
                    combined_data_structures[i][0].pop(-1)
    elif (2 <= i <= 3):
        temp_list = list(combined_data_structures[i][0])
        for element in to_remove:
            if element in temp_list:
                temp_list.remove(element)
                if len(temp_list) > 2:
                    temp_list.pop(0)
                    temp_list.pop(-1)
        combined_data_structures[i][0] = tuple(temp_list)
        del(temp_list)

    print(combined_data_structures[i][1])
    display_collection(combined_data_structures[i][0])
    print()

# 7. Display the length of the combined collections
print("7. Display the length of the combined collections.")
combined_collections = []

for i in range(len(combined_data_structures)):
    for element in combined_data_structures[i][0]:
        combined_collections.append(element)

print("Combined Collections length: " + str(len(combined_collections)))
print()

# 8. Determine the methods needed and display 'YES' if the letter 'e' exists on the lists, tuples, and sets.
print("8. Determine the methods needed and display 'YES' if the letter 'e' exists on the lists, tuples, and sets.")
print()

for i in range(len(combined_data_structures)):
    print(f"Evaluating {combined_data_structures[i][1]}...", end=" ")
    if 'e' in combined_data_structures[i][0]:
        print("YES")
    else:
        print("NO")
print()
# 9. Display the elements of lists and tuples in ascending order.
print("9. Display the elements of lists and tuples in ascending order.")

for i in range(len(combined_data_structures)):
    if i > 3: # breaks before the sets
        break

    if isinstance(combined_data_structures[i][0], tuple):
        temp_list = list(combined_data_structures[i][0])
        temp_list.sort(key=lambda x: (0, x) if isinstance(x, int) else (1, x))
        combined_data_structures[i][0] = tuple(temp_list)
        del(temp_list)
    else:
        combined_data_structures[i][0].sort(key=lambda x: (0, x) if isinstance(x, int) else (1, x))
    
    print(f"{combined_data_structures[i][1]}:")
    display_collection(combined_data_structures[i][0])
    print()

# 10. Display the highest element in the list and the lowest element in the tuple.
print("Display the highest element in the list and the lowest element in the tuple.")

print("Highest element (Lists)")
print(f"List1: {combined_data_structures[0][0][0]}")
temp_list_List2_int = [i for i in combined_data_structures[1][0] if isinstance(i, int)]
temp_list_List2_str = [i for i in combined_data_structures[1][0] if isinstance(i, str)]
temp_list_List2_str.sort()
print(f"List2: {(max(temp_list_List2_int), temp_list_List2_str[0])}")
del(temp_list_List2_int)
del(temp_list_List2_str)
print()

print("Lowest element (tuples)")
print(f"Tuple1: {combined_data_structures[2][0][-1]}")
temp_list_Tuple2_int = [i for i in list(combined_data_structures[3][0]) if isinstance(i, int)]
temp_list_Tuple2_str = [i for i in list(combined_data_structures[3][0]) if isinstance(i, str)]
temp_list_Tuple2_str.sort()
print(f"Tuple2: {(min(temp_list_Tuple2_int), (temp_list_Tuple2_str[-1]))}")
del(temp_list_Tuple2_int)
del(temp_list_Tuple2_str)
print()

# 11. Demonstrate how to empty or delete contents of a list, tuples, and sets.
print("11. Demonstrate how to empty or delete contents of a list, tuples, and sets.")
print()

print("Emptying/Deleting contents of a list offers 3 methods:\n.remove(), .pop(), or .clear()")
print(".remove() takes in an argument and raises a ValueError if the item is not found.")
print(".pop() remove the item from list1 and returns it to list2. Will default to the last index of list1 if no index specified.")
print(".clear() will clear the list.")

print("\nSets also use .remove() and .clear().")
print("Though, sets have .discard(), which removes an element if it exists but raises an error if it is missing.")

print("Finally, Tuples can only be deleted using del().")

print("\nApplying .clear() and del() for tuples:")
print("List1:", end=" ")
print(List1)
List1.clear()
print("After: " + str(List1))
print()
print("Sets1: " + str(Sets1))
Sets1.clear()
print("After: " + str(Sets1))
print()
print("Tuple1: " + str(Tuple1))
del(Tuple1)
print("After: Tuple1 is not defined.")

print("\nCode made by: Ned Markus S. Basilio | CS-201")