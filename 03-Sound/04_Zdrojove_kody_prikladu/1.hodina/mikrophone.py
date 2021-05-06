from microbit import *
display.clear()
microphone.set_threshold(SoundEvent.LOUD, 10)

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()
 