string = input("Enter a string: ")

# print(f"the middle char of {string} is {string[(len(string) )/ 2]}") 
# uporer amader vul hocche amra length integer ke 2 diye divide kore index hisebe use kortechi jeta ekta 
# mistake cause onek shomoy value floating e ashte pare. so floating toh index hisebe use hoy na. she jonno error.

#  so ei problem solve korar jonno python e khub nice and effective operator ache : // eita diye divide korle amader
# float er porer value ashbe na. eikhane shudhu ineter part ta ashbe. jokhon amra floaing niye kaj korbo na. ba index niye 
# kaj korbo tokhon amra ei // operator use korbo. its called "floor division operator."

middle_index = len(string) // 2
print(f"the middle char of {string} is {string[middle_index]}") 