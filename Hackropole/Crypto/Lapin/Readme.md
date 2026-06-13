# La PIN

_intro_ _crypto_ _Symétrique_ _FCSC2021_  

## Description

J’ai protégé le flag en le chiffrant avec des algorithmes modernes. Pourrez-vous le retrouver ?  

**Fichiers** : [lapin.py](./lapin.py) et [output.txt](output.txt)  

**Auteur : Cryptanalyse**

## Elements de réponse

Il s'agit d'un chiffrement AES, donc symétrique. La connaissance de la clé devrait permettre de déchiffrer le message chiffré.  

La clé étant construite à partir d'un nombre entre 0 et 9999, une recherche par force brute peut être envisagée.  

Pour déchiffrer le texte chiffré, il nous faut donc la clé mais il nous faut également les valeurs de `nonce` et `tag` (voir [https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html](https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html)).  

Or, en regardant attentivement le code fourni, la valeur fournie dans le fichier `output.txt` est la concaténation des variables `nonce` (16 octets), `c` (le texte chiffré) et `tag` (16 octets).  

Ainsi, on peut donc récupérer le contenu de ces trois éléments puis de les utiliser pour déchiffrer le texte chiffré par force brute sur la valeur de quatre chiffres maximum utilisée pour la clé.  

On trouve que la valeur de `pin` est `6273` et on trouve le flag.  

## Flag

`FCSC{c1feab88e6c6932c57fbaf0c1ff6c32e51f07ae87197fcd08956be4408b2c802}`

