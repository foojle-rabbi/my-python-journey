"""
📘 Advanced String Slicing

Slicing syntax: string[start : end : step]

- start: starting index (inclusive)
- end: ending index (exclusive)
- step: how many characters to skip (default is 1)
"""

text = "PythonProgramming"

# 🔹 Negative slicing (using negative indices)
print(text[-1])        # 'g' (last character)
print(text[-6:-1])     # 'rammi' (from 6th last to 2nd last)
print(text[-6:])       # 'ramming' (from 6th last to end)

# 🔹 Negative step (reversing string)
print(text[::-1])      # 'gnimmargorPnohtyP' (whole string reversed)

# 🔹 Using step/skip value
print(text[0:10:2])    # 'PtoPg' (from 0 to 9, skip every 2nd char)
print(text[::3])       # 'Phga' (from start to end, skip every 3rd char)

# 🔹 Combining negative indices and step
print(text[-1::-1])    # Same as text[::-1], reverse entire string
print(text[10:3:-1])   # 'margorP' (slice backwards from index 10 to 4)

# 🔹 Examples for practice
example = "ABCDEFGHIJK"

print(example[1:8:2])    # 'BDF' (normal forward slicing)
print(example[-2:-9:-2]) # 'JHF' (backwards slicing with step 2)
print(example[::-2])     # 'KIGCEA' (reverse string skipping every 2nd char)

name = "itsFojle"
print(name[0:5:2]) # output: iso because start korbo 0 theke end hobe 5; ar will take every 2 index value; 

# ar hae amra chaile negative index dia khub easilty ekta string ke reverse korte pari.
print(name[::-1])