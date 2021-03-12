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
plt.title('Iris')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()


"""Box plot Iris-setosa"""
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]]
c1= ["Iris-setosa"]
new_iris_setosa = new_iris[new_iris["Species"].isin(c1)]
print(new_iris_setosa)
plt.figure(figsize = (10, 7))
plt.title('Iris-setosa')
plt.xlabel('Categories')
plt.ylabel('Values')
new_iris_setosa.boxplot()
plt.show()

"""Box plot Iris-versicolor"""
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]]
c1= ["Iris-versicolor"]
new_iris_versicolor = new_iris[new_iris["Species"].isin(c1)]
print(new_iris_versicolor)
plt.figure(figsize = (10, 7))
plt.title('Iris-versicolor')
plt.xlabel('Categories')
plt.ylabel('Values')
new_iris_versicolor.boxplot()
plt.show()

"""Box plot Iris-virginica"""
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]]
c1= ["Iris-virginica"]
new_iris_virginica = new_iris[new_iris["Species"].isin(c1)]
print(new_iris_virginica)
plt.figure(figsize = (10, 7))
plt.title('Iris-virginica')
plt.xlabel('Categories')
plt.ylabel('Values')
new_iris_versicolor.boxplot()
plt.show()