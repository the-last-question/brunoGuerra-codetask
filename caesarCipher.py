def cesar_cryptography(msg):
    encryptedText = ""
    for letter in msg:
        encryptedText = encryptedText + chr((ord(letter) - ord("A") + 3) % 26 + ord("A"))

    return encryptedText

phrase = input("Escreva uma mensagem ")
phrase = phrase.upper();
print(cesar_cryptography(phrase))