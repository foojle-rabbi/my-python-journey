"""
📘 Typecasting (Type Conversion)

Typecasting means **converting one data type into another**.

✅ In Python, we can convert:
- int → float / str / bool
- float → int / str / bool
- str → int / float (only if it's numeric)

means amra jei kono data type ke jei kono data types e convert korte parbo. jehetu amader python er moddhe 
kon data type sheta mention kora lage na. so jodi amader kono specific data type dorkar hoy tokhon amra typecast use kori

just beshi kichu na. tumi jeitake typecast korte chaccho tar age data type likhe diba like: flaot(s), int(), 
"""

# 🔹 1. int() — Convert to Integer
a = "10"
b = 3.9
c = True

print(int(a))   # 10 (string to int)
print(int(b))   # 3  (float to int — decimal part removed)
print(int(c))   # 1  (True becomes 1, False becomes 0)

# 🔹 2. float() — Convert to Float
a = "10"
b = 5
c = False

print(float(a))  # 10.0 (string to float)
print(float(b))  # 5.0 (int to float)
print(float(c))  # 0.0 (False becomes 0.0)

# 🔹 3. str() — Convert to String
a = 100
b = 3.14
c = True

print(str(a))  # '100'
print(str(b))  # '3.14'
print(str(c))  # 'True'

# 🔹 4. bool() — Convert to Boolean
print(bool(0))       # False
print(bool(1))       # True
print(bool(-5))      # True
print(bool(""))      # False (empty string is False)
print(bool("Hi"))    # True (non-empty string is True)
print(bool([]))      # False (empty list is False)

# 🔹 5. Converting between collections
print(list("Fojle"))     # ['F', 'o', 'j', 'l', 'e']
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set("hello"))      # {'l', 'o', 'h', 'e'} — removes duplicates

# ❗ Be careful: converting invalid strings to int or float will crash the program
# int("Fojle")  ❌ This will throw an error
