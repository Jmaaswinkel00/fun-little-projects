#For this encryption you give a key, and that key will transform your work into something else
#it will count the ascii value of the key, divide that by 26 (the amount of letters)
#and then it will add that number to the current ascii value and create a new letter
class key:
    def __init__(self):
        self.encryptedList = []
        self.decryptedList = []
        self.encryptedString = ""
        self.decryptedString = ""
        self.key = "key"

    def encrypt(self, wordToEncrypt: str) -> str:
        listToEncrypt = list(wordToEncrypt)
        while True:
            for char in self.key:
                if len(listToEncrypt) == 0:
                    return self.encryptedString.join(self.encryptedList)
                
                char = ord(char) - 97
                charToEncrypt = ord(listToEncrypt[0])
                
                for _ in range(char):
                    if charToEncrypt == 97:
                        charToEncrypt = 122
                    charToEncrypt -= 1
                
                self.encryptedList.append(chr(charToEncrypt))
                listToEncrypt.pop(0)

    def decrypt(self, wordToDecrypt: str) -> str:
        listToDecrypt = list(wordToDecrypt)
        while True:
            for char in self.key:
                if len(listToDecrypt) == 0:
                    return self.decryptedString.join(self.decryptedList)
                
                char = ord(char) - 97
                charToDecrypt = ord(listToDecrypt[0])
                
                for _ in range(char):
                    if charToDecrypt == 122:
                        charToDecrypt = 97
                    charToDecrypt += 1
                
                self.decryptedList.append(chr(charToDecrypt))
                listToDecrypt.pop(0)