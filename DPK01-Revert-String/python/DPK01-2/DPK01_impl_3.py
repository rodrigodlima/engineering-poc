# DPK01 Revert String
# Create a function that can revert a string.
# revert("Hello") -> "olleH"

def revert_string(word):
    result = ""
    for char in word:
        result = char + result
    return result


print(revert_string("Hello"))
