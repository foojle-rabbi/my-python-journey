# 8. Write a program to:
# - Create a nested list (list of lists)
# - Print all elements using nested loops

# eita onekta amader matrix er moto. but eikhane size can vary 
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# okay lets first print the 3x3 size matrix
for row in list_of_list:
    for col in row:
        print(col, end=" ") # ei end=" " new line break kore
    # ekta new line dorkar so
    print()

# now lets create list of different size
list_of_diff = [[1], [1, 2, 3], [1, 2, 3, 4], [0, 0], [1, 2, 3, 4, 5], [0, 0, 1]]

print("Printing list of diffrent size")
for row in list_of_diff:
    for col in row:
        print(col, end=" ")
    print() # to have a new line 

print(list_of_diff, list_of_diff[2][2]) # yes it can be accessed through indexes