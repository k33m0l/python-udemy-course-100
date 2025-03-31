def encrypt(to_encrypt, shift_num):
    response = []
    for c in to_encrypt:
        response += chr(ord(c) + shift_num)
    return ''.join(response)

mode = input("Type 'encode' to encrypt or type 'decode' to decrypt ")
shift_num = int(input("Enter the shift number: "))
text = input("Type text: ")

if mode == "encode":
    print(f"Encrypted message is \"{encrypt(text, shift_num)}\"")
elif mode == "decode":
    print(f"Decrypted message is \"{encrypt(text, -shift_num)}\"")
else:
    print("Mode unrecognized, exciting")