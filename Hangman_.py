import random
liste = ["ordinateur", "vampire", "mamie", "radio", "fleur", "argent", "salaire", "mouche", "frère", "cheval", "bouteille", "souris", "papa", "fils", "journal", "maman", "robot", "jouet", "parfum", "tableau"]
random.shuffle(liste)
ok = False
global mot
mot = liste[0]
global num
partir = False
num = False
nbr_de_l = len(mot)
global nbr_de_faute
nbr_de_faute = 0
nbr_de_lettres_bonnes = 0
global tiret
tire = "-" * nbr_de_l
tiret = list(tire)

def pendu1():
    print(" |")
    print(" |")
    print(" |")
    print(" |")
    print(" |")

def pendu2 ():
    print(" |")
    print(" |/")
    print(" |")
    print(" |")
    print(" |")

def pendu3():
    print(" |---")
    print(" |/")
    print(" |")
    print(" |")
    print(" |")

def pendu4():
    print(" |---")
    print(" |/ o")
    print(" | ")
    print(" | ")
    print(" |")

def pendu5():
    print(" |---")
    print(" |/ o")
    print(" | -|-")
    print(" |")
    print(" |")

def pendu6():
    print(" |---")
    print(" |/ o")
    print(" | -|-")
    print(" | / \\")
    print(" |")
    

while (not(ok == True)):
    for i in range(nbr_de_l):
        print(tiret[i], end="")
    print()
    print()
    partir = False
    lettre_bonne = False
    mot_j = input("Entrez une lettre : ")
    if mot_j == mot:
        print("Gagné !")
        ok = True
    elif len(mot_j) == 1 and mot_j.isalnum() == True:
        if mot_j != "1" and mot_j != "2" and mot_j != "3" and mot_j != "4" and mot_j != "5" and mot_j != "6" and mot_j != "7" and mot_j != "7" and mot_j != "8" and mot_j != "9" and mot_j != "0":
            for i, j in enumerate(mot):
                if mot_j == j:
                    nbr_de_lettres_bonnes += 1
                    tiret[i] = j
                    print("Une lettre de trouvé !")
                    lettre_bonne = True
            if lettre_bonne == True:
                print("Au total, %s lettres ont été trouvés" % nbr_de_lettres_bonnes)
                if nbr_de_lettres_bonnes == nbr_de_l:
                    print("Bravo !")
                    print("Tu as gagné !")
                    print("Si tu veux rejouer, rallume le programme")
                    ok = True
            else:
                nbr_de_faute += 1
                print("C'est faux")
                if nbr_de_faute == 1:
                    pendu1()
                elif nbr_de_faute == 2:
                    pendu2()
                elif nbr_de_faute == 3:
                    pendu3()
                elif nbr_de_faute == 4:
                    pendu4()
                elif nbr_de_faute == 5:
                    pendu5()
                else:
                    pendu6()
                    print("Tu as perdu")
                    print("Le mot était %s." % mot)
                    print("Si tu veux rejouer, rallume le programme")
                    ok = True
        else:
            print("Vous ne devez pas entrer de chiffres, juste une lettre.")
    elif mot_j.isalnum() != True:
        print("Ce caractère n'est pas alphanumérique")
        print("Vous devez entrer juste une lettre")
    elif mot_j == "exit" or mot_j == "quit" or mot_j == "goodbye":
        print("Es tu sur de vouloir quitter le jeu ?")
        print("Répondez par Y (oui) ou N (non)")
        print()
        while (not (partir == True)):
            repo = input("Entrez votre réponse : ")
            if repo == "Y":
                partir = True
                ok = True
            elif repo == "N":
                partir = True
            else:
                print("Vous devez répondre par Y (oui) ou N (non)")
    elif len(mot_j) != 1:
        print("Vous ne devez entrer qu'UNE seule lettre")
    else:
        print("******** PROBLEME ********")
        print("- Caractère non-reconnu -")
        print()
        print("Vous devez entrer une lettre")
        print("Et rien d'autre")
    

