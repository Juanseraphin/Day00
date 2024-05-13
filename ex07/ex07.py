num = int(input("Entrez un numéro : "))


centaines = num // 100
dizaines = (num // 10) % 10
unites = num % 10


somme_cubes = centaines**3 + dizaines**3 + unites**3


if num == somme_cubes:
    print(num, "est un nombre Armstrong")
else:
    print(num, "n'est pas un nombre Armstrong")