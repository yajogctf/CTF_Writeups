# import random
# 
# with open("test2.py", "r") as f:
#     lines = f.readlines()
# 
# longest = 0
# 
# for i in lines:
#     i = i.replace("\n", " ")
#     if len(i) > longest:
#         longest = len(i)
# 
# print(lines)
# 
# padLines = []
# 
# for i in lines:
#     padLines.append(i.replace("\n"," ") + " " * (longest - len(i)))
#     print(i)
# 
# print(padLines)
# 
# split = ["" for _ in range(longest)]
# 
# for line in padLines:
#     for i in range(longest):
#         split[i] += line[i]
#         split[i] += "\n"
# 
# print(split)
# 
# split.pop()
# 
# print(split)
# 
# random.shuffle(split)
# 
# '''for j in range(len(split[0])):
#     for i in split:
#         if i[j] != "\n":
#             print(i[j], end="")
#     print()'''
# #block to print out the shredded file
# 
# for i in range(len(split)):
#     fname = "./files/shred" + str(i) + ".txt"
#     with open(fname, "w") as f:
#         f.write(split[i])
# 
# print("Shredded file into " + str(longest-1) + " shreds")


"""
Picking up the pieces
"""
ordre = [2, 4, 18, 31, 19, 21, 13, 5, 12, 30, 27, 28, 25, 9, 16,
         6, 26, 24, 17, 29, 11, 14, 1, 3, 15, 7, 32, 0, 20, 23, 10, 8, 22]
        # Obtained by tapping from a list ranging from 0 to 32.
        
contenu_ordonne = [None for _ in range(33)]
for i in range(33):
    with open("shred" + str(ordre[i]) + ".txt", "r") as f:
        lines = f.readlines()
    contenu_ordonne [i] = lines
lignes = ['' for i in range(len(contenu_ordonne[0]))]
for c in range(33):
    for l in range(len(contenu_ordonne[0])):
        lignes[l] = lignes[l] + contenu_ordonne[c][l].rstrip('\r\n')
        
# Displaying the resulting C program
with open("shredded.c", "w") as f:
    for l in lignes:
        f.write(l + '\n')
# for l in lignes:
#     print(l)
    
"""
Python programming of the program written in C.
This helps to understand the program, but is not mandatory for solving it.
Here's an example of a flag : wctf{l_mauvais_flag}
"""
flag = "wctf{l_mauvais_flag}".encode()
inter = [None for _ in range(51)]
lon = len(flag)

for i in range(lon):
    inter[i] = flag [i]

for i in range(lon, 50):
    inter[i] = inter[(i * 2) % lon]
    
inter[50] = '\0'

a = ''
for i in range(50):
    a = inter[i]
    inter[i] = inter[((i + 7) * 15) % 50]
    inter[((i + 7) * 15) % 50] = a

for i in range(50):
    a = inter[i]
    inter[i] = inter[((i + 3) * 7) % 50]
    inter[((i + 3) * 7) % 50] = a

for i in range(50):
    inter[i] = inter[i] ^ 20
    inter[i] = inter[i] ^ 5
    
for i in range(50):
    a = inter[i]
    inter[i] = inter[((i + 83) * 12) % 50]
    inter[((i + 83) * 12) % 50] = a
    
# for i in range(50):
#     print("\\x"+str(inter[i]), end=' ')


"""
Reverse of this prog
"""
out = '\x14 \x5D \x14 \x57 \x16 \x43 \x46 \x7A \x56 \x16 \x57 \x17 \x4B \x16 \x52 \x4C \x61 \x1C \x1C \x7A \x1D \x7A \x11 \x51 \x52 \x16 \x5E \x62 \x6D \x5E \x61 \x7A \x16 \x17 \x61 \x16 \x6B \x61 \x4E \x69 \x14 \x6B \x6D \x51 \x57 \x6D \x6D \x58 \x5D \x4B '

out_tab = out.split(' ')[:-1]
inter = []
for value in out_tab:
    inter.append(hex(ord(value)))
assert inter == ['0x14', '0x5d', '0x14', '0x57', '0x16', '0x43', '0x46', '0x7a', '0x56', '0x16', '0x57', '0x17', '0x4b', '0x16', '0x52', '0x4c', '0x61', '0x1c', '0x1c', '0x7a', '0x1d', '0x7a', '0x11', '0x51', '0x52', '0x16', '0x5e', '0x62', '0x6d', '0x5e', '0x61', '0x7a', '0x16', '0x17', '0x61', '0x16', '0x6b', '0x61', '0x4e', '0x69', '0x14', '0x6b', '0x6d', '0x51', '0x57', '0x6d', '0x6d', '0x58', '0x5d', '0x4b']

for i in range(49, -1, -1):
    inter[i], inter[((i + 83) * 12) % 50] = inter[((i + 83) * 12) % 50], inter[i]

for i in range(49, -1, -1):
    inter[i] = hex(int(inter[i], 16) ^ 5) # 5 == 0x5
    inter[i] = hex(int(inter[i], 16) ^ 32) # 32 == 0x20

for i in range(49, -1, -1):
    inter[i], inter[((i + 3) * 7) % 50] = inter[((i + 3) * 7) % 50], inter[i]

for i in range(49, -1, -1):
    inter[i], inter[((i + 7) * 15) % 50] = inter[((i + 7) * 15) % 50], inter[i]

flag = ''
for i in range(50):
    flag += chr(int(inter[i], 16))
print(flag)
