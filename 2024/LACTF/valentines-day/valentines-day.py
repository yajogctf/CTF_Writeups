def lettre(c):
    # retourne vrai si c est une lettre non accentuee
    car = ord(c.upper())
    return car>64 and car<91

def decalage(c, k):
    # decale une lettre majuscule. Les autres caracteres ne sont pas modifies
    car = ord(c.upper())
    if lettre(c):
        car += k
        while car>90:
            car -= 26
        while car<65:
            car += 26
        return chr(car)
    else:
        return ""

def nettoyer_txt(txt):
    '''Retire tout ce qui n'est pas une lettre de l'alphabet non accentuée'''
    nv_txt = ""
    for lettre in txt:
        if not(lettre < "A" or (lettre > "Z" and lettre <"a") or lettre > "z"):
            nv_txt += lettre
    return nv_txt

def vigenere(message, cle, crypte):
    ''' effectue le decalage en fonction de la cle sur les caracteres de message
    :example:
    >>> cle = "JULIUS"
    >>> texte="Ave Caesar morituri te salutant"
    >>> texte_code = vigenere(texte, cle, True)
    JPP KUWBUC UIJRNFZC LN MLTOLJHE
    >>> texte_decode = vigenere(texte_code, cle, False)
    AVE CAESAR MORITURI TE SALUTANT
    '''
    cle = nettoyer_txt(cle)
    n = 0
    chiffre=''
    for c in message:
        if lettre(c):
            k = ord(cle[n % len(cle)].upper())-65
            if crypte:
                deca = decalage(c, k)
            else:
                deca = decalage(c, -k)
            if c == c.upper():
                chiffre += deca
            else:
                chiffre += deca.lower()
            n+=1
        else:
            chiffre += c
    return chiffre

if __name__ == '__main__':
    indice_chiffre = """Br olzy Jnyetbdrc'g xun, V avrkkr gb sssp km frja sbv kvflsffoi Jnuc Sathrg. Wkmk gytjzyakz mj jsqvcmtoh rc bkd. Canjc kns puadlctus!"""
    indice_dechiffre = """On this Valentine's day, I wanted to show my love for professor Paul Eggert. This challenge is dedicated to him. Enjoy the challenge!"""
    debut_cle = vigenere(indice_chiffre, indice_dechiffre, False)
    debut_cle = nettoyer_txt(debut_cle)
    print("Début de la clé de chiffrement : ", debut_cle)

    lactf_chiffre = "ropgf"
    lactf_dechiffre = "lactf"
    debut_cle_flag = vigenere(lactf_chiffre, lactf_dechiffre, False)
    print('Morceau de la clé au début du flag :', debut_cle_flag)

    debut_cle = debut_cle[5:].lower()
    print("Début de clé : ", debut_cle)

    texte_chiffre = """ropgf{qvjal_dfuxaxzbk_gbq_jeci_hdt_nr_hdr_eexij}"""
    texte_dechiffre = vigenere(texte_chiffre, debut_cle, False)
    print("Flag : ", texte_dechiffre)
