import math

class wordShuffle:
    def __init__(self, columns = 3):
            self.encryptedList = []
            self.decryptedList = []
            self.encryptedString = ""
            self.decryptedString = ""
            self.rows = 0
            self.columns = columns

    def encrypt(self, wordToEncrypt: str) -> str:
        listToEncrypt = list(wordToEncrypt)
        wordLength = len(wordToEncrypt)
        self.rows = math.ceil(wordLength/self.columns)
        
        shuffledWord = [ ['']*self.rows for _ in range(self.columns)]
        for row in range(self.rows):
            for column in range(self.columns):
                if len(listToEncrypt) == 0:
                    break
                shuffledWord[column][row] = listToEncrypt[0]
                listToEncrypt.pop(0)
        
        if len(listToEncrypt) == 0:
            for i in range(len(shuffledWord)):        
                self.encryptedList += shuffledWord[i]
                
        return self.encryptedString.join(self.encryptedList)
    
    def decrypt(self, wordToDecrypt: str) -> str:
        
        return self.decryptedString.join(self.decryptedList)
