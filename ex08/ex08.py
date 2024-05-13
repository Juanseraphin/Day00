n = int(input("Entrez le nombre de lignes pour la pyramide : "))


while n <= 0:
    n = int(input("Entrez un nombre de lignes positif pour la pyramide : "))


for i in range(1, n+1):
    nb_espaces = n - i
    nb_etoiles = 2*i - 1
    ligne = ' ' * nb_espaces + '*' * nb_etoiles
    print(ligne)