from increaseLetterValue import increaseLetterValue


wordToEncrypt = input("Please give the word you want to encrypt: ")
increaseLetterValue = increaseLetterValue()

def main():
    print(f"our encrypted string is: {increaseLetterValue.encrypt(wordToEncrypt)}")
    print(f"our decrypted string is: {increaseLetterValue.decrypt('yjxy')}")

if __name__ == "__main__":
    main()