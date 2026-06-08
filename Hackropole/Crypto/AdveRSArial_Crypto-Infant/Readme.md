# AdveRSArial Crypto (Infant)

_intro_ _crypto_ _RSA_ _FCSC2024_  

## Description

Je viens de suivre un cours sur RSA mais je crois que j’ai oublié quelque chose. Il me semble que le prof parlait de deux trucs, mais je ne sais plus exactement quoi. Vous pouvez m’aider ?  

**Fichiers** : [adversarial-crypto-infant.py](./adversarial-crypto-infant.py) et [output.txt](output.txt)  

**Auteur : Maxime, Cryptanalyse**

## Elements de réponse

Il s'agit d'un chiffrement RSA avec `n` qui est un nombre premier (habituellement, `n` est le produit de deux nombres premiers, ce qui rend difficile la calcul de `phi` et donc de `d`, inverse de `e` modulo `phi`).  

Ici, `phi` vaut donc `n - 1` puisque `n` est premier et l'inverse de `e` se calcule sans soucis.  
Il ne reste plus qu'à transformer l'entier obtenuen octet puis en chaine de caractères.  

## Flag

`FCSC{d0bf88291bcd488f28a809c9ae79d53da9caefc85b3790f57615e61c70a45f3c}`
