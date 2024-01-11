import random

#small script to brute force a string, used hello world as an example
#there are 2 methods, the Quick is is rather quick and checks letter by letter
#whilst the Slow method tries to bruteforce the entire string at once which is extremely slow because it 
#will most likely repeat attempts alot

def QuickMethod():
    stringToFind = "helloworld"
    stringToArray = list(stringToFind)
    foundChars = []
    tries = 0
    for i in range(len(stringToArray)):
        while True:
            randomChar = chr(random.randint(97, 122))
            if randomChar == stringToArray[i]:
                print("we found the letter: " + randomChar)
                foundChars.append(randomChar)
                break
            tries += 1
    print(f"\nwe have found: {foundChars}")
    print(f"which translates to: {stringToFind}")
    print(f"in {tries} attempts")

def SlowMethod():
    x = True
    helloWorldString = ""

    while x:
        for i in range(8):
            helloWorldString += chr(random.randint(97, 122))
            
        print(helloWorldString)
        if helloWorldString == "helloworld":
            x = False
        helloWorldString = ""

    print(helloWorldString)


QuickMethod()
