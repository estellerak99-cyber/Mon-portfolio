class Formation:
    def __init__(self, intitule, duree):
        self.intitule = intitule
        self.duree = duree
        
class Etudiant:
    def __init__(self, nom, age, formation):
            self.nom = nom
            self.age = age
            self.formation = formation
            
    def afficher_information(self):
        print(f"Nom : {self.nom}")
        print(f"Age : {self.age}")
        print(f"Formation : {self.formation.intitule}") 
        
# Créatin d'objet formation
formation1= Formation("Restauration", 2)

# Créatin des etudiants
etudiant1 = Etudiant("Miora", 23, formation1)   
etudiant2 = Etudiant("Koto", 22,  formation1)          

# Afficher les informations 
print("Etudiant1")               
etudiant1.afficher_information()

print("Etudiant2")
etudiant2.afficher_information()  