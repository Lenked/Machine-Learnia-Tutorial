import numpy as np
# La valeur absolue
x = -3
print(abs(x))

# Prendre la valeur entiere d'un nombre decimal
x = 3.14
print(round(x))

# Recuperer le max et le min d'une liste
liste_1 = [0, 23, 14, -19]
print(max(liste_1))
print(min(liste_1))
# La longueur d'Une liste
print(len(liste_1))
# La somme d'une liste
print(sum(liste_1))

#  ###
liste_2 = [True, True, False]
print(all(liste_2))
print(any(liste_2))
print(any(liste_1))

# Recuperer le type d'une variable
x = 10
print(type(x))

# Convertir en chaine de caractere
x = str(x)
print(x, type(x))

x = 10
print(type(float(x)))

liste_1 = [0, 61, 63, 243]
print(tuple(liste_1))

inventaire = {
    "bananes": 5000,
    "pommes": 2048,
    "poires": 2145
}

print(list(inventaire.keys()))

# Convertir en binaire
print(bin(51))
print(oct(16))

# INPUT(entré de valeur)
# x = input('Entrez un nombre : ')
# print(type(x))

# Les formats
x = 25
ville = 'Douala'
message = "La température est de {} degC a {}".format(x, ville)
print(message)
message = f"La température est de {x} degC a {ville}"
print(message)

# Exemple dans le machine learning
parametres = {
    "W1": np.random.randn(10, 100),
    "b1": np.random.randn(10, 1),
    "W2": np.random.randn(10, 10),
    "b2": np.random.randn(10, 1)
}

for i in range(1,3):
    print("couche", i)
    # print(parametres["W{}".format(i)])
    print(parametres[f"W{i}"])

# MANIPULATION DES FICHIERS

# Open
f = open('test.txt', 'w')
f.write('Bonjour')
f.close()

f = open('test.txt', 'r')
print(f.read())

with open('test.txt', 'r') as f:
    print(f.read())

# Exemple de fonctions
with open('test.txt', 'w') as f:
    for i in range(10):
        f.write(f"{i}² = {i**2}\n")


# ############ DEVOIR ###################
"""
    Lire 'test.txt' et retourner une liste [0²=0, 1²=1, 2²=4, ... ,9²=81]
"""

# solution 1
with open('test.txt', 'r') as f:
    liste_3 = f.read().splitlines()
    print(liste_3)

# solution 2
liste_3 = [line.strip() for line in open('test.txt', 'r')]
print(liste_3)
