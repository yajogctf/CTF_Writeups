from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

with open("flag.jpg.enc", "rb") as fichier:
    ct = fichier.read()

key = bytes.fromhex("00112233445566778899aabbccddeeff")
iv = b'\x00'
cipher = AES.new(key, AES.MODE_CTR, nonce = iv)
pt = cipher.decrypt(ct)

with open("flag.jpg", "wb") as fichier:
    fichier.write(pt)

#FCSF{879C2FEE3B9EFBC651050F881841D209}