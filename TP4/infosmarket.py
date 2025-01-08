import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import openpyxl

rep_courant = os.path.abspath(os.path.dirname(__file__))

# Chemin absolu du fichier
chemin_fichier = os.path.join(rep_courant, "Camp_Market 1.csv")

df = pd.read_csv(chemin_fichier, sep=';', lineterminator='\r')

### OBSERVATION DES DONNEES

# on regarde rapidement le contenu du dataset
print(df.info())

print (df.head(10))

# on regarde le min et le max du champ Year_Birth
print ("Kidhome Min / MAX: " + str(df['Kidhome'].min()) + " / " + str(df['Kidhome'].max()))

# on liste les niveaux d'éducation
print (df['Education'].unique())

# idem pour les statuts matrimoniaux
print (df['Marital_Status'].unique())

# On analyse les revenus
print('description des revenus')
print (df['Income'].describe())

# on clusterise les années de naissance
print ("description des années de naissance")
print (df['Year_Birth'].describe())

print ("ventilation des niveau d'études")
print (df['Education'].value_counts())

### REGROUPEMENT DES DONNEES

# on regroupe les statuts marital Alone par Single
df['Marital_Status'] = df['Marital_Status'].replace('Alone', 'Single')
df['Marital_Status'] = df['Marital_Status'].replace('Divorced', 'Single')
df['Marital_Status'] = df['Marital_Status'].replace('Widow', 'Single')

df['Marital_Status'] = df['Marital_Status'].replace('Married', 'Together')
# on supprime la ligne avec statut marital Absurd
df = df[df['Marital_Status'] != 'Absurd']
df = df[df['Marital_Status'] != 'YOLO']
print (df['Marital_Status'].value_counts())

# Calculer la moyenne des revenus
mean_income = df['Income'].mean()

# Remplacer les valeurs manquantes par la moyenne
df['Income'] = df['Income'].fillna(mean_income)


# on totalise les AcceptedCmp de 1 à 5 et la dernière campagne dans une colonne
df['TotalCmp'] = df['AcceptedCmp1'] + df['AcceptedCmp2'] + df['AcceptedCmp3'] + df['AcceptedCmp4'] + df['AcceptedCmp5' ] + df['Response']
# on supprime ensuite les données des campagnes
df = df.drop(columns=['AcceptedCmp1'])
df = df.drop(columns=['AcceptedCmp2'])
df = df.drop(columns=['AcceptedCmp3'])
df = df.drop(columns=['AcceptedCmp4'])
df = df.drop(columns=['AcceptedCmp5'])
df = df.drop(columns=['Response'])

# compte le nombre ligne par le nombre de campagnes acceptées
print ("totalisation des campagnes acceptées")
print (df['TotalCmp'].value_counts())

# exit()

### VISUALISATION GRAPHIQUES DES DONNEES
# il est possible d'utiliser une autre valeur pour visualiser la distribution des données et le boxplot

if True: 
    # Histogrammes
    df['Year_Birth'].hist(bins=20)
    plt.title('Distribution de l\'âge')
    plt.xlabel('Year_Birth')
    plt.ylabel('Fréquence')
    plt.show()

    # Boxplot pour détecter les outliers
    sns.boxplot(x=df['Income'])
    plt.title('Boxplot du revenu')
    plt.show()

## PURGES DES DONNEES


# on purge les lignes avec TotalCmp = 0
df = df[df['TotalCmp'] != 0]
# on enleve les revenus trop faible ou trop élevées
df = df[df['Income'] > 10000] 
df = df[df['Income'] < 200000]

df = df[df['Year_Birth'] > 1940]

if False: 
    df['Year_Birth'].hist(bins=20)
    plt.title('Distribution de l\'âge nettoyée')
    plt.xlabel('Year_Birth')
    plt.ylabel('Fréquence')
    plt.show()

    # Boxplot pour détecter les outliers
    sns.boxplot(x=df['Income'])
    plt.title('Boxplot du revenu nettoyé')
    plt.show()


### CORRELATION DES DONNEES

# on remplace les informations alphabétiques par des valeurs numériques

df['Marital_Status'] = df['Marital_Status'].replace('Single', 1)
df['Marital_Status'] = df['Marital_Status'].replace('Together', 2)

# on supprime le Dt_Customer
df = df.drop(columns=['Dt_Customer'])

# on remplace la graduation des diplomes par une valeur numérique
df['Education'] = df['Education'].replace('Basic', 1)
df['Education'] = df['Education'].replace('2n Cycle', 2)
df['Education'] = df['Education'].replace('Graduation', 3)
df['Education'] = df['Education'].replace('Master', 4)
df['Education'] = df['Education'].replace('PhD', 5)


correlation_matrix = df.corr()

# Afficher la matrice de corrélation
print(correlation_matrix)

# corrélations entre 'TotalCmp' et les autres colonnes spécifiques :
correlation_score = correlation_matrix['TotalCmp']

# on supprime les colonnes dont les corrélations sont nulles
correlation_score = correlation_score.dropna()

# Trier les corrélations par ordre décroissant pour voir celles qui sont les plus fortes
correlation_score_sorted = correlation_score.sort_values(ascending=False)

# Afficher les résultats triés
print(correlation_score_sorted)

# on sélectionne ici les variables dont on souhaite analyse la correlation
##########################################################################
yvalue = "NumCatalogPurchases"
xvalue = "TotalCmp"

features = df[[xvalue, yvalue]]  # Exemple avec seulement deux variables pour une visualisation facile

# Standardisation des données (important pour les algorithmes de clustering)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)


inertia = []  # Liste pour stocker la somme des erreurs quadratiques

# Tester différents nombres de clusters (par exemple de 1 à 10)
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Tracer la courbe pour la méthode du coude
if True: 
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
    plt.title('Méthode du Coude pour déterminer le nombre optimal de clusters')
    plt.xlabel('Nombre de clusters')
    plt.ylabel('Inertie')
    plt.grid(True)
    plt.show()


# Appliquer K-Means avec un nombre de clusters choisi (par exemple 3)
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(features_scaled)

# Visualisation des résultats
plt.figure(figsize=(8, 6))


# on affiche un graphique 2D
sns.scatterplot(x=df[xvalue], y=df[yvalue], hue=df['cluster'], palette='Set1', s=100, marker='o')

# Afficher les centres des clusters
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], s=200, c='red', marker='X', label='Centres des clusters')

# Ajouter des labels et une légende
plt.title('Clustering des données (K-Means)', fontsize=14)
plt.xlabel(xvalue)
plt.ylabel(yvalue)
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()

from sklearn.linear_model import LinearRegression

# Modèle de régression linéaire pour prédire le revenu en fonction de l'âge et du score
X = df[[yvalue, xvalue]]  # Variables indépendantes
y = df['TotalCmp']  # Variable cible

model = LinearRegression()
model.fit(X, y)

# Prédiction
y_pred = model.predict(X)
print(f"Coefficient de régression : {model.coef_}")
print(f"Intercept : {model.intercept_}")
print(f"Score de régression (R²) : {model.score(X, y)}")


# on exporte au format excel le dataframe
df.to_excel('Camp_Market 1_cleaned.xlsx', index=False)
