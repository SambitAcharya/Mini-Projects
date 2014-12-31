'''

Created For Mini Projects Repository

Problem: Design an decryption program.

Implementation: The key and the encrypted text stored in the files are used to
decode the message and print it on the screen,

@author: Sambit

'''

#Imports
from Crypto.Cipher import AES
import base64
import os

#Functions
def decryption(encryptedString):

    '''

        @param Input: The encrypted string from the file
        @print  Output: The decrypted message

    '''

    PADDING = '{'
    DecodeAES = lambda c,e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    file = open('key.txt','r').read()
    key = file
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedString)
    print decoded

mess_file = open('message.txt','r').read()
decryption(mess_file)
