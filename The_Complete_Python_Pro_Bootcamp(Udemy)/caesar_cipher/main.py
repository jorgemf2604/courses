# Caesar Cipher commnad line application by Jorge Martin Fernandez

import os

# globals
alphabet = "abcdefghijklmnopqrstuvwxyz"


# helper functions


def ask_for_msg():
    message = input("Type your message: ")
    return message


def ask_for_key():
    return int(input("Type the shift number: "))


def encode_decode(message, operation):
    key = ask_for_key()
    new_message = ""
    for char in message.lower():
        # dealing with spaces
        if char == " ":
            new_message += " "
            continue
        # get position in the alphabet
        index = alphabet.index(char)
        # shifting key
        if operation == "encode":
            new_char = alphabet[(index+key) % len(alphabet)]
        elif operation == "decode":
            new_char = alphabet[(index-key) % len(alphabet)]
        new_message += new_char
    return new_message


def main():
    print("🏛️  Welcome to the Ceasar Cipher 2000! 🏛️")
    keep_asking = True
    while keep_asking:
        msg = None
        user_choice = input(
            "Type 'encode' to encrypt, type 'decode' to decript , type anything else to exit: ").lower()
        if user_choice == "encode":
            msg = ask_for_msg()
            print(
                f"Here is the encoded result: {encode_decode(msg, 'encode')}\n")
        elif user_choice == "decode":
            msg = ask_for_msg()
            print(
                f"Here is the decoded result: {encode_decode(msg, 'decode')}\n")
        else:
            keep_asking = False
            os.system("clear")
            print("Thanks for using the Caesar Cipher 2000.")


main()
