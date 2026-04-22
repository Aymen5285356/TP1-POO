#1)
class MaClasse:
    x = 23
    y = x + 5

    def affiche(self):
        print("x =", self.x)
        print("y =", self.y)
#2)
class Personne:
    def __init__(self, nom, prenom, adresse, age):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.age = age

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
        print("Adresse:", self.adresse)
        print("Âge:", self.age)
#3)
class Voiture:
    def __init__(self, marque, modele, couleur, kilometrage):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.kilometrage = kilometrage

    def setMarque(self, marque):
        self.marque = marque

    def setModele(self, modele):
        self.modele = modele

    def setCouleur(self, couleur):
        self.couleur = couleur

    def setKilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def affiche(self):
        print("Marque:", self.marque)
        print("Modèle:", self.modele)
        print("Couleur:", self.couleur)
        print("Kilométrage:", self.kilometrage)
#4)
class CompteBancaire:
    def __init__(self, numeroCompte, titulaire, solde):
        self.numeroCompte = numeroCompte
        self.titulaire = titulaire
        self.solde = solde

    def setNumeroCompte(self, numero):
        self.numeroCompte = numero

    def setTitulaire(self, titulaire):
        self.titulaire = titulaire

    def setSolde(self, solde):
        self.solde = solde

    def affiche(self):
        print("Numéro:", self.numeroCompte)
        print("Titulaire:", self.titulaire)
        print("Solde:", self.solde)
#5)
class Livre:
    def __init__(self, titre, auteur, nombrePages, prix):
        self.titre = titre
        self.auteur = auteur
        self.nombrePages = nombrePages
        self.prix = prix

    def setTitre(self, titre):
        self.titre = titre

    def setAuteur(self, auteur):
        self.auteur = auteur

    def setNombrePages(self, nb):
        self.nombrePages = nb

    def setPrix(self, prix):
        self.prix = prix

    def affiche(self):
        print("Titre:", self.titre)
        print("Auteur:", self.auteur)
        print("Pages:", self.nombrePages)
        print("Prix:", self.prix)