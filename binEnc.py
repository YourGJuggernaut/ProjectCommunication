import os
from numbin import bintonum, numtobin

with open('DataEN.txt', 'w') as file:
    pass

with open('dataDE.txt', 'r') as file:
    content = file.read()  

with open ('DataEN.txt', 'a') as file:
    for letter in content:
        if letter.isalpha():
            value = ord(letter.lower()) - 97
            c = numtobin(value)
            file.write(c + "\n")
        if letter == " ":
            file.write("SPACE" + "\n")
        if letter == "\n":
            file.write("ENTER" + "\n")