# 5. Write a program that:
# - Creates a list of 3 tuples, each tuple having 2 integers
# - Prints the sum of the two integers in each tuple  

list_of_tuple = [(10, 20), (20, 25), (50, 100)]

# now lets check how can I access them?
value = list_of_tuple[0][0] # yes i can acces using index so now lets find the sum

print("The sum of first tuple: ", list_of_tuple[0][0] + list_of_tuple[0][1])
print("The sum of first tuple: ", list_of_tuple[1][0] + list_of_tuple[1][1])
print("The sum of first tuple: ", list_of_tuple[2][0] + list_of_tuple[2][1])

# print(value)