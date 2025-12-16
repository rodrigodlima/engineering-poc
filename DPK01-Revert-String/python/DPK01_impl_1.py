#!/opt/homebrew/bin/python3

def RevertString(word):
    result = ""
    for char in word:
        result = char + result
    print (result)
        

RevertString("Hello")
