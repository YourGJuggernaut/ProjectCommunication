from numbin import bintonum, getkey, wipekey  # type: ignore
from rulecrypter import checktag, addtag, decry, secret, removekey # type: ignore
import os
key = decry()
passed = False
passi = False
if key == "":
    print("no password")
    inputkey = ""
else:
    inputkey = input('What is the key: ')

state = getkey(key)
if getkey(key) and key == inputkey:
    wipekey(key)
    passed = True

for _ in range(2):
    bol = False

    with open('DataOUT.pycomm', 'w'):
        pass

    with open('DataEN.pycomm', 'r') as file:
        content = file.read()


    if passed:
        # CHAT GPT START ---
        # Split the binary string into groups of 5 bits
        binary_chunks = [content[i:i+5] for i in range(0, len(content), 6)]
        decoded_string = ""
        for chunk in binary_chunks:
        # CHAT GPT END ---
            # Convert each 5-bit binary chunk back to decimal
            # - mine
            if chunk == "SPACE":
                decoded_string += " "
                continue
            elif chunk == "ENTER":
                decoded_string += "\n"
                continue
            elif chunk == "SHIFT":
                bol = True
                continue
            decimal_value = bintonum(chunk)
            if bol:
                decoded_string += chr(decimal_value + 65)
                bol = False
            else:
                decoded_string += chr(decimal_value + 97)
        with open('DataOUT.pycomm', 'a', encoding='utf-8') as file:
            file.write(decoded_string)

    Passi = True
        # - mine
if not passed:
    print('key not correct')
#if checktag() == secret():
#    passed = False
#    print("Arleady used, re-allow decryption")
if passed:
#   removekey()
#   addtag()
    print("Fully Succesfull")
