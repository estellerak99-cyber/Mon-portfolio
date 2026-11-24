class Transport:
    def se_deplacer(self):
        print(f"Le transport se deplace")

class Voiture:
    def se_deplacer(self):
        print(f"La voiture se deplace sur la rouete")

class Avion:
    def se_deplacer(self):
        print(f"L'avion vole dans les aires")  

class Bateau:
    def se_deplacer(self):
        print("Le bateau navigue sur l'eau")  
        
#Creation des objets         
voiture = Voiture() 
avion = Avion() 
bateau = Bateau() 

transport = [voiture, avion, bateau]

#Parcours
for transport in transport:
    transport.se_deplacer()

               