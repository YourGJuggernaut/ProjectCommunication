def getkey(key):
    string = ""
    with open('dataEN.pycomm', 'r') as file:
        securitycontent = file.read()
    for i in range (0, len(key)):
        try:
            string = string + securitycontent[i]
        except Exception as e:
            return False
    if string == key:
        return True
    else:
        return False
# used ChatGPT as Idea
def wipekey(enc):
    string = ""
    with open('dataEN.pycomm', 'r') as file:
        securitycontent = file.read()
    for i in range(0, len(enc)):
        string = string + securitycontent[i]
    modded = securitycontent.replace(string, '')
    
    with open('dataEN.pycomm', 'w') as file:
        file.write(modded)
    with open('key.key', 'w') as file:
        pass


def bintonum(bininput):
    bininput = str(bininput) 
    templen = len(bininput)
    suma = 0
    j = 0
# Converted from Basic To Python using ChatGPT
    for i in range(templen - 1, -1, -1):
        j += 1
        if bininput[i] == '1':
            suma += 2 ** (j - 1)

    return suma
# Used ChatGPT for byte Fill
def numtobin(numinput):
    if numinput == 0:
        return "00000"
    
    binary = ""
    while numinput > 0:
        binary = str(numinput % 2) + binary
        numinput = numinput // 2
    
    return binary.zfill(5)