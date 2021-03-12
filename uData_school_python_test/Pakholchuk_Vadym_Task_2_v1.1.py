# Завдання №2 Пахольчук Вадим Володимрович

"""Import block"""

import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import numpy

"""importing data"""

iris = pandas.read_csv('iris.csv')
print(iris.head(10))
iris.info()

""""Scatter plot"""
iris["Id"] = iris.index
iris["Ratio"] = iris["SepalLengthCm"]/iris["SepalWidthCm"]
sns.lmplot(x = "Id", y = "Ratio", data = iris, hue = "Species", fit_reg = False, legend = False)

plt.legend()
plt.show()

"""Box plot iris"""
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]]
print(new_iris)
plt.figure(figsize = (10, 7))
new_iris.boxplot()
plt.show()