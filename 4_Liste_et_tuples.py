################################################
# STRUCTURES DE DONNÉES : SEQUENCE
################################################

# Listes
liste_1 = [1, 4, 2, 7, 35, 84]
villes = ['Douala', 'Yaoundé', 'Buea', 'Baffoussam']
liste_2 = [liste_1, villes]
liste_3 = []

# Tuples
tuple_1 = (1, 4, 2, 7, 5)

# String
prenom = 'Lenked'

# INDEXING
print(villes[0])
print(villes[1])
print(villes[-1])

# SLICING
print(villes[1:3])
print(villes[:3])
print(villes[2:])
print(villes[::2])
print(villes[::-1])

print(prenom[:3])

# villes[0] = 'Limbe'
# print(villes)

villes.append('Limbe')
villes.insert(2, 'Garoua')

villes_2 = ['Ngaoundere', 'Bertoua']
villes.extend(villes_2)

print(len(villes))

# Les Conditions
if 'Garoua' in villes:
    print('oui')
else:
    print('non')

for i in villes:
    print(i)

for index, value in enumerate(villes):
    print(index, value)

for a, b in zip(villes, liste_1):
    print(a, b)


# ###### EXERCICE #########
# Suite de Fibonacci
def fibonacci(n):
    fib1 = 0
    fib2 = 1
    while fib1 < n:
        print(fib1)
        fib1, fib2 = fib2, fib1 + fib2


fibonacci(1000)
