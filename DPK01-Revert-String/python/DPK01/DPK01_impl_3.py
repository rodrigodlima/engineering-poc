#!/opt/homebrew/bin/python3

def revert(text):
    result = ""
    i = len(text) - 1
    while i >= 0:
        result += text[i]
        i -= 1
    return result

print (revert("Hello"))