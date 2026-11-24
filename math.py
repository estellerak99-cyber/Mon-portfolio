import math

class Forme:
    def calculer_surface(self):
        return 0
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def calculer_surface(self):
        return self.longueur * self.largeur
    
class Carre:
    def __init__(self, cote):
        self.cote = cote
    def calculer_surface(self):
        return self.cote *self.cote   
class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
    def calculer_surface(self):
        return math.pi * self.rayon**2
       
#Creation des objets
rectangle = Rectangle(6,4)  
carre = Carre(4)    
cercle = Cercle(5)
 
formes =[rectangle, carre, cercle] 
noms = ["Rectangle","Carre","Cercle"]
for nom, forme in zip(noms, formes):
    print(f"{nom}: surface = {round(forme.calculer_surface(),2)}")