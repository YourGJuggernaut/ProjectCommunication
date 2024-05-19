import os
from numbin import numtobin # type: ignore

with open('DataEN.pycomm', 'w') as file:
    pass

with open('dataDE.pycomm', 'r') as file:
    content = file.read()  

with open ('DataEN.pycomm', 'a') as file:
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
