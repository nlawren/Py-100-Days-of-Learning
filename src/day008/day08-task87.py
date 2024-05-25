# Day 8 - Function Parameters and Caesars Cipher
# Task 87 - Caesar Cipher Part 2 - Decryption
# References:
# https://en.wikipedia.org/wiki/Caesar_cipher
# https://www.w3schools.com/python/ref_list_index.asp
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encrypt(plain_text, shift_index):
    cipher_text = ""
    for index in plain_text:
        position = alphabet.index(index)
        cipher_position = int((position + shift_index) % 26)
        cipher_message = alphabet[cipher_position]
        print(
            f"Plain text is {index}, position {position}, cipher text is {cipher_message}"
        )
        cipher_text += cipher_message
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_index):
    plain_text = ""
    for index in cipher_text:
        position = alphabet.index(index)
        plain_position = int((position - shift_index) % 26)
        plain_message = alphabet[plain_position]
        print(
            f"Cipher text is {index}, position {position}, cipher text is {plain_message}"
        )
        plain_text += plain_message
    print(f"The decrypted text is {plain_text}")


print("Day 8 - Ceasars Cipher - Task 87\n")
loop = True

while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if "code" in direction:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(plain_text=text, shift_index=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, shift_index=shift)
    else:
        print("\nGoodbye\n")
        loop = False

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet
# by the shift amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction'
# variable. Then call the correct function based on that 'drection' variable. You should be able
# to test the code to encrypt *AND* decrypt a message.
