# Tuple of numbers
my_tuple = (12, 15, -3, -21, 52, 33, 11, 89, -2, 50)

# -------------------------------
# Method 1: Manually find min and max
# -------------------------------
min_value = my_tuple[0]  # Assume first value is the minimum
max_value = my_tuple[0]  # Assume first value is the maximum

# Loop through all elements to find min and max
for value in my_tuple:
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value

print(f"Manual method → Max: {max_value}, Min: {min_value}")

# -------------------------------
# Method 2: Using built-in functions
# -------------------------------
min_builtin = min(my_tuple)
max_builtin = max(my_tuple)

print(f"Built-in min() and max() → Max: {max_builtin}, Min: {min_builtin}")

# -------------------------------
# Tuples cannot be sorted directly with .sort() because they are immutable
# -------------------------------
# So we use sorted() which returns a new sorted list
sorted_list_from_tuple = sorted(my_tuple)
print("Sorted version of tuple (as a list):", sorted_list_from_tuple)

# If you want to convert that list back to a tuple:
sorted_tuple = tuple(sorted_list_from_tuple)
print("Sorted version as a tuple:", sorted_tuple)

# -------------------------------
# Demonstrating .sort() with list
# -------------------------------
my_list = [9, 2, 4, 1]

# Incorrect way: print(my_list.sort())  # Will return None

# Correct way:
my_list.sort()  # Sorts the list in place
print("List after using .sort():", my_list)

# Or use sorted() to keep the original list unchanged
unsorted_list = [9, 2, 4, 1]
new_sorted_list = sorted(unsorted_list)

print("Original list:", unsorted_list)
print("New sorted list using sorted():", new_sorted_list)
