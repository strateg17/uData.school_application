# Завдання №3 Пахольчук Вадим Володимрович

"""Import block"""
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""Importing data and creating a summary"""
dfTitanic = pd.read_csv('titanic.csv')
print(dfTitanic.info())

#Extract the first name from passenger name
dfTitanic['FirstName'] = dfTitanic['Name'].str.extract('(Mr\. |Miss\. |Master. |Mrs\.[A-Za-z ]*\()([A-Za-z]*)')[1]

#pull out the passengers that have popular names (> 10 occurances)
dfPassengersWithPopularNames = dfTitanic[dfTitanic['FirstName'].isin(dfTitanic['FirstName'].value_counts()[dfTitanic['FirstName'].value_counts() > 10].index)]


# calculate the surival rate by popular name
# ax = (dfPassengersWithPopularNames.groupby('FirstName').Survived.sum()/dfPassengersWithPopularNames.groupby('FirstName').
# Survived.count()).order(ascending=False).plot(kind='bar',y='Popular Names',fontsize=8)
ax = (dfPassengersWithPopularNames.groupby('FirstName').Survived.sum()).order(ascending=False).plot(kind='bar',y='Survival rate',fontsize=8)

#set y axis label and save to png for display below
ax.set_ylabel("Popular Names")
fig = ax.get_figure()
fig.savefig('figure.png')
