def encrypt():
    from cryptography.fernet import Fernet # type: ignore
    with open('key.key', 'r') as file:
        content = file.read()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    content = content.encode('utf-8')
    cipher_text = cipher_suite.encrypt(content)
    with open('key.key', 'w') as file:
        pass
    with open('key.key', 'wb') as file:
        file.write(cipher_text)
    with open('dual.key', 'wb') as file:
        file.write(key)

def decry():
    from cryptography.fernet import Fernet # type: ignore
    with open('dual.key', 'r') as file:
        content = file.read()
    with open('key.key', 'r') as file:
        content2 = file.read()
    fernet = Fernet(content)
    decrypt = fernet.decrypt(content2).decode()
    return decrypt

def encryptthem(Bool):
    from cryptography.fernet import Fernet # type: ignore
    with open('dual.key', 'r') as file:
        key = file.read()
    cipher = Fernet(key)
    content = Bool.encode('utf-8')
    text = cipher.encrypt(content)
    return text

def decryptthem():
    from cryptography.fernet import Fernet # type: ignore
    with open('dual.key', 'r') as file:
        key = file.read()
    with open('metadata.key') as file:
        Bool = file.read()
    cipher = Fernet(key)
    content = cipher.decrypt(Bool).decode()
    if content == "True":
        return True
    else:
        return False

def removekey():
    import os
    os.remove("key.key")
    os.remove("dual.key")
    os.remove("metadata.key")
    os.remove("DataEN.pycomm")