#1st proyect
#Simple Cipher
#The user gives a sentence then a number that will indicate the displacement of the letters  in the given sentence

#startingg with a message of what the program is about and asking for the inputs
print("Simple Cipher(Caesar Cipher): Give a sentence then this program will displace the letters of your sentence")
print("")
sentence = str(input("Write your sentence: "))
num_displa = int(input("How much displacement do you want? "))

alphabet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
]

#this functions make the work more easy and more clean and oranized
def new_senten():
    #a variable for the new sentence
    new_senten = ""

    #divides the sentences into characters
    for char in sentence:
        #add the characters one by one
        new_senten += displacement(char,num_displa)
    #this print the sentence when it is done and when you call the new_senten function
    print(new_senten)

def displacement(char,num_displa):
    #if the characters is not a letter it just return the character like symbols, space and numbers
    if char not in alphabet:
        return char
    
    #this line identifice what index the letter(char) have in the alphabet list, and converts the characters into lowercase letters
    index_char = alphabet.index(char.lower())
    #these lines change the index for the new one addingg the number of displacement that the user put and also looks if the result is not more than 26(# of letters in the alphabet), and if it is more it just return subtract 26 to the index once 
    n_index = index_char + num_displa
    if n_index >= len(alphabet):
        n_index -= len(alphabet)
    
    #this line puts the new char in a variable searching in the alphabet with the new index 
    new_char = alphabet[n_index]

    #this returns the new character in uppercase if it was uppercase, if not it just  return the character
    return new_char.upper() if char.isupper() else new_char

#this  print the  messae with the new sentence
print("Your new sentence is:")
new_senten()