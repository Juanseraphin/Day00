def compter_caracteres(chaine):
    compteur = 0
    for _ in chaine:
        compteur += 1
    return compteur

chaine = "thimotime est raciste"
nb_caracteres = compter_caracteres(chaine)
print("La chaîne", chaine, "contient", nb_caracteres, "caractères.")
