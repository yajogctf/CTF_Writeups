from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.strxor import strxor

if __name__ == '__main__':
    ct = bytes.fromhex("d91b7023e46b4602f93a1202a7601304a7681103fd611502fa684102ad6d1506ab6a1059fc6a1459a8691051af3b4706fb691b54ad681b53f93a4651a93a1001ad3c4006a825")
    
    pt_debut = "FCSC".encode()
    key = strxor (ct[:len(pt_debut)], pt_debut) * 20
    pt = strxor (ct, key[:len(ct)])
    print(f"FLAG : {pt.decode()}")
    