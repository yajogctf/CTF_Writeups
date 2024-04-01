#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import pwn

seed = 0

def get_random_number():
    global seed 
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def decrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.decrypt(pad(message, AES.block_size))
    return ciphertext

def get_key():
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    return key

proc = pwn.remote('betta.utctf.live', 7356)
proc.recvuntil(b'What would you like to do (1 - get encrypted flag, 2 - encrypt a message)?')
proc.sendline(b'1')
proc.recvline()
rep = proc.recvline()
ct = bytes.fromhex(rep.decode().rstrip('\r\n').split(' ')[-1])
print('reception : ', rep)
print('CypherText :', rep.decode().rstrip('\r\n').split(' ')[-1])

for s in range(1000000):
    seed = s
    key = get_key()
    pt = decrypt(ct, key)
    if b'utflag{' in pt :#or b'ctf' in pt:
        print(pt)
        break
