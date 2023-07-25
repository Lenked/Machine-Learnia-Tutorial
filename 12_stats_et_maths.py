import numpy as np

np.random.seed(0)
A = np.random.randint(0, 10, [5, 5])
print(A)

print(A.sum(axis=1))
print(A.cumsum())

# Pour obtenir le minimum et le maximum
print(A.min())
print(A.max())

# Pour obtenir l'ordre du minimum et du maximum
print(A.argmin())
print(A.argmax())

# Le lien du site pour apprendre les fonctions NumPy : https://docs.scipy.org

print(np.exp(A))

################## LES SATISTICS ###############################

# Methodes ndarray
print(A.mean())
print(A.std())
print(A.var())

# Les routines
print(np.corrcoef(A))

print(np.corrcoef(A)[0, 1])

values, counts = np.unique(A, return_counts=True)

print(values, counts)

for i, j in zip(values[counts.argsort()], counts[counts.argsort()]):
    print(f'valeur {i} apparait {j}')

print(A.std())

print(A.var())

A = np.random.randn(5, 5)
A[0, 2] = np.nan
A[4, 3] = np.nan
print(A)

print(np.nanstd(A))

print(np.isnan(A))
print(np.isnan(A).sum())
print(np.isnan(A).sum() / A.size)

A[np.isnan(A)] = 0
print(A)

################ ALGEBRE LINEAIRE ########################
A = np.ones((2, 3))
B = np.ones((3, 2))
print(A, '\n', B)

print(A.dot(B))

print(A)

print(np.linalg.det(A))

print(np.linalg.inv(A))

print(np.linalg.eig(A))

####### CORRECTION DEVOIR ####################


from scipy import misc
import matplotlib.pyplot as plt

face = misc.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()


