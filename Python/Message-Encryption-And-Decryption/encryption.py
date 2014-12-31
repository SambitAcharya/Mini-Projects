from Crypto.Cipher import AES
import base64
import os

def encryption(privateInfo):
    BLOCK_SIZE = 16
    PADDING = '{'

    pad = lambda s: s+(BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    secret = os.urandom(BLOCK_SIZE)
    print 'encryption key:', secret

    file = open('key.txt','w')
    file.write(secret)
    file.close

    cipher = AES.new(secret)

    encoded = EncodeAES(cipher,privateInfo)

    file = open('message.txt','w')
    file.write(encoded)
    file.close

    print 'Encrypted string:', encoded

encryption('Test message for encryption. Hopefully it can be read only with the help of decryption file.')from Crypto.Cipher import AES
import base64
import os

def encryption(privateInfo):
    BLOCK_SIZE = 16
    PADDING = '{'

    pad = lambda s: s+(BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    secret = os.urandom(BLOCK_SIZE)
    print 'encryption key:', secret

    file = open('key.txt','w')
    file.write(secret)
    file.close

    cipher = AES.new(secret)

    encoded = EncodeAES(cipher,privateInfo)

    file = open('message.txt','w')
    file.write(encoded)
    file.close

    print 'Encrypted string:', encoded

encryption('Test message for encryption. Hopefully it can be read only with the help of decryption file.')
