
from random import*
from math import *

somme=1000
continuer=True
print("vous etes installer sur la table a roulette avec",somme,"$")

while continuer:
    mise_numero= -1
    while mise_numero>49 or mise_numero<0:
        mise_numero=input("Parier sur un nombre (entre 0 et 49) : ")
        try :
            mise_numero=int(mise_numero)
        except ValueError:
            print("Vous n'avez fait de saisie")
            mise_numero = -1
            continue
        if mise_numero<0 or mise_numero>49:
            print("Ce nombre n'est pas  entre 0 et 49.")
    mise = 0
    while mise <= 0 or mise > somme:
        mise = input("entrez votre mise:")
        try:
            mise = int(mise)
        except ValueError:
            print("vous n'avez pas saisi de mise")
            mise = -1
            continue
        if mise <= 0:
            print("votre mise est invalide")
        if mise > somme:
            print ("veuillez restez dans les clous,vous n'avez que",somme,"$")


    roulette=randint(0,49)
    print("Faite vos jeu , la roulette tourne.... et le Numéro gagnant est : ", roulette," !")

    if roulette==mise_numero:
        print("Vous avez gagné ",mise*3," euros !")
        somme+=mise*3
        print("Vous avez maintenant ",somme, "euros.")
    elif roulette%2 == mise_numero%2:
        print("vous avez parier sur la bonne couleur", mise, "euros")
        mise = ceil(mise*0.5)
        somme+=mise
        print("vous avez maintenant", somme, "euros")
    else:
        print("Perdu,vous perdez votre mise")
        somme-=mise
        print("il vous reste maintenant",somme,"$")
    if somme<=0:
        print("Dommage,Vous n'avez plus d'argent ! C'est fini.")
        choice = input("voulez-vous continuer? ")
        if choice not in ('o', 'oui', 'ok'):
            continuer= False
