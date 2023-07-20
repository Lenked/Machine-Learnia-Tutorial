import time

# Tous les carrés de 0 a 9
# METHODE NORMALE
liste_1 = []
for i in range(10):
    liste_1.append(i ** 2)

print(liste_1)

# METHODE LIST COMPREHENSION
liste_2 = [i ** 2 for i in range(10)]
print(liste_2)

# AUTRE EXEMPLE
# Fonction pour calculer le temps d'execution d'un algorithme
# Methode simple
start = time.time()

liste_3 = []
for i in range(10000000):
    liste_3.append(i ** 2)

end = time.time()
print(end - start)

# Mode List comprehension
start = time.time()

liste_4 = [i ** 2 for i in range(10000000)]

end = time.time()
print(end - start)

liste_5 = [[i + j for i in range(3)] for j in range(3)]
print(liste_5)

# ######### DICT COMPREHENSION #######################
dictionnaire = {
    '0': 'Pierre',
    '1': 'Jean',
    '2': 'Julie',
    '3': 'Sophie',
}

prenoms = ['Pierre', 'Jean', 'Julie', 'Sophie']

dico = {k: v for k, v in enumerate(prenoms)}
print(dico)

print(dico.values())

ages = [24, 62, 10, 23]
dico_2 = {prenom: age for prenom, age in zip(prenoms, ages) if age > 20}
print(dico_2)

"""
    Voici la syntaxe pour faire un dict comprehension
    Do this       For this collection                   In this situation
    -------  ------------------------------------  ---------------------------
       x**2         for x in range(0, 50)                 if x % 3 == 0
       
    Cette technique est utile pour avoir un code :
    1. Plus Pro
    2. Plus Court 
    3. Plus Performant
"""

# ############# TUPLE COMPREHENSION ###############
tuple_1 = tuple((i**2 for i in range(10)))
print(tuple_1)

# #################### DEVOIR ########################

# Creer un dictionnaire k:v
# k = 0 - 20
# v = k**2
carres_pairs = {
    str(k): k**2 for k in range(0, 20)
}
print(carres_pairs)