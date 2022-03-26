from Encrypting import encrypting
from Decrypting import decrypting

print("-" * 20)
print("Code Caesar".center(18))
print("-" * 20)

print("1. Encrypting.")
print("2. Decrypting.")
choice = input("Choose number: ")

if choice == "1":
    text = input("\nEnter text to be encrypted:\n")
    encrypting(text)
elif choice == "2":
    text = input("\nEnter text to be decrypted:\n")
    decrypting(text)
else:
    print("\nChoose between 1 or 2!")