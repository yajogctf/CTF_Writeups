# Délog

_intro_ _crypto_ _Courbe elliptique_ _FCSC2026_  

## Description

Le problème du logarithme discret est à la base de plusieurs primitives cryptographiques très utilisées aujourd’hui. J’ai chiffré mon flag avec une courbe elliptique, arriverez-vous à résoudre le log discret ?  

**Fichier** : [delog.py](./delog.py)  

**Auteur : ElyKar**

## Elements de réponse

Le chiffrement s'effectue via un chiffrement par Courbe elliptique.  
Ici, les coordonnées de chaque point fourni sont obtenues en multipliant G (calculable à l'aide du code fourni) par le code ASCII de chaque caractère du FLAG.  
Comme il y a au plus 256 possibilités par caractère du FLAG, on peut y aller par force brute, en commençant par le code 20 puisque les caractères du flag sont tous imprimables.  


## Flag

`FCSC{Dl0G_S0lV1ng!}`

