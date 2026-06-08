def vigenere_chiffrer(texte: str, cle: str) -> str:
    """Chiffre un texte avec le chiffre de Vigenère."""
    cle_ = cle.upper() * (len(texte) // len(cle) + 1)
    resultat = ""
    j = 0
    for c in texte:
        if c.isalpha():
            decalage = ord(cle_[j]) - ord('A')
            if c.isupper():
                c_chiffre = chr((ord(c) - ord('A') + decalage) % 26 + ord('A'))
            else:
                c_chiffre = chr((ord(c) - ord('a') + decalage) % 26 + ord('a'))
            resultat += c_chiffre
            j += 1
        else:
            resultat += c  # ponctuation et espaces conservés
    return resultat


def vigenere_dechiffrer(texte: str, cle: str) -> str:
    """Déchiffre un texte chiffré avec le chiffre de Vigenère."""
    cle_ = cle.upper() * (len(texte) // len(cle) + 1)
    resultat = ""
    j = 0
    for c in texte:
        if c.isalpha():
            decalage = ord(cle_[j]) - ord('A')
            if c.isupper():
                c_chiffre = chr((ord(c) - ord('A') - decalage) % 26 + ord('A'))
            else:
                c_chiffre = chr((ord(c) - ord('a') - decalage) % 26 + ord('a'))
            resultat += c_chiffre
            j += 1
        else:
            resultat += c  # ponctuation et espaces conservés
    return resultat


if __name__ == "__main__":
    texte_clair  = "Hello World !"
    cle          = "blaise"
    chiffre      = vigenere_chiffrer(texte_clair, cle)
    dechiffre    = vigenere_dechiffrer(chiffre, cle)
    assert (chiffre == 'Ipltg Apcll !')
    assert (dechiffre == texte_clair)
