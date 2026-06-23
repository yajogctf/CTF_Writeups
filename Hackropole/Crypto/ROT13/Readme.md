# ROT13

_intro_ _crypto_ _FCSC2023_  

## Description

Un de vos collègues ne jure que par cette méthode de chiffrage révolutionnaire appelée rot13.  

Il l’a utilisée pour dissimuler un flag dans ce texte. Démontrez-lui qu’il a tort de supposer que cet algorithme apporte une quelconque notion de confidentialité !  

```
GBQB yvfgr :
- Cnva (2 onthrggrf)
- Ynvg (1 yvger)
- Pbevnaqer (fhegbhg cnf, p'rfg cnf oba)
- 4 onanarf, 4 cbzzrf, 4 benatrf
- Cbhyrg (4 svyrgf qr cbhyrg)
- 1 synt : SPFP{rq24p7sq86p2s0515366}
- Câgrf (1xt)
- Evm (fnp qr 18xt)
- Abheve zba qvabfnher
```

**Auteur : Cryptanalyse**

## Elements de réponse

Un grand classique du chiffrement symétrique : chaque lettre de l'alphabet est décalée de 13 lettres de manière circulaire.  

Les espace, les caractères spéciaux et les chiffres ne changent pas.  

Il suffit donc d'effectuer ce décalage une seconde fois pour retrouver le texte initial et déterminer le flag.  

## Flag

`FCSC{ed24c7fd86c2f0515366}`

