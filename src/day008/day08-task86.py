# Day 8 - Function Parameters and Caesars Cipher
# Task 86 - Caesar Cipher Part 1 - Encryption
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


def encrypt(text, shift):
    cipher_text = []
    for index in text:
        position = alphabet.index(index)
        cipher_position = int((position + shift) % 26)
        cipher_message = alphabet[cipher_position]
        print(
            f"Plain text is {index}, position {position}, cipher text is {cipher_message}"
        )
        cipher_text += cipher_message
    print(f"The encoded text is {''.join(cipher_text)}")


print("Day 8 - Ceasars Cipher - Task 86\n")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet
# by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# TODO-3: Call the encrypt function and pass in the user inputs.
# You should be able to test the code and encrypt a message.
