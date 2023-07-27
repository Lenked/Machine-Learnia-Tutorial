import numpy as np

np.random.seed(0)
A = np.random.randint(0, 10, [2, 3])
B = np.ones((1, 3))

C = A + B
print(C)

############### EXERCICE REPONSE ###########################

# Standardize une matrice
A = np.random.randint(0, 100, [100, 5])
print(A)

D = (A - A.mean(axis=0)) / A.std(axis=0)
print(D)
print(D.mean(axis=0))
print(D.std(axis=0))



