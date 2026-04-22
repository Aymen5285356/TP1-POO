#1)
class Maison:
    def setAdresse(self, adresse):
        self.adresse = adresse

    def setNbrEtage(self, nbr):
        self.nbrEtage = nbr

    def setCouleur(self, couleur):
        self.couleur = couleur

    def setSurface(self, surface):
        self.surface = surface

    def affiche(self):
        print("Adresse:", self.adresse)
        print("Nombre d'étages:", self.nbrEtage)
        print("Couleur:", self.couleur)
        print("Surface:", self.surface)
#2)
class Personne:
    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

    def __del__(self):
        print("Objet Personne supprimé")

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setAge(self, age):
        self.age = age

    def setAdresse(self, adresse):
        self.adresse = adresse

    def affiche(self):
        print("Nom:", self.nom)
        print("Prénom:", self.prenom)
        print("Âge:", self.age)
        print("Adresse:", self.adresse)
#3)
class Produit:
    def __init__(self, reference, nom, prix, quantite):
        self.reference = reference
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __del__(self):
        print("Produit supprimé")

    def setReference(self, ref):
        self.reference = ref

    def setNom(self, nom):
        self.nom = nom

    def setPrix(self, prix):
        self.prix = prix

    def setQuantite(self, qte):
        self.quantite = qte

    def affiche(self):
        print("Référence:", self.reference)
        print("Nom:", self.nom)
        print("Prix:", self.prix)
        print("Quantité:", self.quantite)