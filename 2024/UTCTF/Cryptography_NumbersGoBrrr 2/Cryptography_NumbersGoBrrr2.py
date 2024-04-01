#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import random
import pwn

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

proc = pwn.remote('betta.utctf.live', 2435)
proc.recvline() # b'Thanks for using our encryption service! To get the start guessing, type 1. To encrypt a message, type 2.\n'
proc.recvline() # b'You will need to guess the key (you get 250 guesses for one key). You will do this 3 times!\n'

for _ in range(3):
    proc.recvline() # b'Find the key 1 of 3!\n'
    proc.recvline() # b'What would you like to do (1 - guess the key, 2 - encrypt a message)?\n'
    proc.sendline(b'2') 
    proc.recvline() # b'What is your message?\n'
    proc.sendline(b'Hello_world')
    rep = proc.recvline().decode().rstrip('\r\n') # b'Here is your encrypted message: 789421ca2362e655e47f18b1ee3e35f4\n'
    proc.recvline() # b'What would you like to do (1 - guess the key, 2 - encrypt a message)?\n'
    proc.sendline(b'1')
    proc.recvline() # b'You have 250 guesses to find the key!\n'
    proc.recvline() # b'What is your guess (in hex)?\n'

    ct = bytes.fromhex(rep.split(' ')[-1])

    for s in range(1000000):
        seed = s
        key = get_key()
        pt = decrypt(ct, key)
        if b'Hello' in pt:
            break
    proc.sendline(key.hex().encode())
    print(proc.recvline()) # b'You found the key!\n'
    
print(proc.recvline()) # b'Here is the flag: utflag{ok_you_are_either_really_lucky_or_you_solved_it_as_intended_yay}\n'