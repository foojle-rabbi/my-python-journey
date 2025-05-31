# You will get a number as input then return the sum of digits.
# so shono fojle, sum of digits ber korar kintu khub nicer ekta way ache sehta holo 10 diye divide kore. but jeehtu
# amra python e kaj kortechi tai eikhane aro easy houar kotha. so will try both of them lets start.

# method 1:- divided by 10 method
number = int(input("Enter a number: "))
sum_of_digits = 0
while (number != 0):
    # print("number is ", number)
    rem = number % 10
    # print("reminder is : ",rem)
    # print("befroe sum: ", sum_of_digits)
    sum_of_digits += rem
    # print("After sum", sum_of_digits)
    number = number // 10 # i forgot 1 thing that / this will casse floating number to prevent this use //
    # print("numbe after divition ", number)

print(f"The sum of digits of {number} is = {sum_of_digits}")

# now lets use our python's capabiltiy

number = input("Enter a number ") # the number will input as string
sum = 0

# so now only iterate the whole string
for i in number:
    sum = sum + int(i) # as the i is a string convert in into interger then sum with the sum variable its easy adn simple

print("Number of digits is: ", sum)

# -------------------------------------------------- bonus tip -------------------------------------------------

# my both logic was right but there might be some cases where user might give me invalid input so in these case
if number.isdigit(): # it will check if the string is digit or not if not then it will show an error
    for i in number:
        sum += int(i)
    print("Sum of digits is:", sum)
else:
    print("Invalid input. Please enter digits only.")


# and what if user enter negative values then:
number = input("Enter a number: ")

if number.lstrip('-').isdigit():  # This strips one minus sign before checking
    sum = 0
    for i in number.lstrip('-'):
        sum += int(i)
    print("Sum of digits is:", sum)
else:
    print("Invalid input.")
