age = input("Are you 18? \n")

if age == "yes":
    print("True")
else:
    print("False")

# ami jei code likhchi emon na je eita vul hoiche but eitake aro better banano jay like
age = input("Are you 18? (yes/no) \n")

is_adult = age.lower() == "yes"

print(is_adult)
