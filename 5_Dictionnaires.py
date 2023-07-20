import numpy as np

traduction = {
    "chien": "dog",
    "chat": "cat",
    "souris": "mouse",
    "oiseau": "bird"
}

inventaire = {
    "bananes": 5000,
    "pommes": 2048,
    "poires": 2145
}

dictionnaire_3 = {
    "dict_1": traduction,
    "dict_2": inventaire
}

parametres = {
    "W1": np.random.randn(10, 100),
    "b1": np.random.randn(10, 1),
    "W2": np.random.randn(10, 10),
    "b2": np.random.randn(10, 1)
}

print(inventaire.values())
print(inventaire.keys())
print(len(inventaire))

inventaire["abricots"] = 4902
print(inventaire)

print(inventaire.get('poires', 1))

liste_1 = ('Douala', 'Yaoundé', 'Buea', 'Baffoussam')
print(inventaire.fromkeys(liste_1, 'defaut'))
fruits = inventaire.pop('poires')
print(fruits, inventaire)

for i in inventaire:
    print(i)

for i in inventaire.values():
    print(i)

for k, v in inventaire.items():
    print(k, v)


# ########### EXERCICE ############
def fibonacci(n):
    # Retourne ue liste contenant une suite de fibonacci
    a = 0
    b = 1
    fib = [a]
    while b < n:
        a, b = b, a + b
        fib.append(a)
    return fib


print(fibonacci(1000))

# ####### DEVOIR ###############

classeur = {
    "positif": [],
    "negatif": [],
}

"""
def trier(classeurParam, nombre):
    # classeurParam : dictionnaire taille 2
    # nombre : int
    # Range nombre dans positif ou negatif de classeur de nombre
    return classeurParam
trier(classeur, 2)
trier(classeur, 2)

"""


# ################ CORRECTION #####################
def trier(classeurParam, nombre):
    # classeurParam : dictionnaire taille 2
    # nombre : int
    # Range nombre dans positif ou negatif de classeur de nombre
    if nombre > 0:
        classeurParam['positif'].append(nombre)
    else:
        classeurParam['negatif'].append(nombre)
    return classeurParam


trier(classeur, 2)
trier(classeur, -2)
trier(classeur, 45)
trier(classeur, -1)

print(classeur)
