import time
import random
import sys

if __name__ == '__main__':
#     flag = input("Flag? > ").encode('utf-8')
#     correct = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]
#     time_cycle = int(time.time()) % 256
#     if len(flag) != len(correct):
#         print('Nope :(')
#         sys.exit(1)
#     for i in range(len(flag)):
#         random.seed(i+time_cycle)
#         if correct[i] != flag[i] ^ random.getrandbits(8):
#             print('Nope :(')
#             sys.exit(1)
#     print(flag)

    
    correct = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]
    flag = 'wctf{'.encode('utf-8')
    trouve = False
    time_cycle = 0
    while not trouve:
        trouve = True
        for i in range(len(flag)):
            random.seed(i+time_cycle)
            if flag[i] ^ correct[i] != random.getrandbits(8):
                trouve = False
                break
        if not trouve:
            time_cycle += 1
    print('time_cycle = ', time_cycle)
    
    flag = [None for _ in range(len(correct))]
    for i in range(len(flag)):
         random.seed(i+time_cycle)
         flag[i] = chr(correct[i] ^ random.getrandbits(8))
    print(''.join(flag))
    