def reverseString(word):
    if len(word) <= 1:
        return word
    return word[-1] + reverseString(word[:-1])

print (reverseString("Hello"))