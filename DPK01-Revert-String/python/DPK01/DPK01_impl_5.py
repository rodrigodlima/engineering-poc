def reverse_string(word):
    return ''.join([word[i] for i in range(len(word)-1, -1, -1)])

print (reverse_string("Hello"))