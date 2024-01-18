#This is a simple encryption which will just increase the ascii value of a letter
class increaseLetterValue:
    def __init__(self):
        self.encryptedList = []
        self.decryptedList = []
        self.encryptedString = ""
        self.decryptedString = ""
        self.valueIncrease = 5
        

    def encrypt(self, wordToEncrypt: str) -> str:
        listOfChars = list(wordToEncrypt)
        for i, char in enumerate(listOfChars):
            encryptedChar = ord(char)
            if(encryptedChar+self.valueIncrease > 122):
                encryptedChar = ord(char) - 26
            self.encryptedList.append(chr(encryptedChar + self.valueIncrease))
        
        return self.encryptedString.join(self.encryptedList)
    
    def decrypt(self, wordToDecrypt: str) -> str:
        listOfChars = list(wordToDecrypt)
        for i, char in enumerate(listOfChars):
            decryptedChar = ord(char)
            if(decryptedChar-self.valueIncrease < 97):
                decryptedChar = ord(char) + 26
            self.decryptedList.append(chr(decryptedChar - self.valueIncrease))

        return self.decryptedString.join(self.decryptedList)
