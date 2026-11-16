class Livre:
    def __init__(self,titre, auteur, annee):
        self.titre =  titre
        self.auteur = auteur
        self.annee = annee
    
    def afficher_details(self):
        print(f"Titre : {self.titre}") 
        print(f"Auteur : {self.auteur}")  
        print(f"Annee : {self.annee}") 
    
class Bibliotheque:
    def __init__(self,):
        self.livre = []
    
    def ajouter_livres(self,livre):
        self.livre.append(livre)
        
    def afficher_catalogue(self):
        print(f"Catalogue")
        for livre in self.livre:
            livre.afficher_details()
            
#Creation des objets livres     
livre1 = Livre("Les Miserabeles","Victor Hugo",1862) 
livre2 = Livre("Le Petit Prince","Antoine ST",1943)  
livre3 = Livre("L'Etranger", "Albert Camus", 1942) 

#Creation de bibliotheque
bibliotheque = Bibliotheque()
        
#Ajouter des livres a la bibliotheque
bibliotheque.ajouter_livres(livre1)  
bibliotheque.ajouter_livres(livre2)      
bibliotheque.ajouter_livres(livre3)

#Afficher catalogue
bibliotheque.afficher_catalogue()