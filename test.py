# Suite de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    fib = []
    while a < n:
        fib.append(a)
        a, b = b, a+b
    return fib


# ################ CORRECTION #####################
def classer(classeurParam, nombre):
    # classeurParam : dictionnaire taille 2
    # nombre : int
    # Range nombre dans positif ou negatif de classeur de nombre
    if nombre > 0:
        classeurParam['positif'].append(nombre)
    else:
        classeurParam['negatif'].append(nombre)
    return classeurParam