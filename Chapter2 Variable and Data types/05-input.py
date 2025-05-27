"""
📘 input() Function

The `input()` function is used to **take input from the user** during program execution.

By default, input is always read as a string (text).

So jehetu amader input ta string akare read hoy she jonno amader jodi number niye kaj korte hoy tahole type cast kore 
nite hobe. jodi typecast na kori tahole string hisebe dhora hobe. int(input("Enter a number: ))

ar hae amra chaile input er vitorei ja mon chay likhte pari.
"""

# 🔹 Basic input usage
name = input("Enter your name: ")  # Shows prompt, waits for user input
print("Hello, " + name + "!")       # Prints greeting with the input name


# 🔹 Taking numeric input
age = input("Enter your age: ")    # input() returns string
print(type(age))                   # <class 'str'>

# To use it as an integer, convert with int()
age_int = int(age)
print(type(age_int))               # <class 'int'>
print("You will be", age_int + 1, "years old next year.")


# 🔹 Taking float input
price = float(input("Enter price: "))  # Convert input to float immediately
print("Price after tax:", price * 1.1)


# 🔹 Important note:
# If user inputs something that can't be converted (like letters when expecting int),
# the program will throw an error. You can handle that later with try-except blocks.


# 🔹 Example - Full program snippet
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum is:", num1 + num2)


num = input("Enter your age : ")
print(num)

name = input("Enter you name: ")
print("Hello " + name + " whats up? you are now ", num, " years old")

# so jodi amader number niye kaj korte hoy tahole amra 
a = int(input("Enter number first nubmer: "))
b = int(input("Enter you second number: "))

sum = a + b
print("Sum of these two numbers: ", sum)