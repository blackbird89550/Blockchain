import random
import string

# def generer_lignes(nombre_ligne):
#     for i in range(0, nombre_ligne):
#         print("Voici un nombre aléatoir" + str(random.randint(0,5)))
# generer_lignes(100)


def gen_lettre():
    return(random.choice(string.ascii_letters))

def gen_chiffre():
    return(random.randint(0,9))

def gen_chiffre_lettre():
        return(gen_lettre() + str(gen_lettre()))

def gen_nonce(x):
    nonce = ""
    for i in range (x):
        hasard = random.randint(0,1)
        if hasard == 0:
            nonce = nonce + str(gen_chiffre())
        else:
            nonce = nonce + gen_lettre()
    return(nonce)
print(gen_nonce(64))

