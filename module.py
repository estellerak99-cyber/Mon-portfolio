class Module:
    def __init__(self, titre, nombres_heures):
        self.titre = titre
        self.nombres_heures = nombres_heures
        
class Apprenant:
    def __init__(self, nom, identifiant, modules):  
        self.nom = nom
        self.identifiant = identifiant
        self.modules = []
    
    def inscrire(self, module):
        self.modules.append(module)    
            
    def afficher_modules(self):
         print(f"Apprenant : {self.nom}")
         print(f"Identifiant : {self.identifiant}")   
         print(f"Module : ")
         
         for module in self.modules:
             print(f"{module.titre}: {module.nombres_heures} heures")   

#Creation des modules 
module1 = Module("Python" ,20)
module2 = Module("HTML", 22) 
module3 = Module("java", 15)     

#Creation des deux apprenants
apprenant1 = Apprenant("Koto",3, "Python,Java")  
apprenant2 = Apprenant("Miora",4, "HTML, Java") 

#Inscripton Koto
apprenant1.inscrire(module1)
apprenant1.inscrire(module3)
#Incription Miora
apprenant2.inscrire(module2)
apprenant2.inscrire(module3)

#Afficher les inscriptons
apprenant1.afficher_modules()
apprenant2.afficher_modules()
 