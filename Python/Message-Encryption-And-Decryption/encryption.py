'''

Created For Mini Projects Repository

Problem: Design an encryption program.

Implementation: Python's encryption model PyCrypto has been used here. The program
generates an encryption key and encrypts the message which is given by the user.
The encryption key and the message are stored in their respective files so that
they can be retrieved by the decryption file. Same key has been used for encryption
and decryption.

@author: Sambit

'''

#Imports
from Crypto.Cipher import AES
import base64
import os

#Functions

#Function to write to a file.
def fileWrite(filename,text):

    '''

        @param Input: The filename in which the given text is to be written
        @none  Output: Text is written in the file.

    '''


    file = open(filename,'w')
    file.write(text)
    file.close

#Function to encrypt a text.
def encryption(privateInfo):

    '''

        @param Input: The message which is to be encrypted.
        @print Output: The encrypted message.

    '''

    BLOCK_SIZE = 16  # 128 bit AES encryption(16 bytes)
    PADDING = '{'

    pad = lambda s: s+(BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    secret = os.urandom(BLOCK_SIZE)
    print 'encryption key:', secret

    fileWrite('key.txt',secret)

    cipher = AES.new(secret)

    encoded = EncodeAES(cipher,privateInfo)

    fileWrite('message.txt', encoded)

    print 'Encrypted string:', encoded

encryption('Test message for encryption. Hopefully it can be read only with the help of decryption file.')
