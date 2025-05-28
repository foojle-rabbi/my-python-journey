# accha python er moddhe slicing technique tha korai. abar tar upor ache negetive slicing;
# toh eitar moddhe amra [start:ending] dite parbo. eita valid jeikono size theke jei kono size hoite pare
# abar ei same slicing technique use kore amra char skip o korte pari. eita kaj kore 
# [start:end: koto index por por skip korte chao / ba koto index por por value print korba] 

# suppose amar kache ekta string s = "MyNameIsFojle" dhoro ei string ache. ekhon ami jodi [0:13:2] likhi
# tahole amar start theke shururu kore 13 porjonto jabe then proti 2 index por por char print korbe 
# tahole amader output ashar kotha : MNmIFje

s = "MyNameIsFojle"

print(s[0:13:2])

string = input("Enter a string ")
# print("Skiping skip every 2nd character ", string[0:string.len():2]) # accha ami eikhane len() vul vabe use kortechi

# right way to get the len of a string is len(string_name)
print("Skiping skip every 2nd character ", string[0:len(string):2])

# hah ha tobe jnao er thekeo short form e ber kora jay
print("Skipping every 2nd character:", string[::2]) # nothing means start form 0 and end; 