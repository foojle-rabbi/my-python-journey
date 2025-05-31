# remove vowels from a sentence
sentence = input("Enter your sentence: ")

without_vowel = ""
vowels = "aeiouAEIOU"

#now iterate the sentence if found vowels then skip
for i in sentence:
    # if('a' and 'e' and 'i' and 'o' and 'u' not in sentence.lower()): # its not right but i was close
    # if i.lower() not in ['a', 'e', 'i', 'o', 'u'] :
    # if i.lower() not in vowels: # lets see if it works or not 
    if i not in vowels:
    #yes its works fine though i include both upper and lower case i dont need to convert it into lower
        without_vowel += i
    
print("Without vowels ", without_vowel)
    
