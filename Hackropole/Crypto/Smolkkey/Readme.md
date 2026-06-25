# Smölkkey

_intro_ _crypto_ _RSA_ _FCSC2025_  

## Description

![Image d'illustration'](./smolkkey.jpg)  

**Fichiers** : [smolkkey.py](./smolkkey.py) et [smolkkey.txt](./smolkkey.txt)  

**Auteur : Cryptanalyse**

## Elements de réponse

On remarque que `c` et `e` sont très petits. On peut donc supposer que le texte clair est tout simplement la racine cubique de `c` sans modulo. C'est à dire que $c = pt^e + 0 * n$.  

Il suffit donc d'extraire la racine cubique de `c` pour déterminer `pt`. Pour cela, soit on l'implémente, comme dans le fichier `solve.py`, soit on utilise par exemple la bilbiothèque `gmpy2` et la fonction `iroot` (`gmpy2.iroot(c, 3)`)  

Une fois le texte obtenu, il faut l'écrire correctement, les caractères ayant été tous permutés.  

## Flag

`FCSC{30f7c4b2fa7f0fb48bfbd9bbd413491c0a6da660764961b862fe38a83b4bc00f}`

