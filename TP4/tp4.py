import numpy 
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os

rep_courant = os.path.abspath(os.path.dirname(__file__))

# Chemin absolu du fichier
chemin_fichier = os.path.join(rep_courant, "winter_olympics_medals.csv")

df = pd.read_csv(chemin_fichier, sep=',', encoding="ISO-8859-1", quoting=csv.QUOTE_ALL, lineterminator='\n')

print (df.year.unique())


print (df.country.unique())

print (df.sport.unique())

dataframe = pd.DataFrame(df, columns = ['country', 'host', 'medal'])
# print (dataframe)

rslt_df = dataframe.loc[dataframe['host'] == 1]

print ("pays organisateur ayant gagner une médail", rslt_df.country.unique())

moyenne_medaille = df.groupby('country').size().mean()
print(f"Moyenne de médailles par pays : {moyenne_medaille}")

moyenneDataframe = pd.DataFrame(df, columns = ['country','medal','year'])

moyenne_year_df = moyenneDataframe[(moyenneDataframe['year'] >= 1920) & (moyenneDataframe['year'] <= 1970)]

# print (moyenne_year_df)

medailles_par_pays = moyenne_year_df.groupby('country').size()

# Calcul de la moyenne des médailles par pays
moyenne_medailles = medailles_par_pays.mean()

print ("moyenne des medailles par pays entre 1920 et 1970 :" , moyenne_medailles)
 

# Filtrer les données pour les USA, URS et RUS
df_usa = df[df['country'] == 'USA']
df_russie = df[df['country'].isin(['URS', 'RUS'])]

# Grouper par année et compter les médailles
medailles_usa = df_usa.groupby('year').size()
medailles_russie = df_russie.groupby('year').size()
# Ajouter des années manquantes pour Russie/URS
medailles_russie = medailles_russie.reindex(medailles_usa.index, fill_value=0)

# Recréer le graphique avec valeurs corrigées
plt.plot(medailles_usa.index, medailles_usa.values, label='USA', marker='o')
plt.plot(medailles_russie.index, medailles_russie.values, label='Russie/URS', marker='o')

plt.xlabel("Année")
plt.ylabel("Nombre de médailles")
plt.title("Nombre de médailles par année (USA vs Russie/URS)")
plt.legend()
plt.grid()
plt.show()









