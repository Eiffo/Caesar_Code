def decrypting(text):
    cipher = ""
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        cipher += chr(code)
    print("Decrypted code:\n" + cipher.title())