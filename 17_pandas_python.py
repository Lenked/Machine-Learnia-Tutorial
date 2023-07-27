import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#################### DATA FRAME #############################

data = pd.read_excel('data_game/titanic3.xls')
data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)

data = data.dropna(axis=0)

data['pclass'].value_counts().plot.bar()

data.groupby(['sex']).mean()



