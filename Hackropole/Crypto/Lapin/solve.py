from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.number import long_to_bytes

ct = bytes.fromhex("f049de59cbdc9189170787b20b24f7426ccb9515e8b0250f3fc0f0c14ed7bb1d4b42c09d02fe01e0973a7233d99af55ce696f599050142759adc26796d64e0d6035f2fc39d2edb8a0797a9e45ae4cd55074cf99158d3a64dc70a7e836e3b30382df30de49ba60a")
nonce_ = ct[:16]
ct_ = ct[16:-16]
tag_ = ct[-16:]

for pin in range(10000):
    k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1)
    aes = AES.new(k, AES.MODE_GCM, nonce = nonce_)
    pt = aes.decrypt(ct_)
    if b'FCSC' in pt:
        print(f"PIN : {pin}")
        print(f"Flag : {pt.decode()}")
        break