def revertString(word):
    result=""
    for char in word:
        result = char + result
    return result


print(revertString("Hello"))