from increaseLetterValue import increaseLetterValue
from wordShuffle import wordShuffle
from key import key
wordToEncrypt = input("Please give the word you want to encrypt: ")
increaseLetterValue = increaseLetterValue()
key = key()

def main():
    # print(f"our encrypted string using the letter value increase is: {increaseLetterValue.encrypt(wordToEncrypt)}")
    # print(f"our decrypted string using the letter value increase is: {increaseLetterValue.decrypt(increaseLetterValue.encrypt(wordToEncrypt))}")
    print(f"our encrypted string using the key encryption is: {key.encrypt(wordToEncrypt)}")
    print(f"our decrypted string using the key encryption is: {key.decrypt('ykssu')}")

if __name__ == "__main__":
    main()