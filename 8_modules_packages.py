import test as f
from test import *
import random
import statistics
import os
import glob
import math


liste = f.fibonacci(50)

#########################################################
# MATH
#########################################################
print(math.cos(2*math.pi))
print(math.exp(5))

#########################################################
# STATISTICS
#########################################################
print(statistics.mean(liste))
print(statistics.variance(liste))

#########################################################
# RANDOM
#########################################################

random.seed(0)

print(random.choice(liste))
print(random.choice(['Jean', 'Anne', 'Julie']))

print(random.random())
print(random.randint(5, 10))
print(random.randrange(100))
print(random.sample(range(100), random.randrange(10)))

random.shuffle(liste)

#########################################################
# OS
#########################################################

print(os.getcwd())

#########################################################
# GLOB
#########################################################

print(glob.glob("*"))
print(glob.glob("*.txt"))

filenames = glob.glob("*.txt")

d = {}

for file in filenames:
    with open(file, 'r') as f:
        d[file] = f.read().splitlines()

print(d)

