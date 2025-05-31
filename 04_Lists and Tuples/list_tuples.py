"""
📘 Lists and Tuples in Python

🔹 List:
A list is a collection which is ordered and **mutable** (changeable).
Tumi chaile list er moddhe je kono type er data rakhte parba: number, string, boolean etc.
List er value change kora jai.

🔹 Tuple:
Tuple holo ordered collection, but **immutable** (unchangeable).
Tuple er data ekbar set korle tarpor change kora jai na.

Ekhon cholo details e dekhi:
"""

# 🔹 Creating Lists
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30]
mixed = [1, "hello", True]

print(fruits)   # ['apple', 'banana', 'mango']
print(numbers)  # [10, 20, 30]
print(mixed)    # [1, 'hello', True]


# 🔹 Accessing List Items
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'mango' (last item)


# 🔹 Modifying List
fruits[1] = "orange"
print(fruits)       # ['apple', 'orange', 'mango']


# 🔹 List Operations
fruits.append("grape")         # add at the end
fruits.insert(1, "kiwi")       # insert at index 1
print(fruits)                  # ['apple', 'kiwi', 'orange', 'mango', 'grape']

fruits.remove("orange")        # remove specific item
last = fruits.pop()            # remove last item
print(fruits)                  # ['apple', 'kiwi', 'mango']
print("Popped:", last)         # grape


# 🔹 Useful List Methods
nums = [3, 1, 4, 2]
nums.sort()
print("Sorted:", nums)         # [1, 2, 3, 4]

nums.reverse()
print("Reversed:", nums)       # [4, 3, 2, 1]

print("Length:", len(nums))    # 4


# 🔹 Slicing a List
print(nums[1:3])     # [3, 2]
print(nums[:2])      # [4, 3]
print(nums[2:])      # [2, 1]

# 🔹 You can also use the slicing [start: stop: step]

step = [10, 15, 35, 21, 51, 32, 12]
print(step[::2]) # output: 10 35 51 12


# 🔹 Tuples
# in a simpler word tuples are like list but as list is muatalbe means you can change the values of any indexes
# but you cant change the values of any indexes in a tuple 
person = ("John", 25, "USA")
print(person)             # ('John', 25, 'USA')
print(person[0])          # 'John'

# 🔹 Tuple Methods
print(len(person))             # 3
print(person.count("USA"))     # 1
print(person.index(25))        # 1

# 🔹 Tuples are immutable
# person[0] = "Mike"     # ❌ Error: Tuples cannot be changed


# 🔹 List vs Tuple Summary
print("\nList vs Tuple:")
print("List:", fruits)        # List is mutable
print("Tuple:", person)        # Tuple is immutable

# lasltly 
# the main differenct between a list and tuple is: 
# list can be changeable 
# tuple cannot be changed
# list is declared using []
# tuple is declared using ()
# also list is slightly slower because of mutabiltiy and tuple is faster because of immutablity
