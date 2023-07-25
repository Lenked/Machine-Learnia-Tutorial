import numpy as np

A = np.array([1, 2, 3])

# Affiche la dimension d'un tableau
print(A.shape)

B = np.zeros((3, 2))
print(type(B.shape))

C = np.ones((3, 4))
print(C)

D = np.full((2, 3), 9)

np.random.seed(0)
print(np.random.randn(3, 4))

print(np.eye(4))

print(np.linspace(0, 10, 20, dtype=np.float16))

# print(np.arange(0, 10, 0.5))


####################################
# MANIPULATION
####################################

D = D.reshape((3, 4))
print(D)


def initialisation(m, n):
    """ m : nombre de lignes
    # n : nombre de colonnes
    # retourne un matricule aléatoire (m, n+1)
    # avec ue colonne biais (remplie de "1") tout à droite """
    X = np.random.randn(m, n)
    X = np.concatenate((X, np.ones((X.shape[0], 1))), axis=1)
    return X


initialisation(3, 4)
