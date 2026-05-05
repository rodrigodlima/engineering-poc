def revertString(word):
    result=""
    for i in word:
        result=i+result
    return result

print(revertString("Hello"))