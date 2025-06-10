from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s,key):
    encrypted = []
    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            new_index = (index + key) % 26
            encrypted.append(ascii_lowercase[new_index])
        elif char in ascii_uppercase:
            index = ascii_uppercase.index(char)
            new_index = (index + key) % 26
            encrypted.append(ascii_uppercase[new_index])
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def caesar_cypher_decrypt(s, key):
    decrypted = []
    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            new_index = (index - key) % 26
            decrypted.append(ascii_lowercase[new_index])
        elif char in ascii_uppercase:
            index = ascii_uppercase.index(char)
            new_index = (index - key) % 26
            decrypted.append(ascii_uppercase[new_index])
        else:
            decrypted.append(char)
    return ''.join(decrypted)

📌
