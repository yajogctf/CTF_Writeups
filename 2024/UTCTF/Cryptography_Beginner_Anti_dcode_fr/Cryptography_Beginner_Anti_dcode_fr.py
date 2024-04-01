#!/usr/bin/env python3

with open('LoooongCaesarCipher.txt') as file:
    ct = file.readline().rstrip('\r\n')

for d in range(1, 26):
    print('...')
    pt = ''
    for letter in ct:
        if 'a' <= letter <= 'z':
            pt += chr(((ord(letter) + d - ord('a')) % 26) + ord('a'))
        else:
            pt += letter

    txt = pt.split("utflag{")
    for i in range(1, len(txt)):
        print('d = ',d)
        print('utflag{' + txt[i].split('}')[0] + '}')
