

wordToEncrypt = input("Please give the word you want to encrypt: ")
encryptedList = []
encryptedString = ""

#This is a simple encryption which will just increase the ascii value of a letter
def increaseLetterValue(wordToEncrypt: str):
    listOfChars = list(wordToEncrypt)
    for i, char in enumerate(listOfChars):
        encryptedChar = ord(char)
        if(encryptedChar+5 > 122):
            encryptedChar = ord(char) - 26
        encryptedList.append(chr(encryptedChar + 5))
    
    return encryptedString.join(encryptedList)




print(f"our encrypted string is: {increaseLetterValue(wordToEncrypt)}")