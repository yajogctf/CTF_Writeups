import sympy
from Crypto.Util.number import long_to_bytes

if __name__ == '__main__':
    e = 65537
    n = 632459103267572196107100983820469021721602147490918660274601
    c = 63775417045544543594281416329767355155835033510382720735973
    
    # On obtient la décomposition avec la page https://www.dcode.fr/decomposition-nombres-premiers
    p = 650655447295098801102272374367
    q = 972033825117160941379425504503
    assert (sympy.isprime(p) and sympy.isprime(q))
    assert(n == 650655447295098801102272374367 * 972033825117160941379425504503)
    
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    pt = pow(c, d, n)
    print("Flag : FCSC{" + str(pt) + "}")