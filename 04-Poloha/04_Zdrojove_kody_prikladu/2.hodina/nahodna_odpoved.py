from microbit import *
import random

answers = [
    "Jiste",
    "Urcite",
    "Bez obav",
    "Ano, ano, ano",
    "Uvidime, uvidime",
    "Pravdepodobne",
    "To vypada dobre",
    "Ano",
    "Zeptej se pozdeji",
    "Ted nevim",
    "Nelze urcit",
    "Radeji ne",
    "Me vnitrni ja rika ne",
    "Urcite ne",
    "Ne",
    "Nikdy",
]

while True:
    display.show('8')
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))
    sleep(10)