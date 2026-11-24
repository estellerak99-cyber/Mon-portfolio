class Employe:
    def __init__(self,nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base
        
    def calculer_salaire(self):
        return self.salaire_base
    
class Developpeur(Employe):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique
        
    def calculer_salaire(self):
        return self.salaire_base + self.prime_technique
       
class Commercial(Employe):
    def __init__(self, nom, salaire_base, comission):
        super().__init__(nom, salaire_base)
        self.comission = comission
        
    def calculer_salaire(self):
        return self.salaire_base + self.comission
                  
developpeur1 = Developpeur("Bary", 300000, 120000)
developpeur2 = Developpeur("Toky", 500000, 550000)

commercial1 = Commercial("Mitia", 150000, 300000)
commercial2 = Commercial("Zara", 450000, 360000)

employes = [developpeur1, developpeur2, commercial1, commercial2]

for employe in employes:
    print(f"Employe :",employe.nom)
    print(f"Salaire :",employe.calculer_salaire(),"Ar")
    