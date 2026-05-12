def tokenize(text, token):
    tokens = []
    current = ""
    i = 0
    while i < len(text):
        if text[i:i + len(token)] == token:
            tokens.append(current)
            current = ""
            i += len(token)
        else:
            current += text[i]
            i += 1
    tokens.append(current)
    return tokens


if __name__ == "__main__":
    print(tokenize("Hello,World,How,Are,You", ","))
    print(tokenize("Hello World How Are You", " "))
    print(tokenize("Hello-World-How-Are-You", "-"))
