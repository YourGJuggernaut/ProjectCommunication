from numbin import numtobin # type: ignore
from rulecrypter import encrypt, encryptthem # type: ignore
key_string = input('Set KEY/Password (Can Be Blank for non!): ')

getstate = input('\n Is this One time use- True or All Time use- False (True/False): ')
if getstate == "True" or getstate == "true":
    boolean = True
elif getstate == "False" or getstate == "false":
    boolean = False
else:
    print("True or False only!")
    exit()

with open('DataEN.pycomm', 'w') as file:
    pass

with open('dataIN.pycomm', 'r') as file:
    content = file.read()  
with open('key.key', 'w') as file:
    pass

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
with open('metadata.key', 'w') as file:
    pass
if boolean:
    f = encryptthem('True')
    with open('metadata.key', 'wb') as file:
        file.write(f)
else:
    f = encryptthem('False')
    with open('metadata.key', 'wb') as file:
        file.write(f)