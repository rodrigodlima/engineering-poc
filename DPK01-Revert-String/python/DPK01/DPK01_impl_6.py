from functools import reduce

def reverse_string(text):
    return reduce(lambda x, y: y + x, text)

print(reverse_string("Hello"))