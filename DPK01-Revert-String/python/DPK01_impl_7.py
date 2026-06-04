def revert_string(word):
    result = ""
    for i in word:
        result = i + result
    return result


print(revert_string("Hello"))