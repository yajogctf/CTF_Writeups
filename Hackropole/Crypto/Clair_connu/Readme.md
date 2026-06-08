# Clair connu

_intro_ _crypto_ _Stream_ _FCSC2021_  

## Description

Votre but est de déchiffrer le flag.

**Fichiers** : [clair-connu.py](./clair-connu.py) et [output.txt](./output.txt)  

**Auteur : Cryptanalyse**

## Elements de réponse

Il s'agit ici d'un chiffrement par XOR, chiffrement symétrique. Donc, si on détermine la clé, on peut ensuite déchiffrer le texte chiffré.  

On obeserve que la clé est constitué de 4 octets reproduits à l'identique 20 fois.  
On va exploiter le fait que $PT XOR KEY = CT <=> PT XOR CT = KEY.  
Or, on connait 4 octets du texte clair (`FCSC`) dont la longueur est celle de la partie de la clé reproduite. Il suffit donc de faire un XOR entre les 4 premiers octets du texte chiffré et de `FCSC` pour déterminer la partie de la clé reproduite 20 fois.  
Reste ensuite à déchiffrer le texte chiffré à l'aide de la clé trouvéeprécédemment.  


## Flag

`FCSC{3ebfb1b880d802cb96be0bb256f4239c27971310cdfd1842083fbe16b3a2dcf7}`

