def encrypting(text):
    cipher = ""
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    print("Encrypted code:\n" + cipher.title())