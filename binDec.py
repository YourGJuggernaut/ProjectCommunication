from numbin import bintonum, getkey, wipekey  # type: ignore
import os
with open('key.key', 'r') as file:
    key = file.read()
passed = False
if key == "":
    print("no password")
else:
    inputkey = input('What is the key: ')

for _ in range(2):
    bol = False

    with open('DataOUT.pycomm', 'w'):
        pass

    with open('DataEN.pycomm', 'r') as file:
        content = file.read()
    with open('key.key', 'r') as file:
        key = file.read()

    state = getkey(key)
    if getkey(key) and key == inputkey:
        wipekey(key)
        passed = True
    if getkey(key) and key == inputkey:
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
        # - mine


if not passed:
    print('key not correct')
if passed:
    with open('DataEN.pycomm', 'w') as file:
        pass
    os.remove("key.key")
