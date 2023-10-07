import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#################### DATA FRAME #############################

data = pd.read_excel('data_game/titanic3.xls')
data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)

data = data.dropna(axis=0)

# data['pclass'].value_counts().plot.bar()

# data.groupby(['sex']).mean()

###################################
data.loc[data['age'] <= 20, 'age'] = 0
data.loc[(data['age'] > 20) & (data['age'] <= 30), 'age'] = 1
data.loc[(data['age'] > 30) & (data['age'] <= 40), 'age'] = 2
data.loc[data['age'] > 40, 'age'] = 3

data.head()

data['age'].value_counts()

data.groupby(['age']).mean()


def categories_ages(age):
    if age <= 20:
        return '< 20 ans'
    elif (age > 20) & (age <= 30):
        return '20-30 ans'
    elif (age > 30) & (age <= 40):
        return '30-40 ans'
    else:
        return '+40 ans'


print(data['age'].map(categories_ages))
