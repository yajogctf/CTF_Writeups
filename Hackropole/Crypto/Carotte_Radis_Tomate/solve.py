import math
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes

def premiers_deux_a_deux(nb_tab: list)-> bool:
    "Renvoie si les nombres passés dans la list en paramètre sont deux à deux premiers entre eux."
    for i in range(len(nb_tab)):
        for j in range(i + 1, len(nb_tab)):
            if math.gcd(nb_tab[i], nb_tab[j]) != 1:
                return False
    return True

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def crt(residues, moduli):
    """
    Résout le système x ≡ residues[i] (mod moduli[i]) par le CRT généralisé.
    
    Paramètres :
        residues : liste des restes r_i
        moduli   : liste des moduli p_i (pas forcément coprimes)
    
    Retourne :
        (x, M) tel que x est la plus petite solution positive,
        et M = ppcm(p_i) est le modulus global.
    
    Lève ValueError si le système est incompatible.
    """
    if len(residues) != len(moduli):
        raise ValueError("Les listes residues et moduli doivent avoir la même longueur.")
    def fuse(r1, m1, r2, m2):
        d, u, _ = extended_gcd(m1, m2)
        if (r2 - r1) % d != 0:
            raise ValueError(
                f"Système incompatible : pas de solution pour "
                f"x ≡ {r1} (mod {m1}) et x ≡ {r2} (mod {m2})"
            )
        lcm = m1 * m2 // d
        k = (u * ((r2 - r1) // d)) % (m2 // d)
        return (r1 + k * m1) % lcm, lcm
    r, m = residues[0] % moduli[0], moduli[0]
    for i in range(1, len(residues)):
        r, m = fuse(r, m, residues[i] % moduli[i], moduli[i])
    return r, m

if __name__ == '__main__':
    carotte =  392278890668246705
    radis   =  4588810924820033807
    tomate  =  17164682861166542664
    pomme   =  12928514648456294931
    banane  =  5973470563196845286
    enc = '2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d'

    p = [17488856370348678479, 16548497022403653709, 17646308379662286151, 14933475126425703583, 17256641469715966189]
    assert (premiers_deux_a_deux(p)) # Les nombres sont bien premiers entre eux deux à deux.
    r = [carotte, radis, tomate, pomme, banane]
    # On applique le CRT pour déterminer la clé de chiffrement.
    x, _ = crt(r, p)
    key = long_to_bytes(x)
    # Déchiffrement du ciphertext.
    E = AES.new(key, AES.MODE_ECB)
    plaintext = E.decrypt(long_to_bytes(int(enc, 16))).rstrip().decode()
    print(f"Flag : {plaintext}")