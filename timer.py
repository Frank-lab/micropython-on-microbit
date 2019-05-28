from microbit import *
import music
#declear timer
counter = 0


while True:
    if button_a.is_pressed():
        counter += 1
        display.scroll(str(counter), 150)
        
    if button_b.is_pressed():
        for i in range(counter):
            display.show(Image.ALL_CLOCKS, loop=False, delay=1000*5)
            
        display.show(Image.HAPPY)
        music.play(music.RINGTONE)
        
