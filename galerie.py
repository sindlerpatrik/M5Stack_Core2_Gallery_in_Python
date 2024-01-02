#přidáme jednotlivé knihovny
from m5stack import *
from m5stack_ui import *
from uiflow import * 
import os

#vytvoříme si list s fotkami z SD karty
Gallery = ["/sd/GALERIE/1.jpg","/sd/GALERIE/2.jpg","/sd/GALERIE/3.jpg","/sd/GALERIE/4.jpg","/sd/GALERIE/5.jpg",
"/sd/GALERIE/6.jpg","/sd/GALERIE/7.jpg","/sd/GALERIE/8.jpg","/sd/GALERIE/9.jpg","/sd/GALERIE/10.jpg",
"/sd/GALERIE/11.jpg","/sd/GALERIE/12.jpg","/sd/GALERIE/13.jpg","/sd/GALERIE/14.jpg","/sd/GALERIE/15.jpg"
]

#nadeklarujeme si proměnné
#index říká kolikátá fotka z galerie se zobrazí na displeji
index = 0
#počet fotek v gelerii
length = len(Gallery)
#nastavení síly vibrace na 10
power.setVibrationIntensity(10)

#vytvoříme si funkce
def photos():
  #načtení fotky z SD karty
  photo = open(Gallery[index]).read()
  #umístění fotky na displej na střed
  lcd.image_buff(lcd.CENTER, lcd.CENTER, photo)

def vibrate_button():
  #tlačítko po zmáčknutí bude vibrovat po dobu 100ms
  power.setVibrationEnable(True)
  wait_ms(100)
  power.setVibrationEnable(False)

#aktivování funkce pro načtení galerie při startu zařízení
photos()

#nekonečná smyčka
while True:
  #když zmáčkeneme levé tlačítko
  if btnA.wasPressed():
    vibrate_button()
    #tak se index zmenší o 1
    index -= 1
    #pokud je index menší než nula
    if (index < 0):
        #tak poté se index bude rovnat počtu fotek minus 1 a zobrazí se poslední fotka z galerie
        index = length-1
    photos()
  
  #když zmáčkeneme třetí tlačítko
  elif btnC.wasPressed():
    vibrate_button()
    #tak se index zvetší o 1
    index += 1
    #pokude se index rovná počtu fotek v galerii
    if (index == length):
        #tak poté se index bude rovnat nule a zobrazí se první fotka z galerie
        index = 0
    photos()
  
  #když zmáčkneme prostřední tlačítko
  elif btnB.wasPressed():
    vibrate_button()
    #tak index se bude rovnat nule a galerie se vrátí na první fotku
    index = 0
    photos()