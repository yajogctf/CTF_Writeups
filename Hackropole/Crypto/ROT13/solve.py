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

if __name__ == '__main__':
    ct_tab = ["GBQB yvfgr :", "- Cnva (2 onthrggrf)", "- Ynvg (1 yvger)", "- Pbevnaqer (fhegbhg cnf, p'rfg cnf oba)",
          "- 4 onanarf, 4 cbzzrf, 4 benatrf", "- Cbhyrg (4 svyrgf qr cbhyrg)", "- 1 synt : SPFP{rq24p7sq86p2s0515366}",
          "- Câgrf (1xt)", "- Evm (fnp qr 18xt)", "- Abheve zba qvabfnher'"]
    for ct in ct_tab:
        pt = rot13(ct)
        print(pt)
