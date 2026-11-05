class Employe:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai{self.age} ans.")  
          
          
class Developpeur(Employe):
    def __init__(self, nom, age, langage_prefere):
        super().__init__( nom, age)
        self.langage_prefere = langage_prefere
        
    def se_presenter(self):
        Employe.se_presenter(self) 
        print(f"Mon langage de programmation préféré est le {self.langage_prefere}.")   
        
        
        
developpeur1 = Developpeur("Soa", 25, "Python")     

developpeur1.se_presenter()       
                  