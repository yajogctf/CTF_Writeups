from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256

output = {"iv": "ea425b2ea4bb67445abe967e3bd1b583", "c": "69771c85e2362a35eb0157497e9e2d17858bf11492e003c4aa8ce1b76d8d3a31ccc3412ec6e619e7996190d8693299fc3873e1e6a96bcc1fe67abdf5175c753c09128fd1eb2f2f15bd07b12c5bfc2933", "h": "951bd9d2caae0d9e9a5665b4fc112809aac9f5f9ecbcfc5ad8e23cb1d020201d"}
iv = bytes.fromhex(output['iv'])
ct = bytes.fromhex(output['c'])
h = output['h']

# On teste tous les mdp du fichier rockyou.txt
trouve = False
with open("rockyou.txt", "r", encoding="latin-1") as file:
    for line in file:
        password = line.rstrip('\n\r')
        h_ = HMAC.new(password.encode(), digestmod = SHA256)
        h_.update(b"FCSC2022")
        if h == h_.hexdigest(): # La clé 
            trouve = True
            break
if trouve:
    # On déchiffre à l'aide du mot de passe trouvé avant
    assert (password == 'omgh4xx0r')
    print(f"Mot de pass : {password}")
    k  = SHA256.new(password.encode()).digest()
    cipher  = AES.new(k, AES.MODE_CBC, iv = iv)
    pt = cipher.decrypt(ct)
    print(f"Flag : {pt.decode()}")