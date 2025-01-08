import os
import pandas as pd
import csv
import matplotlib.pyplot as plt

rep_courant = os.path.abspath(os.path.dirname(__file__))
chemin_fichier = os.path.join(rep_courant, "titanic.csv")
df = pd.read_csv(chemin_fichier, sep=',', encoding="ISO-8859-1", quoting=csv.QUOTE_ALL, lineterminator='\n')

# Affiche les premières lignes du DataFrame
print(df.head())
print(df.info())


partDf = df.loc[:, ['Survived','Pclass', 'Sex', 'Age']] #[df['Survived'] == 1]
partDf['Sex'] = partDf['Sex'].str.replace('female', '0')
partDf['Sex'] = partDf['Sex'].str.replace('male', '1')
partDf['Sex'] = partDf['Sex'].astype(int)

print (partDf.info())

dfTotal = partDf.loc[partDf['Sex'] == 0][partDf['Pclass'] == 1][partDf['Age'] > 20]
dfSurvivant = partDf.loc[partDf['Survived'] == 1][partDf['Sex'] == 0][partDf['Pclass'] == 1][partDf['Age'] > 20]
print ("Femme 1er classe supérieur à 20 ans")
print(dfTotal.describe())
print(dfSurvivant.describe())

print ("Homme 3e classe supérieur à 20 ans")
dfTotal = partDf.loc[partDf['Sex'] == 1][partDf['Pclass'] == 3][partDf['Age'] > 20]
dfSurvivant = partDf.loc[partDf['Survived'] == 1][partDf['Sex'] == 1][partDf['Pclass'] == 3][partDf['Age'] > 20]
print(dfTotal.describe())
print(dfSurvivant.describe())

# on filtre les personne de 3e classe ayant survécu pour avoir la moyenne de leur age
dfSurvivant = partDf.loc[partDf['Survived'] == 1]

for classe in range(1, 4) :
	dfClasse = partDf.loc[partDf['Pclass'] == classe]
	dfClasseSurvivant = dfClasse.loc[partDf['Survived'] == 1]

	print ("nombre de personne de la classe ", classe,':', dfClasse['Pclass'].count())
	print ("Moyenne d'age des  ", classe, " classe vs survivant de la classe vs survivant total")
	print(int(dfClasse['Age'].mean()), "vs", int(dfClasseSurvivant['Age'].mean()), "vs", int(dfSurvivant['Age'].mean()))



# ## graphique 3D
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x = partDf['Age']
# y = partDf['Sex']
# z = partDf['Pclass']
# ax.scatter(x, y, z)
# plt.show()


# print(dfSurvivant.describe())
# print( dfSurvivant['Sex'].value_counts())

# Affiche les statistiques descriptives du DataFrame
# print(df.describe())

# # Affiche les informations sur les colonnes du DataFrame
# print(df.info())


# plt.hist(df['Age'], bins=20)
# plt.xlabel('Age')
# plt.ylabel('Nombre de passagers')
# plt.show()

# labels = ['Femmes', 'Hommes']
# sizes = df['Sex'].value_counts()
# colors = ['pink', 'lightblue']

# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
# plt.axis('equal')
# plt.show()

# survived_by_class = df.groupby(['Pclass', 'Survived']).size().unstack()
# survived_by_class.plot(kind='bar', stacked=True)
# plt.xlabel('Classe de billet')
# plt.ylabel('Nombre de passagers')
# plt.show()

