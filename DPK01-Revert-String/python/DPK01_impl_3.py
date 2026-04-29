def revertString(word):
    result = ""
    for char in word:
        result = char + result
    print(result)


revertString("hello")
