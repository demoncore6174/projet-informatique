import time
import random
from grove.grove_led import GroveLed
from grove.grove_button import GroveButton
from grove.chainable_led import ChainableLED

class Simon:
    def __init__(self):
        self.score = 0
        self.pseudo_jeu = ""
        self.sequence = []
        self.level = 1
        self.sequence = 4
        self.boutton = [Boutton(16,0), Boutton(18,1), Boutton(24,2), Boutton(26,3)]
        self.leds = ChainableLED(6, 5, 4)
        self.partie = True
        self.pseudo()
    def jeu(self):
        if self.level == 1:
           print(" La partie va à présent commencer  dans quelques instants...")
           time.sleep(2)
           print("La partie commence:")
        print("Level : ", self.level)
        time.sleep(1)
        nbr_sequence = self.sequence
        self.sequence = [random.randint(0,3) for i in range(nbr_sequence)]
        for element in self.sequence:
            if element == 0:
                self.leds.setColorRGB(0,0,40,0)
                time.sleep(1)
                self.leds.setColorRGB(0,0,0,0)
            elif element == 1:
                self.leds.setColorRGB(40,0,0,1)
                time.sleep(1)
                self.leds.setColorRGB(0,0,0,1)
            elif element == 2:
                self.leds.setColorRGB(0,40,0,2)
                time.sleep(1)
                self.leds.setColorRGB(0,0,0,2)
            else:
                self.leds.setColorRGB(40,40,40,3)
                time.sleep(1)
                self.leds.setColorRGB(0,0,0,3)
            time.sleep(1)
        print("à toi de jouer")
    def pseudo(self):
        self.pseudo_jeu = input("Veuillez saisir votre pseudo: ") 
        print("Bienvenue", self.pseudo_jeu)
        self.jeu()       
    
    def signal(self,emplacement):
        if emplacement == 0:
            self.leds.setColorRGB(0,0,40,0)
        elif emplacement == 1:
            self.leds.setColorRGB(40,0,0,1)
        elif emplacement == 2:
            self.leds.setColorRGB(0,40,0,2)
        else:
            self.leds.setColorRGB(40,40,40,3)
        if self.sequence[0] == emplacement:
            print("bien joué")
            self.sequence.remove(emplacement)
            if len(self.sequence) == 0:
                print("gagné")
                time.sleep(1)
                self.leds.setColorRGB(0,0,0,emplacement)
                self.gagne_level()
        else:
            print("perdu")
            print("Votre score final est de ", self.score)
            print("Vous êtes allé jusqu'au level:",self.level)
            self.partie = False
            print(self.pseudo_jeu, "Veuillez appuyer sur le boutton 1 pour relancer une partie")
            
    def gagne_level(self):
        self.score += 200 * self.level
        self.level += 1
        self.sequence = 4 + (self.level //3)
        time.sleep(1)
        self.jeu()
    
    def réinitialisation_jeu(self):
        self.score = 0
        self.level = 1
        self.sequence = 4
        self.partie = True
        self.jeu()
            
                        
              


class Boutton:
    def __init__(self, pin, position):
        self.pin = pin
        self.button = GroveButton(pin)
        self.position = position
        self.button.on_press = self.on_press
        self.button.on_release = self.on_release
    def on_press(self,t):
        if (t is None or t >= 0.03) and jeu.partie:
           jeu.signal(self.position)
        elif not(jeu.partie) and self.position == 0:
           jeu.réinitialisation_jeu()        
    def on_release(self,t):
        jeu.leds.setColorRGB(0,0,0,0)    
        jeu.leds.setColorRGB(0,0,0,1)
        jeu.leds.setColorRGB(0,0,0,2)
        jeu.leds.setColorRGB(0,0,0,3)            
                   

jeu = Simon()
while True:
    time.sleep(2)
