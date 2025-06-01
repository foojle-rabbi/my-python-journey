# 7. Given a tuple of numbers, write a program to:
# - Find the maximum and minimum value

my_tuple = (12, 15, -3, -21, 52, 33, 11, 89, -2, 50)

# okay then lets impleemnt our logics here
# min = INT_MIN # so if its not work then lets try another way;

min = my_tuple[0] # lets assume the first value is minium
max = my_tuple[0] # same goes with the maximu;

# lets iterate the whole tuple
for value in my_tuple:
    if min > value:
        min = value
    if max < value:
        max = value

# okay lets see if it works!
print(f"The values of tuple {my_tuple} \nThe maxium is: {max}\tThe minimum is: {min}")

# # there are some others methods too
#     1. by sorting the tuple using sort method
#     2. 
# ------------- no no there is no in build sort method of tuple
# print(my_tuple.sort())

# my_list = [9, 2]
# print((my_list.sort())) # why its showing none?