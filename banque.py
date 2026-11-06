class CompteBanque:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def afficher_solde(self):
        print(f"Titulaire :{self.titulaire}")
        print(f"Solde disponoble :{self.solde} Ar")
    
class CompteEpargne(CompteBanque):
    def __init__(self, nom, solde, taux_interet):
        super().__init__(nom, solde)
        self.taux_interet = taux_interet
 
    def afficher_solde(self):
       super().afficher_solde() 
       print(f"Taux d'interet: {self.taux_interet} %")   
     
     
compte_miora = CompteEpargne("Miora",  500000, 5) 
compte_miora.afficher_solde()