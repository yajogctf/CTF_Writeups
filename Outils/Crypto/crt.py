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
    moduli = [17, 11, 6]
    residues = [3, 4, 5]

    x, M = crt(residues, moduli)
    print(f"Solution : x ≡ {x} (mod {M})")