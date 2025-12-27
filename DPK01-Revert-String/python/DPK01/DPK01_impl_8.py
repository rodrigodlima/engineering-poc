def reverse_string(text):
    stack = []
    for char in text:
        stack.append(char)
    
    result = ''
    while stack:
        result += stack.pop()
    return result

print (reverse_string("Hello"))