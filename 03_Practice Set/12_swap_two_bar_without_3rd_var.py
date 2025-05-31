# i knew that its possbile to swap two number without using 3rd or temp variable.

#it can be done with subtruction and other method is using bitwise operator. so lets so it

number1 = 10
number2 = 20

print(f"Before swapping\nnumber1 is : {number1}\nNumber2 is : {number2}")
#lets impelement our logc
number2 = number1 + number2
number1 = number2 - number1
number2 = number2 - number1

print(f"After swapping\nnumber1 is : {number1}\nNumber2 is : {number2}")

# now lets try with xor operator
number1 = number1 ^ number2
number2 = number2 ^ number1
number1 = number1 ^ number2
print(f"using bitwise operator\nnumber1 is : {number1}\nNumber2 is : {number2}")

# yeah finnaly both method works fine. ekta kothay ache learning never dissapoint us. 