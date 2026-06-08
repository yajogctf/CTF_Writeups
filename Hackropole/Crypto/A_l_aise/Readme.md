# À l'aise

_intro_ _crypto_ _symétrique_ _FCSC2022_  

## Description

Cette épreuve vous propose de déchiffrer un message chiffré avec la méthode inventée par [Blaise de Vigénère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re). La clé est `FCSC` et le message chiffré est :

```
Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.
```

Le flag est le nom de la ville mentionnée dans ce message.

## Elements de réponse

Le chiffrement de Vigenère consiste à décaler chaque lettre de la position de la lettre correspondante de la clé.  

Pour déchiffrer, on procède de la même manière, mais cette fois on décale dans l'autre sens les lettres.  

Pour se faciliter la tâche, on peut faire appel au site dcode.fr ([https://www.dcode.fr/chiffre-vigenere](https://www.dcode.fr/chiffre-vigenere)), à une bibliothèque Python (comme ) ou programmer soi-même une fonction de déchiffrement.  

Ainsi, on trouve :  
```python
>>> ct = "Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf."
>>> k = "FCSC"
>>> vigenere_dechiffrer(ct, k)
Bonjour cher agent ! Votre prochaine mission, si vous
l'acceptez bien sur, sera d'infiltrer le reseau
souterrain ou se cache nos ennemis. Rendez-vous a
Nantes le 29 avril pour le debut de votre mission.
```

Explication plus complètes ici : [https://www.thepingouin.com/2024/10/15/chiffre-de-vigenere-en-python-guide-complet-pour-le-chiffrement-polyalphabetique/](https://www.thepingouin.com/2024/10/15/chiffre-de-vigenere-en-python-guide-complet-pour-le-chiffrement-polyalphabetique/)  

## Flag

`Nantes`
