import numpy as np
import matplotlib.pyplot as plt

############### MATPLOTLIB ##############

x = np.linspace(0, 2, 10)
y = x ** 2
print(x)

# plt.plot(x, y, c='red', lw=3, ls='--')
plt.figure()
plt.plot(x, y, label='quadratique')
plt.plot(x, x ** 3, label='cubique')
plt.title('figure 1')
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.legend()
plt.show()
plt.savefig('figure.png')

plt.subplot(2, 1, 1)
plt.plot(x, y, c='red')
plt.subplot(2, 1, 2)
plt.plot(x, y, c='blue')
plt.show()

#################  EXERCICE ###########################
dataset = {f"Experience {i}": np.random.randn(100) for i in range(4)}
print(dataset)


def graphique(data):
    n = len(data)
    plt.figure(figsize=(12, 8))
    for k, i in zip(data.keys(), range(n)):
        plt.subplot(n, 1, 1)
        plt.plot(data[k])
        plt.title(k)
    plt.show()


graphique(dataset)
