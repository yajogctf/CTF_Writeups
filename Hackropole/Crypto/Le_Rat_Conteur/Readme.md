# Le Rat Conteur

_intro_ _crypto_ _Symétrique_ _FCSC2020_  

## Description

Le fichier suivant a été chiffré en AES-128 en mode CTR, avec la clé de 128 bits `00112233445566778899aabbccddeeff` et un IV nul.  

À vous de le déchiffrer pour obtenir le flag.  

**Fichiers** : [flag.jpg.enc](./flag.jpg.enc)  

**Auteur : Cryptanalyse**

## Elements de réponse

On a l'élément chiffré dans un fichier. Pour récupérer le "texte chiffré", on effectue une lecture bianire du fichier fourni.  

Ensuite, on déchiffre le texte binaire chiffré à l'aide de l'algorithme AES, mode CTR, avec la clé fournie et comme `iv` la valeur `NULL`.  

Le texte chiffré est alors sauvegardé en binaire dans un fichier image au format JPG. L'affichage de ce fichier permet de lire le flag attendu.  

## Flag

`FCSC{879C2FEE3B9EFBC651050F881841D209}`