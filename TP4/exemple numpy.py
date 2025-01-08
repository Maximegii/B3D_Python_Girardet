import numpy as np

# création manuelle
# maListe=[[1,2,3],[4,5,6]]
# monT2D=np.array(maListe)
# print (monT2D)

# listeHeterogene=["charlene", 1, True]
# monTableau=np.array(listeHeterogene)
# print(monTableau)
# print(type(monTableau[1]))

# #création automatique
# # zeros
# TdeZero=np.zeros((3,4))
# print(TdeZero)
# # un 
# TdeUns=np.ones((3,4))
# print(TdeUns)
# #random
# TdeRand=np.random.random((3,4))
# print(TdeRand)
# # progression arithmétique
# TdeArange=np.arange(10, 20, 2)
# print(TdeArange)

# création depuis une liste
# mesNotes = {
#             "tp1": 12,
#             "tp2": 15,
#             "tp3": 8,
#             "tp4": 10,
#             "tp5": 16,
#         }
# maListe = [mesNotes[note] for note in mesNotes]
# print (maListe)
# monTableau = np.array(maListe)
# print(monTableau)

# ajouter une dimension
# monTableau1=np.array([1,2,3])
# monTableau3=np.array([4,5,6])
# monTableau2D=np.array([monTableau1, monTableau3])
# print(monTableau2D)

# filtrage booléen
maListe=np.array([[1,2,3,4],[4,5,17,8],[8,9,10,11],[11,12,13,14]])

# filtreBool=np.array([True,False,True,False], dtype=bool)
# # on filtre les lignes de maListe
print (maListe)
# print ('---')
# print (maListe[filtreBool , : ])
# print ('---')
# # on filtre les colonnes de maListe
# print (maListe[: , filtreBool])
# print ('---')
# # on filtre les colonnes de maListe
# print (maListe[filtreBool, filtreBool])


print (maListe >9)

print (maListe.max())
print (np.amax(maListe))
print (maListe.max(axis=0))
print (maListe.max(axis=1))

print (np.mean(maListe, axis=0))
print (np.mean(maListe, axis=1))
print (maListe.mean( axis=1))
print(np.median(maListe, axis=0))
print(np.median(maListe, axis=1))
# print (maListe.median( axis=1))  # ne fonctionne pas