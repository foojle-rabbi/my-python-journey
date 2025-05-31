"""
📘 type() Function in Python

The `type()` function is used to check the data type of any variable or value.
Very useful for debugging or when you're unsure of what type you're working with.
"""

# 🔹 Basic Usage
a = 10
b = 3.14
c = "Fojle Rabbi"
d = True
e = None

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'NoneType'>


# 🔹 It also works with more complex data types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"name": "Fojle", "age": 22}
my_set = {1, 2, 3}

print(type(my_list))   # <class 'list'>
print(type(my_tuple))  # <class 'tuple'>
print(type(my_dict))   # <class 'dict'>
print(type(my_set))    # <class 'set'>


# 🔸 You can even use type() inside conditions
x = 100

if type(x) == int:
    print("x is an integer")

