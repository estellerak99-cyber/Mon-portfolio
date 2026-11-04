class Telephone:
    def __init__(self, marque, couleur, batterie):
        self.marque = marque
        self.couleur = couleur
        self.batterie = batterie
        
    def se_presenter(self):
     print(f"Mon telephone est {self.marque}  de couleur {self.couleur}, avec une batterie de {self.batterie} mAH")  
     
    def appeler(self):
        print(f"Le téléphone est en train d'appeler.")  
        
    def envoyer_message(self):
        print(f"Le téléphone envoie un message.") 
        
        
telephone1 = Telephone("OPPO", "noir", 5000)
telephone2 = Telephone("TECNO", "bleu", 5500)

telephone1.se_presenter()
telephone1.appeler()
telephone1.envoyer_message()

telephone2.se_presenter()
telephone2.appeler()
telephone2.envoyer_message()
    