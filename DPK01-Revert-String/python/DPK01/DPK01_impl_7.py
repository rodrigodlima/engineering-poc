from collections import deque

def reverse_string(text):
    d = deque(text)
    d.reverse()
    return ''.join(d)

print(reverse_string("Hello"))