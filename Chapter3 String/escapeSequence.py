# -----------------------------------------------
# 🔸 Escape Sequences in Python
# -----------------------------------------------

# These are special characters used inside strings to do things like:
# new lines, tabs, printing quotes, and more.

# -----------------------------
# \n → New Line
# -----------------------------
print("Hello\nWorld")  
# Output:
# Hello
# World

# -----------------------------
# \t → Tab (Horizontal space)
# -----------------------------
print("Name:\tFojle")  
# Output: Name:    Fojle (adds tab space between)

# -----------------------------
# \' → Single quote inside single quotes
# -----------------------------
print('It\'s a beautiful day')  
# Output: It's a beautiful day

# -----------------------------
# \" → Double quote inside double quotes
# -----------------------------
print("He said \"I will go\"")  
# Output: He said "I will go"

# -----------------------------
# \\ → Backslash itself
# -----------------------------
print("This is a backslash: \\")  
# Output: This is a backslash: \

# -----------------------------
# \r → Carriage return (moves cursor to beginning of the line)
# -----------------------------
print("Python\rROCKS")  
# Output: ROCKS (overwrites Python with ROCKS)

# -----------------------------
# \b → Backspace (removes 1 character before)
# -----------------------------
print("Helloo\b!")  
# Output: Hello! (the extra 'o' is removed)

# -----------------------------
# \f → Form feed (rarely used, behaves differently in terminals)
# -----------------------------
print("Line1\fLine2")  
# Output: Line1Line2 (you may see a page break symbol or weird spacing)
