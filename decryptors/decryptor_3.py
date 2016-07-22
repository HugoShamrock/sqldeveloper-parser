#!/usr/bin/env python3

# http://stackoverflow.com/questions/1032721/does-anybody-know-what-encrypting-technique-is-jdeveloper-sql-developer-using-to

import os
import pyDes
import binascii


def decrypt(cipherHex, db_system_id):
    cipherText = binascii.unhexlify(cipherHex)
    assert cipherText[0] == 5
    key = cipherText[1:9]
    cipher = pyDes.des(key, mode=pyDes.CBC, IV='\0' * 8, padmode=pyDes.PAD_PKCS5)
    plainText = cipher.decrypt(cipherText[9:]).decode('utf-8')
    return plainText


def encrypt(plainText):
    key = os.urandom(8)
    cipher = pyDes.des(key, mode=pyDes.CBC, IV='\0' * 8, padmode=pyDes.PAD_PKCS5)
    cipherText = b'\5' + key + cipher.encrypt(plainText)
    cipherHex = binascii.hexlify(cipherText)
    return cipherHex


def test(encrypted, decrypted):
    assert decrypt(encrypt(decrypt(encrypted))) == decrypted


if __name__ == '__main__':
    test('0527C290B40C41D71139B5E7A4446E94D7678359087249A463', 'SAILBOAT')
