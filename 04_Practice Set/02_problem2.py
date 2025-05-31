# 2. Given a list of numbers, write a program to:
# - Add a new number to the end of the list
# - Remove the second element
# - Print the updated list

list = [10, "Fojle", False, 4.58, "Practice"] # though the statement said list of number you're using this list
print(list[::]) # it will print the whole list though we also can print the list using loop
for i in list:
    print(i)

list.append(40)
print("After adding a value: ", list[::])
print()

# lets now remove the second element
# list.remove(10) # so remove method takes a input data and removes that from the list. if its not there then it will throw error
# so amra kintu jani je pop method amader list theke element pop kore but oita return kore so 
removed = list.pop(2) 
# so as there is 0 based index so the False iteam will removed
print("After removing the second element: ", list[::])
