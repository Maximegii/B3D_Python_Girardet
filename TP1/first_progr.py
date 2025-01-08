import datetime


naissanceDate = datetime.date(2004,6,8)
dateDuJour = datetime.date.today()
age_en_jours = dateDuJour - naissanceDate 
age_en_annee = dateDuJour.year - naissanceDate.year
age_en_mois = age_en_annee * 12
age_en_semaine = age_en_annee * 52

print("mon age en annee: ", age_en_annee)
print("mon age en mois: ", age_en_mois)
print("mon age en jour: ", age_en_jours)
print("mon age en semaine:", age_en_semaine)

maChaine = 'une chaine de carractere'

def get_vowels_numbers(word):

    nb_vowels = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y','A','E','I','O','Y']:
            nb_vowels += 1
    return nb_vowels


vowels_count = get_vowels_numbers(maChaine)
print("Il y a", vowels_count, "voyelles dans :", maChaine)

def get_letter(word):

    nb_letter = 0 
    letter_searched = 'e'
    for letter in word:
        if letter in letter_searched:
            nb_letter += 1
    return nb_letter
    
letter_count = get_letter(maChaine)

print("il y'a", letter_count,  "dans cette chaine") 

print(maChaine.split(','))

def search_letter(word):

    nb_letter = 0 
    letter_searched = 'a'
    
    if letter_searched in word:
        reponse =  print ("la lettre", letter_searched, "est présente dans la chaine de carractere")
    return reponse
    
letter_recherche = search_letter(maChaine)





