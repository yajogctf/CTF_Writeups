#!/usr/local/bin/python3

# import hmac
# from os import urandom


# class Cipher:
#     def __init__(self, key: bytes):
#         self.key = key
#         self.block_size = 16
#         self.rounds = 1

#     def F(self, x: bytes):
#         return hmac.new(self.key, x, 'md5').digest()[:15]

#     def encrypt(self, plaintext: bytes):
#         plaintext = plaintext.ljust(self.block_size, b'\x00')
#         ciphertext = b''

#         for i in range(0, len(plaintext), self.block_size):
#             block = plaintext[i:i+self.block_size]
#             for _ in range(self.rounds):
#                 L, R = block[:-1], block[-1:]
#                 L, R = R, strxor(L, self.F(R))
#                 block = L + R
#             ciphertext += block

#         return ciphertext


# key = urandom(16)
# cipher = Cipher(key)
# flag = open('flag.txt', 'rb').read().strip()

# print("faked onion")
# while True:
#     choice = input("1. Encrypt a message\n2. Get encrypted flag\n3. Exit\n> ").strip()

#     if choice == '1':
#         pt = input("Enter your message in hex: ").strip()
#         pt = bytes.fromhex(pt)
#         print(cipher.encrypt(pt).hex())
#     elif choice == '2':
#         print(cipher.encrypt(flag).hex())
#     else:
#         break

# print("Goodbye!")

import socket
from Crypto.Util.number import bytes_to_long, long_to_bytes

# caract = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('0'), ord('9') + 1)] + ['}', '{', '_']
# assert caract == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#                   '}', '{', '_']

# conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conn.connect(('chal.amt.rs', 1414))
# rep = conn.recv(1024).decode()
# #print(rep)
# ct_R = {}
# for car in caract:
#     conn.send('1\n'.encode())
#     rep = conn.recv(1024)
#     #print(rep)
#     c = long_to_bytes(ord(car)).rjust(16, b'\x00').hex() + '\n'
#     #print(c)
#     conn.send(c.encode())
#     rep = conn.recv(1024)
#     val = rep.decode().split('\n')[0]
#     #print('---------> ', rep)
#     ct_R[car] = val[2:].encode()
# conn.send('2\n'.encode())
# rep = conn.recv(1024)
# conn.close()

ct_R = {'n': '6e046405a5df0bcd63b7ab861fae9815', # proposer 0000000000000000000000000000006E et récupérer le ct
        'i': '69b4cc41f9e9e0f401d8e3989fa52780',
        '4': '341e5cb4fcb89e43c786adc24703a027',
        'r': '728a26938850992cb6cd4bb7cab2a548',
        'e': '657211c7257ac9e60acd921ea7509d17',
        '}': '7daaf9028db125104709034eace423ed'}
ct = bytes.fromhex('6e650964d1ba7ebf10f4ffc064c1f04a69db932c80b68f9a64878cfec0c478eb3470389999caec1cb4e9dfb03e2fff4172e143f7d73ff71d86a314d4a3c2cd2d652d76a85125a28f3bfcf77af867ae277dc8c861bd')

def strxor(a: bytes, b: bytes):
    return bytes([x ^ y for x, y in zip(a, b)])

BLOCKSIZE = 16
ct_blocks = [ct[i : i + BLOCKSIZE] for i in range(0, len(ct), BLOCKSIZE)]
print('ct_blocks : ', ct_blocks)
pt = b''
for block in ct_blocks:
    #print('block : ', block)
    R, L = block[:1], block[1:]
    #print('R : ', R)
    #print('L : ', L)
    F = bytes.fromhex(ct_R[R.decode()][2:])
    #print('F : ', F)
    L = strxor(L, F)
    #print('L : ', L)
    block_ = L + R
    pt += block_

print(pt.decode())