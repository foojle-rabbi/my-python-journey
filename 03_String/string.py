"""
📘 Strings in Python

A **string** is a sequence of characters enclosed in quotes.
Python supports single (' '), double (" "), and triple quotes (''' ''' or """ """) for strings.
Orthat tumi chaile singel doulbe ba triple quote dia string declare korte parba. tobe triple use hoy mutli line er jonno

Ar mone rakhba in python string is immutable means tumi sting er kicchu korte parba na. mane ekta string first e ja likhcho tai
tumi oitake change korte parba na. kono index er char change korte parba na. orthat ja ache tai. hae eita true je tumi chaile
string er onek functions use korte parba. But oi function gula main string ke change korbe na. borong ekta copy stirng kore
oita change korbe. 
"""

# 🔹 Creating strings
s1 = 'Hello'
s2 = "Fojle Rabbi"
s3 = '''This is a
multiline
string'''
s4 = """Also
a multiline
string"""

print(s1)
print(s2)
print(s3)
print(s4)


# 🔹 String operations
name = "Fojle"
greeting = "Hello " + name       # Concatenation
print(greeting)                  # Output: Hello Fojle

repeat = "Hi! " * 3              # Repetition
print(repeat)                    # Output: Hi! Hi! Hi!

length = len(name)               # Length of string
print("Length:", length)         # Output: Length: 5


# 🔹 Accessing characters (indexing)
word = "Python"

print(word[0])   # 'P' (first character, index 0)
print(word[-1])  # 'n' (last character, negative indexing) will talk about this later


# 🔹 Slicing strings
print(word[0:3])    # 'Pyt' (from index 0 to 2); means eikhne 0 theke shuru kore 3 porjonto print koro
print(word[2:])     # 'thon' (from index 2 to end); last jehetu khali tar mane 2 theke start kore last index porjonto
print(word[:4])     # 'Pyth' (from start to index 3); first jehetu khali tar mane 0 theke start kore
print(word[-3:-1])  # 'ho' (negative index slice) will talk about negetive slicing later


# 🔹 Strings are immutable (cannot be changed)
# word[0] = 'p'   # This will cause an error
#Means unlike c, c++ you cannot change any index of a string. they are immutable


# 🔹 Useful string methods
text = " hello world "

print(text.upper())        # ' HELLO WORLD '
print(text.lower())        # ' hello world '
print(text.strip())        # 'hello world' (removes leading/trailing spaces)
print(text.replace('world', 'Python'))  # ' hello Python '
print(text.split())        # ['hello', 'world']  (split by spaces)

# Check if substring in string
print('hello' in text)     # True
print('bye' in text)       # False
print('word' not in text)  # True 

# Find position of substring
print(text.find('world'))  # 7 (index of 'w' in 'world')
print(text.find('Python')) # -1 (not found)


