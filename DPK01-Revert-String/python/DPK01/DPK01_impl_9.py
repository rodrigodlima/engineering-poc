def reverse_string(text):
    b = bytearray(text, 'utf-8')
    b.reverse()
    return b.decode('utf-8')

print(reverse_string("Hello"))