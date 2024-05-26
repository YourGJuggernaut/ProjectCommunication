from numbin import numtobin # type: ignore
from rulecrypter import removetag, encrypt # type: ignore
key_string = input('insert KEY: ')
with open('DataEN.pycomm', 'w') as file:
    pass

with open('dataIN.pycomm', 'r') as file:
    content = file.read()  
with open('key.key', 'w') as file:
    pass
#removetag("ENCBYPASS ")

with open ('key.key', 'a') as file:
    file.write(key_string)
encrypt()
with open ('DataEN.pycomm', 'a') as file:
    file.write(key_string)
    for letter in content:
        if letter == letter.upper() and letter != " ":
            file.write("SHIFT" + "\n")
        if letter.isalpha():
            value = ord(letter.lower()) - 97
            c = numtobin(value)
            file.write(c + "\n")
        if letter == " ":
            file.write("SPACE" + "\n")
        if letter == "\n":
            file.write("ENTER" + "\n")