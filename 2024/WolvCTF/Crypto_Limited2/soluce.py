import time
import random
import sys

# if __name__ == '__main__':
#     flag = input("Flag? > ").encode('utf-8')
#     correct = [192, 123, 40, 205, 152, 229, 188, 64, 42, 166, 126, 125, 13, 187, 91]
#     if len(flag) != len(correct):
#         print('Nope :(')
#         sys.exit(1)
#     if time.gmtime().tm_year >= 2024 or time.gmtime().tm_year < 2023:
#         print('Nope :(')
#         sys.exit(1)
#     if time.gmtime().tm_yday != 365 and time.gmtime().tm_yday != 366:
#         print('Nope :(')
#         sys.exit(1)    
#     for i in range(len(flag)):
#         # Totally not right now
#         time_current = int(time.time())
#         random.seed(i+time_current)
#         if correct[i] != flag[i] ^ random.getrandbits(8):
#             print('Nope :(')
#             sys.exit(1)
#         time.sleep(random.randint(1, 60))
#     print(flag)

import datetime
import calendar
 
date = datetime.datetime(2023, 12, 31, 0, 0, 0)
temps = calendar.timegm(date.timetuple())

correct = [192, 123, 40, 205, 152, 229, 188, 64, 42, 166, 126, 125, 13, 187, 91]
flag = 'wctf{'.encode()
time_current = temps - 1
found = False
while (time_current < temps + 2 * 86401) and (not found):# 1 Day = 86401 s
    time_current += 1
    t = time_current
    found = True
    for i in range(len(flag)):
        random.seed(i + t)
        if correct[i] != flag[i] ^ random.getrandbits(8):
            found = False
            break
        t += random.randint(1, 60)

flag = [None for _ in range(len(correct))]
t = time_current
for i in range(len(correct)):
    random.seed(i + t)
    flag[i] = chr(correct[i] ^ random.getrandbits(8))
    t += random.randint(1, 60)

print(''.join(flag))