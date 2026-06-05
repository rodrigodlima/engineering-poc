def revert_string(word):
    result = ""
    for char in word:
        result = char + result
    return result


print(revert_string("Hello"))