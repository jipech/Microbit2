from microbit import *
while (True):
    if pin0.is_touched():
        display.show("A")
    else:
        display.show("N")
    sleep(100)