"""
Data Types

In most programming languages, data types and variable concepts are similar.
Since you're coming from a C/C++ background, you'll find this easy.

BUT Python has some unique behaviors:
- Dynamic typing (you don't need to mention the type)
- A new type called 'None'
"""

# 🔢 Numeric Data Types
a = 10          # Integer
b = 3.14        # Float
c = 2 + 3j      # Complex number (real + imaginary)

# 🧵 String Data Type
name = "Fojle Rabbi"  # Text (sequence of characters)

# ✅ Boolean Data Type
is_happy = True       # Boolean can be either True or False
is_tired = False

# ❌ None Type
nothing = None        # Represents "no value" or "empty"

# ℹ️ Python automatically detects types (no need for int, float, etc.)
print(type(a))        # <class 'int'>
print(type(b))        # <class 'float'>
print(type(name))     # <class 'str'>
print(type(nothing))  # <class 'NoneType'>


# 📛 Variable Naming Rules in Python:
# ✅ Must start with a letter (a-z, A-Z) or underscore (_)
# ✅ Can contain letters, digits (0-9), and underscores
# ❌ Cannot start with a digit
# ❌ Cannot use reserved Python keywords like 'if', 'while', 'class', etc.

# ✅ Valid variable names:
my_name = "Fojle"
_age = 20
marks123 = 95

# ❌ Invalid variable names:
# 2name = "Wrong"
# class = "Error"  # 'class' is a reserved keyword

