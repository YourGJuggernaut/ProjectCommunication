import numbin # type: ignore
import rulecrypter # type: ignore

bintonum = numbin.bintonum
getkey = numbin.getkey
wipekey = numbin.wipekey
rem = numbin.rem

decry = rulecrypter.decry
removekey = rulecrypter.removekey
decryptthem = rulecrypter.decryptthem
dnx = rulecrypter.dnx
unopt = rulecrypter.unopt
enx = rulecrypter.enx
tmp = rulecrypter.tmp
red = rulecrypter.red



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
    passed = True
    temp1 = key
    content = dnx()
    tmp(content)
    t22 = red()
    towir = str(t22)
    wipekey(key)
    t22 = red()
for _ in range(4):
    bol = False

    with open('DataOUT.pycomm', 'w'):
        pass




    if passed:

        # CHAT GPT START ---
        # Split the binary string into groups of 5 bits
        binary_chunks = [t22[i:i+5] for i in range(0, len(t22), 6)]
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
    rem()
    if decryptthem():
        removekey()
    else:

        with open('DataEN.pycomm', 'w') as file:
            pass
        with open('DataEN.pycomm', 'a', encoding='utf-8') as file:
            pass
            unopt(towir)
#   addtag()
    print("Fully Succesfull")
