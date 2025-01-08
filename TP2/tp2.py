import os
import json

dicEleves = { 
	'titi' : {'notes':{'tp1':10, 'tp2':13,'tp3':17}, 'appréciation': 'moyenne' }, 
	'toto' : {'notes':{'tp1':19, 'tp2':11,'tp3':14}, 'appréciation': 'Très Bien' }, 
	'tata' : {'notes':{'tp1':15,'tp2':8,'tp3':13}, 'appréciation': 'Bonne' },
	'tutu' : {'notes':{'tp3':15,'tp4':13}, 'appréciation': 'Bonne' },
    'tete' : {'notes':{}, 'appréciation': 'Absent' },
}

# Créer le dossier principal
os.makedirs('eleves', exist_ok=True)

# Créer un sous-dossier pour chaque élève
for eleve in dicEleves.keys():
    os.makedirs(os.path.join('eleves', eleve), exist_ok=True)

for eleve, data in dicEleves.items():
    # Chemin du sous-dossier de l'élève
    eleve_folder = os.path.join('eleves', eleve)

    # Écrire le fichier appreciation.txt
    with open(os.path.join(eleve_folder, 'appreciation.txt'), 'w') as app_file:
        app_file.write(data['appréciation'])
    
    # Écrire le fichier notes.csv
    notes = data['notes'].values() 
    if notes:
         with open(os.path.join(eleve_folder, 'notes.csv'), 'w') as notes_file:
            notes_file.write("TP,Notes\n")  # Entête du fichier CSV
            for tp, note in data['notes'].items():
                 notes_file.write(f"{tp},{note}\n")

statistiques = {}

for eleve, data in dicEleves.items():
    notes = list(data['notes'].values())
    if notes:  
        moyenne = sum(notes) / len(notes)
        min_note = min(notes)
        max_note = max(notes)
    else:  # Si l'élève n'a pas de notes
        moyenne = min_note = max_note = "Pas de note enregistre"

    statistiques[eleve] = {
        'moyenne': moyenne,
        'min': min_note,
        'max': max_note
    }

# Écrire dans un fichier JSON
with open(os.path.join('eleves', 'statistiques.json'), 'w') as json_file:
    json.dump(statistiques, json_file, indent=4)