from numbin import bintonum # type: ignore
bol = False

with open('DataDE.txt', 'w') as file:
    pass

with open('DataEN.txt', 'r') as file:
    content = file.read()
# CHAT GPT START ---
# Split the binary string into groups of 5 bits
binary_chunks = [content[i:i+5] for i in range(0, len(content), 6)]

decoded_string = ""
for chunk in binary_chunks:
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
    else:
        decimal_value = bintonum(chunk)
        if bol:
            decoded_string += chr(decimal_value + 65)
            bol = False
        else:
            decoded_string += chr(decimal_value + 97)
    # - mine
# Write the decoded string to DataDE.txt
with open('DataDE.txt', 'a', encoding='utf-8') as file:
    file.write(decoded_string)
# CHAT GPT END ---
