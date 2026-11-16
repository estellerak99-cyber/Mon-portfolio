class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        
class Commande:
    def __init__(self,produit, quantite):
        self.produit = produit
        self.quantite = quantite
        
    def calcul_total(self):
        return self.produit.prix * self.quantite
               
    def afficher_commande(self):
        print(f"Le nom du produit : {self.produit.nom}") 
        print(f"Sa quantite : {self.quantite}")
        print(f"Montant total : {self.calcul_total()} Ar")
        
        
#Création de produit
produit1 = Produit("Telephone",65000) 
#Création commande
commande1 = Commande(produit1,6)

print("Le commande")
commande1.afficher_commande()  
            