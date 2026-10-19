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