"""
📘 Operators in Python

Operators are used to perform operations on variables and values.

Python supports several types of operators:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""

# 🔢 1. Arithmetic Operators (+, -, *, /, %, //, **)
a = 10
b = 3

print(a + b)   # ➕ Addition → 13
print(a - b)   # ➖ Subtraction → 7
print(a * b)   # ✖️ Multiplication → 30
print(a / b)   # ➗ Division (float) → 3.333...
print(a % b)   # 🔁 Modulus (remainder) → 1
print(a // b)  # 🚫 Floor division → 3 (ignores decimal part)
print(a ** b)  # ⏫ Exponentiation → 10^3 = 1000


# 📝 2. Assignment Operators (=, +=, -=, *=, etc.)
x = 5          # Assigns 5 to x
x += 2         # Same as x = x + 2 → x = 7
x *= 3         # x = x * 3 → x = 21
x -= 1         # x = x - 1 → x = 20
print(x)


# ⚖️ 3. Comparison Operators (==, !=, >, <, >=, <=)
print(5 == 5)   # True
print(5 != 3)   # True
print(10 > 3)   # True
print(2 < 1)    # False
print(3 >= 3)   # True
print(4 <= 2)   # False


# 🧠 4. Logical Operators (and, or, not)
a = True
b = False

print(a and b)  # False (both must be True)
print(a or b)   # True (at least one is True)
print(not a)    # False (opposite of True)


# 🆔 5. Identity Operators (is, is not)
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (same memory location)
print(x is z)      # False (same content, different objects)
print(x is not z)  # True


# 🔍 6. Membership Operators (in, not in)
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True
print("orange" not in fruits)  # True


# ⚙️ 7. Bitwise Operators (Optional - advanced)
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
a = 5     # Binary: 0101
b = 3     # Binary: 0011

print(a & b)   # 1 (0001)
print(a | b)   # 7 (0111)
print(a ^ b)   # 6 (0110)
print(~a)      # -6 (inverts bits)
print(a << 1)  # 10 (shifts left)
print(a >> 1)  # 2  (shifts right)
