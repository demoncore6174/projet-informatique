import time
import random
from grove.grove_led import GroveLed
from grove.grove_button import GroveButton
from grove.chainable_led import ChainableLED

class Simon:
    def __init__(self):
        self.score = 0
        self.niveau = 1
        self.pseudo = ""
        self.sequence = []
        self.level = 1
        self.sequence = 4
        self.boutton = [Boutton(16,0), Boutton(18,1), Boutton(24,2), Boutton(26,3)]
        self.leds = ChainableLED(6, 5, 4)
        self.jeu()
    def jeu(self):
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
      
    def signal(self,emplacement):
        if self.sequence[0] == emplacement:
            print("bien joué")
            self.sequence.remove(emplacement)
            if len(self.sequence) == 0:
                print("gagné")
                self.gagne_level()
        else:
            print("perdu")
    def gagne_level(self):
        self.score += 200 * self.level
        self.level += 1
        self.sequence = 4 + (self.level //3)
        print("Level", self.level, ":")
        time.sleep(1)
        self.jeu()
                
              


class Boutton:
    def __init__(self, pin, position):
        self.pin = pin
        self.button = GroveButton(pin)
        self.position = position
        self.button.on_press = self.on_press
    def on_press(self,t):
        if t is None or t >= 0.03:
           jeu.signal(self.position)


jeu = Simon()
while True:
    time.sleep(2)
