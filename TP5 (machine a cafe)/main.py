import csv
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

dicBoisson = {}
dicPiece = {}
dicVentes = {}

def charger_pieces():
    with open('piece.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dicPiece[float(row['piece'])] = int(row['quantite'])

def sauvegarder_pieces():
    with open('piece.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['piece', 'quantite'])
        for piece, quantite in dicPiece.items():
            writer.writerow([piece, quantite])

def mettre_a_jour_quantite_piece(montant, rendu):
    # Ajouter les pièces reçues
    for piece in sorted(dicPiece.keys(), reverse=True):
        while montant >= piece:
            dicPiece[piece] += 1
            montant -= piece
            montant = round(montant, 2)

    # Rendre la monnaie
    for piece in sorted(dicPiece.keys(), reverse=True):
        while rendu >= piece and dicPiece[piece] > 0:
            dicPiece[piece] -= 1
            rendu -= piece
            rendu = round(rendu, 2)
    sauvegarder_pieces()

def creer_fichier_csv():
    with open('boissons.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'boisson', 'prix'])
        for boisson, details in dicBoisson.items():
            writer.writerow([details['id'], boisson, details['prix']])

def charger_boissons():
    with open('boissons.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dicBoisson[row['boisson']] = {'prix': float(row['prix']), 'id': int(row['id'])}

def afficher_boissons_disponibles():
    boissons = "Boissons disponibles:\n"
    for boisson, details in dicBoisson.items():
        boissons += f"{details['id']} - {boisson} : {details['prix']}€\n"
    return boissons

def afficher_pieces_disponibles():
    pieces = "Pièces disponibles:\n"
    for piece, quantite in dicPiece.items():
        pieces += f"{piece}€ : {quantite} pièces\n"
    return pieces

def compteur_ventes(boisson):
    if boisson in dicVentes:
        dicVentes[boisson] += 1
    else:
        dicVentes[boisson] = 1

def afficher_ventes():
    ventes = "Ventes:\n"
    for boisson, quantite in dicVentes.items():
        ventes += f"{boisson} : {quantite} ventes\n"
    return ventes

class BoissonApp(App):
    def build(self):
        self.title = 'Distributeur de boissons'
        self.layout = BoxLayout(orientation='vertical')

        self.boissons_label = Label(text=afficher_boissons_disponibles())
        self.layout.add_widget(self.boissons_label)

        self.label = Label(text='Entrez le numéro de la boisson que vous souhaitez (ou 0 pour quitter) : ')
        self.layout.add_widget(self.label)

        self.textinput = TextInput(multiline=False)
        self.layout.add_widget(self.textinput)

        self.button = Button(text='Valider')
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        # creer_fichier_csv()
        charger_pieces()
        charger_boissons()

        # Mettre à jour l'affichage des boissons après chargement
        self.boissons_label.text = afficher_boissons_disponibles()

        self.selected_boisson = None

        return self.layout

    def on_button_press(self, instance):
        if self.selected_boisson is None:
            self.selectionner_boisson()
        else:
            self.encaisser()

    def selectionner_boisson(self):
        try:
            boisson_id = int(self.textinput.text)
            if boisson_id == 0:
                self.result_label.text = "Merci et à bientôt!"
                exit()
            if boisson_id == -1:
                self.result_label.text = afficher_pieces_disponibles()
                return
            if boisson_id == -2:
                self.result_label.text = afficher_ventes()
                return
            for boisson, details in dicBoisson.items():
                if details['id'] == boisson_id:
                    self.selected_boisson = boisson
                    self.result_label.text = f"Vous avez choisi un(e) {boisson}. Entrez le montant à payer :"
                    self.textinput.text = ''
                    return
            self.result_label.text = "Boisson inconnue"
        except ValueError:
            self.result_label.text = "Veuillez entrer un ID valide."

    def encaisser(self):
        prix = dicBoisson[self.selected_boisson]['prix']
        try:
            montant = float(self.textinput.text)
            if montant < prix:
                self.result_label.text = "Montant insuffisant"
            else:
                rendu = montant - prix
                self.result_label.text = f"Vous avez payé {montant}€. Votre monnaie : {rendu}€"
                mettre_a_jour_quantite_piece(montant, rendu)
                compteur_ventes(self.selected_boisson)
                self.selected_boisson = None
                self.textinput.text = ''
                
              
        except ValueError:
            self.result_label.text = "Veuillez entrer un montant valide."
    
    def reset_interface(self):
        self.label.text = 'Entrez le numéro de la boisson que vous souhaitez (ou 0 pour quitter) : '
        self.result_label.text = ''
        self.textinput.text = ''
        self.selected_boisson = None

if __name__ == '__main__':
    BoissonApp().run()