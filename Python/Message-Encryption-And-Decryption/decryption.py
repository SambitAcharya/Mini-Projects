from Crypto.Cipher import AES
import base64
import os

def decryption(encryptedString):
    PADDING = '{'
    DecodeAES = lambda c,e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    file = open('key.txt','r').read()
    key = file
    file.close()
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedString)
    print decoded

file = open('message.txt','r').read()
decryption(file)
file.close()
