# SMIC (2)

_intro_ _crypto_ _RSA_ _FCSC2020_  

## Description

La sécurité du cryptosystème RSA repose sur un problème calculatoire bien connu.  

On vous demande de déchiffrer le “message” chiffré `c` ci-dessous pour retrouver le “message” en clair `m` associé à partir de la clé publique `(n, e)`.  

Valeurs :  

- `e = 65537`
- `n = 632459103267572196107100983820469021721602147490918660274601`
- `c = 63775417045544543594281416329767355155835033510382720735973`  

Le flag est `FCSC{xxxx}` où xxxx est remplacé par la valeur de `m` en écriture décimale.  

Une variante de cette épreuve est disponible ici : [SMIC (1)](./Hackropole/Crypto/SMIC_1/).  

**Auteur : Cryptanalyse**

## Elements de réponse

Ici, il faut déterminer le texte clair.  

Le fait que `n` soit petit permet d'envisager de chercher sa décomposition en facteurs premiers.  

Ainsi, avec la page [https://www.dcode.fr/decomposition-nombres-premiers](https://www.dcode.fr/decomposition-nombres-premiers), on trouve que `n` est égale au produit des nombres premiers suivants : `650655447295098801102272374367 * 972033825117160941379425504503`  

Ensuite, il suffit de déterminer `phi` puis `d` pour trouver le texte clair.  

## Flag

`FCSC{563694726501963824567957403529535003815080102246078401707923}`

