# Завдання №3 Пахольчук Вадим Володимрович

"""Import block"""

import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""Importing data and creating a summary"""
df = pd.read_csv('titanic.csv')
print(df.head(5))
print(df.tail(5))
print(df.describe())
print(df.info())
print(df.dtypes)

"""Sorting the DataFrame"""
print(df.sort_values("Fare", ascending = False).head(10))             # Sort the values according to the "Fare"
print(df.sort_values("Cabin", ascending = True, na_position ='last')) # Sort the Cabon and replacinf the NaN positions

"""Counting the occurences of variables"""
# To select a column: df.Sex ot df["Sex"]
print(df["Name"].value_counts())
print(df[["Name", "Sex"]].nunique())

"""Filtering"""
print(df["Embarked"].tail(5))

"""Masks"""
df_fare_mask = df["Fare"] < 100
df_sex_mask = df["Sex"] == "female"
df[df_fare_mask & df_sex_mask]        # Filterig with the AND conditions

df_fare_mask2 = df["Fare"] > 500
df_age_mask = df["Age"] > 70
df[df_fare_mask2 | df_age_mask]       # Filterig with the OR conditions

"""Finding the null values with .isnull()"""
null_mask = df["Cabin"].isnull()
df[null_mask]
df.isnull().sum() # Count all NaN values of DataSet

"""Dealing with missing values"""
#df.drop(labels = ["Cabin"], axis=1).head() # Dropping the column
df["columnname"].fillna(0, inplace = True) #with inplace argument, we don't have to write it as
df["columnname"] = df["columnname"].fillna(0, inplace = True # The other way to compete the code above
df["Age"].fillna("Unknown", inplace = True) #Replacing the missing values as "Unknown"
df['Age'] = df['Age'].fillna((df['Age'].median())) #Replacing the NaN with the median value

