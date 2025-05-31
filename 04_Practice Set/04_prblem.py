# 4. Given a list of names, write a program to:
# - Check if a given name is in the list (print True/False)
# - Count how many times a particular name appears

names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fojle", "Grace", "Hannah"]

name_in_list = input("Enter a name to check: ")

if name_in_list in names:
    print("True")
else:
    print("False")

name_in_list = input("Enter a name to find out how many time it appear: ")

print(f"The name {name_in_list} appears {names.count(name_in_list)} times")