#!/usr/bin/env python3

# https://github.com/maaaaz/sqldeveloperpassworddecryptor

from Crypto.Cipher import DES
import base64
import hashlib
import binascii


def decrypt(encrypted, db_system_id):
    def unpad(s):  # unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        return s[:-ord(s[len(s) - 1:])]
    encrypted = base64.b64decode(encrypted)
    db_system_id = db_system_id.encode('utf-8')
    # salt = '051399429372e8ad'.decode('hex')  # python2
    salt = binascii.unhexlify('051399429372e8ad')  # python3
    key = db_system_id + salt
    for i in range(42):
        moo = hashlib.md5(key)
        key = moo.digest()
    cipher = DES.new(key=key[:8], mode=DES.MODE_CBC, IV=key[8:])
    decrypted = cipher.decrypt(encrypted)
    return unpad(decrypted).decode('utf-8')

if __name__ == '__main__':
    assert decrypt(
        encrypted='rZOwZ6vE5zk=',
        db_system_id='6e0c2564-1351-4df9-b165-b52cbc74d258',
    ) == 'heslo'
