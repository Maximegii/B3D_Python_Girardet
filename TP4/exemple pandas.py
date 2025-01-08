import pandas as pd
import numpy as np
import csv
import os

# s = pd.Series([1.3, 2, 5.3, 7]) # série numérique flottante.
# print (s)

# df1 = pd.DataFrame({
# 		'empl':['Bob', 'Jake', 'Lisa', 'Sue'],
# 		'group':['Accounting', 'Engineering', 'Engineering','HR'],
#         'age':[25, 32, 27, 38]
# 	}
# 	, index=[1,220,233,4]
# )
# print(df1)


# Chemin absolu du répertoire courant
rep_courant = os.path.abspath(os.path.dirname(__file__))

# Chemin absolu du fichier
chemin_fichier = os.path.join(rep_courant, "listedefactures.csv")

# # Lecture du fichier CSV avec Pandas
df = pd.read_csv(chemin_fichier, sep=';', encoding="ISO-8859-1", quoting=csv.QUOTE_ALL, lineterminator='\n')
print (df)
print (df.head(10))
# print (df.shape())
print(df.info() )
# print (df.size())


partDf = df.loc[30:200, ['Document - Numéro du document','Document - Date', 'Document - Total Brut HT', 'Document - Total TTC']]
print (partDf)

partDf.columns = ['Numéro', 'Date', 'Total_HT', 'Total_TTC']
print (partDf)

partDf.rename(columns = {'Numéro':'ref'}, inplace = True)
print (partDf)
print (partDf.info())
# # affiche le nombre de références uniques de facture
print (partDf['ref'].unique())
print ("nb fact", len(partDf['ref'].unique()))

# # renvoie le nombre de date différentes
print (df['Document - Date'].value_counts())

# pour réaliser la conversion en float
partDf['Total_TTC'] = partDf['Total_TTC'].str.replace(',', '.')
partDf['Total_TTC'] = partDf['Total_TTC'].astype(float)
print (partDf)
# totalisation par colonne
print(partDf['Total_TTC'].sum())



partDf['Total_HT'] = partDf['Total_HT'].str.replace(',', '.')
partDf['Total_HT'] = partDf['Total_HT'].astype(float)

print (partDf)

partDf['Total_TVA'] = partDf['Total_TTC'] - partDf['Total_HT']
print (partDf.info())

# print (partDf)

#concaténation de deux séries
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 7])
print(pd.concat([ser1, ser2]))

# exemple de merge
df1 = pd.DataFrame({'Emp': ['Bob', 'Jake','Lisa','Sue'], 'group': ['Comptable', 'Ingenieur', 'Ingenieur','RH']})
df2 = pd.DataFrame({'Emp':['Lisa', 'Bob', 'Jake', 'Sue', 'helen'],'hire_date':[2004, 2014, 2012, 2014, 2016]})
print(df1,"\n\n")
print(df2,"\n\n")
df3=df2.merge(df1, on = ['Emp'], how="outer")
print (df3,"\n\n")
df3 = pd.merge(df1, df2)
print (df3,"\n\n")

# # # exemple d'aggregation avec groupby
df4 = pd.DataFrame({'Emp': ['Bob', 'Jake','Lisa','Sue'], 'group': ['Comptable', 'Ingenieur', 'Ingenieur','RH'], 'salaire':[1000, 2000, 3000, 4000]})
print(df4,"\n\n")
print(df4.groupby('group').mean(numeric_only=True),"\n\n")
print(df4.groupby('group').sum(numeric_only=True),"\n\n")


# # # # # Sélectionner uniquement les colonnes numériques
numeric_cols = df4.select_dtypes(include=np.number).columns.tolist()
print(df4.groupby('group')[numeric_cols].agg(['mean', 'sum']),"\n\n")