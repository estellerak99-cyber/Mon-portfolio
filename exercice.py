class Module:
    def __init__(self,titre ,duree):
        self.titre = titre
        self.duree = duree
        
class Formation:
    def __init__(self, intitule):
        self.intitule = intitule
        self.modules = []
    
    def ajouter_modules(self, module):
        self.modules.append(module)

class Apprenant:
    def __init__(self, nom):
        self.nom = nom
        self.formations = []
        
    def s_inscrire(self, formation):
         self.formations.append(formation)
        
    def afficher_parcours(self):
        print(f"Apprenant : {self.nom}")
        
        for formation in self.formations:
            print(f"Formation : {formation.intitule}") 
            for module in formation.modules:
                print(f"Module : {module.titre}")
                print(f"Duree : {module.duree} heures")

#Creation de module
module1 = Module("POO",5)
module2 = Module("HTML",4) 
module3 = Module("Python",8)

#Creations des formations
formation1 = Formation("Language de programmation")
formation2 = Formation("Developpement Web")  
#Ajouter des modules
formation1.ajouter_modules(module1)                 
formation1.ajouter_modules(module2) 
formation2.ajouter_modules(module1)  
formation2.ajouter_modules(module3)  

#Creation des apprenants
apprenant1 = Apprenant("Luc") 
apprenant2 = Apprenant("Aina") 

#Inscription des apprenants
apprenant1.s_inscrire(formation1)

apprenant2.s_inscrire(formation2)

#Affiche le parcours
print("PARCOURS DES APPRENANTS")
apprenant1.afficher_parcours()
apprenant2.afficher_parcours()
                         
                