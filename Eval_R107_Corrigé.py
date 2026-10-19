#Exercice 1:

def calculer_niveau(stats):
    somme = 0
    for stat in stats :
        somme += stat
        niveau = somme / len(stats)
    return niveau
seuil_legendaire = 15

personnage = ["Legolas", "Archer", [17, 16, 20, 10]]
nom = personnage[0]
classe = personnage[1]
stats = personnage[2]
niveau = calculer_niveau(stats)
if niveau > seuil_legendaire :
    force = "Légendaire"
else :
    force = "Standard"
print(f"{nom}, ({classe}) est de niveau {niveau} : {force}")


#Exercice 2:

def deter_spe():
    nom = input("Entrez le nom du personnage : ") # nom chaine
    stats = [] # stats liste de nb
    for i in range(4):
        stats.append(int(input(f"Entrez la statistique {i} : ")))
    max_stat = stats[0] # nombre, initialisation
    index_max = 0 # entier, initialisation
    for i in range(1, len(stats)): # pour chaque i de 1 a longueur stat - 1 faire
        if stats[i] > max_stat :
            max_stat = stats[i]
            index_max = i
    # fin pour
    if index_max == 1 :
        specialisation = "Spécialisé en combat"
    elif index_max == 2 :
        specialisation = "Spécialisé en magie"
    elif index_max == 3 :
        specialisation = "Spécialisé en furtivité"
    else :
        specialisation = "Polyvalent"
    # fin si
    print(f"{nom} est {specialisation}")


deter_spe()

#Exercice 3: