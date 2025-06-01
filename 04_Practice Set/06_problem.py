# 6. Write a program to:
# - Create a list of numbers
# - Replace all even numbers with their square in the same list
# - Print the modified list

my_list = [12, 3, 8, 21, 4, 23, 35, 21, 86]

print("Before opration: ", my_list)
for i in my_list:
    # if my_list[i] % 2 == 0:
    #     square = my_list[i] ** 2
    #     my_list[i] = square

    # upre amar mylist use na kore i use kora dorkar chilo casue i e toh amar mylist er values
    if i % 2 == 0:
        square = i ** 2
        # but here is a check for indexing i need the current index. so how can i find that? yes possible with
        my_list[my_list.index(i)] = square
# I think now it should work hehe: yes both logic are fine. 

# ooh na ami toh eikhane vul korechi
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        square = my_list[i] ** 2
        my_list[i] = square
    

print("After operation: ", my_list)