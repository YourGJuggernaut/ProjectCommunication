# ProjectCommunication

ProjectCommunication
A Python Communication Project

I am still a beginner in programming, so this is one of my bigger projects.

For those who might not be familiar with coding, let me explain:

This is a simple project focused on communication. It's just the beginning, but here's what it does for now:

### About the Project
This project is currently a binary-string converter:
- **DataIN**: Input for about to be decoded data
- **DataEN**: Encoded data
- **DataOUT**: Output for decoded data
- **Any Code, For my sake of learning, Generated by ChatGPT is highlighted**
### Key Components
#### `binEnc.py`
This script takes letters from `DataIN`, converts them to binary, and saves them to `DataEN`. It processes each letter sequentially.

#### `binDec.py`
This script takes 6-bit binary chunks, converts them to letters, and saves them to `DataOUT`. It processes each chunk sequentially.

### The Alphabet System
1. Convert a 5-bit binary to a number.
2. Add 96 to the number.
3. Convert the result to an ASCII character.

**Example:**
- `00001` = 1 + 97 = ASCII(98) = 'b'


# Output
- **If you want to send somebody This encrypted mess you must send the following:**
1. DataEN.pycomm (The Actuall File)
2. dual.key (The cryptography key)
3. key.key (The Password)
4. metadata.key (Attributes)
- **This will the basic principle of how my Communication will work**
# Features
- **Detection of newline characters (`\n`)**: **DONE**
- **Detection of spaces**: **DONE**
- **Addition of symbols**: *In Progress*
- **Addition of uppercase letters**: **DONE**
- **Addition of numbers**: *In Progress*
- **Encryption of keys**: **DONE**
- **One-time Key + All-time Key**: **DONE**
- **Encryption of Encoded Material**: *In progress*

# **NEW** Security
- When Encoding, You enter a key. A file named key.key gets saved with that key. When it gets encrypted it also puts the key in the dataEN.pycomm
- When Decoding, You enter a key. Checks for if key.key == dataEN.pycomm (key) == user input. If all correct it runs it 2 times (To be trouble shooted) and Deletes the key.key
- Key is now Encrypted using Fernet
- 2 Keys now
# LICENSE USE:
1. What You Can Do:
- Use the software for any purpose
- Modify the software
- Distribute copies of the software to others.
- use the software into your own projects
2. What you Can't Do:
- Remove the license notice
- Impose additional restrictions on recipients' rights granted by the GPL.
3. What you Must Note:
- Any modifications or derivatives of the software must be licensed under the GPL.
- Provide access to the corresponding source code if distributing the software or any modifications.
- Include a copy of the GPL license with any distribution of the software.
- The software has no warranty.




# Updates

- **May 19, 2024, 2:46 AM** - Initial version of ProjectCommunication.
- **May 20, 2024, 12:34 PM** - Fixed Some things + Uppercase.
- **May 20, 2024, 8:26 PM** - Added More Security Mesures part 1 (file extension)
- **May 20, 2024, 10:40 PM** - Added More Security Mesures part 2 (Key)
- **May 26, 2024, 1:10 PM** - Added More Security Measures to the Key + One/All Time key + Some optimizations to the Decoder
