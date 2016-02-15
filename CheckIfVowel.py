#write a function that takes a character (i.e. a string of length 1)
# and returns true if it is a vowel, false otherwise.

checkIfVowel=()

checkIfVowel=input("Write a single character: ")

if (checkIfVowel.upper())=="A" or (checkIfVowel.upper())=="O" or (checkIfVowel.upper())=="E" or (checkIfVowel.upper())=="I" or (checkIfVowel.upper())=="U":
    print("TRUE")
else:
    print("FALSE")
