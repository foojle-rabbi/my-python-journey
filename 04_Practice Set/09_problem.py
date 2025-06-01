# 9. Take input from the user to:
# - Enter 5 names and store them in a list
# - Print the list
# - Print the list in reverse order

names_list = []

print("Enter 5 names: ")
for i in range(0, 5):
    # names_list[input()]  accha eivabe kora jabe na
    name = input()
    names_list.append(name)

print("Names in the list: ", names_list)
print("names in reverse order: ", names_list[::-1])