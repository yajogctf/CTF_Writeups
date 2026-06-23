def rot13(texte):
    dico = {}
    for lettre_debut in ['A', 'a']:
        for i in range(26):
            dico[chr(ord(lettre_debut) + i)] = chr(ord(lettre_debut) + (i + 13) % 26)
    texte_chiffre = ''
    for lettre in texte:
        if lettre in dico:
            texte_chiffre += dico[lettre]
        else:
            texte_chiffre += lettre
    return texte_chiffre