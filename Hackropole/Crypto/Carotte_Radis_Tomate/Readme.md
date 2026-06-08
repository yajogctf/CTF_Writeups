# Carotte Radis Tomate

_intro_ _crypto_ _FCSC2025_  

## Description

Mangez cinq fruits et légumes par jour !  

**Fichiers** : [carotte-radis-tomate.py](./carotte-radis-tomate.py) et [output.txt](output.txt)  

**Auteur : Cryptanalyse**

## Elements de réponse

Le Flag est chiffré via un chiffrement AES, chiffrement symétrique. Donc si nous réussissons à déterminer la clé `key`, il est possible de déchiffrer le texte chiffré.  

Pour cela, nous disposons des restes de la division euclidienne de cette clé par cinq nombres(`carotte`, `radis`, `tomate`, `pomme` et `banane`). Or, on peut vérifier que ces cinq nombres sont premiers entre eux deux à deux.  
Il est donc possible d'appliquer le théorème des restes chinois pour détemriner la clé. Reste alors à déchiffrer le ciphertext.  

## Flag

`FCSC{2c4c4b3be7d86e1642ce6a8bf1bd75f33b9736e5943f51a49fb9327e248c3b6a}`
