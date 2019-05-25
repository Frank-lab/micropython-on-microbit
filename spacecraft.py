from microbit import *
import random
player_x = 2
player_y = 4
enemys = [[random.randint(0, 4), 0]]
hit = 0
press_count = 0
timer = running_time()
bom = 4
bom_timer = running_time()
while True:
    display.clear()
    display.set_pixel(player_x, player_y, bom)
    if button_a.is_pressed():
        player_x = (player_x - 1 + 5) % 5
        press_count += 1
        sleep(90)
    if button_b.is_pressed():
        player_x = (player_x + 1 + 5) % 5
        press_count += 1
        sleep(90)
    if button_a.is_pressed() and button_b.is_pressed():
        if bom > 3:
            bom -= 3
            display.show(Image.SQUARE_SMALL)
            sleep(200)
            display.show(Image.SQUARE)
            sleep(200)
            enemys = [[random.randint(0, 4), 0]]
            press_count = 0
    for enemy in enemys:
        display.set_pixel(enemy[0], enemy[1], 5)
        if enemy[1] == player_y and enemy[0] == player_x:
            hit = 1
            break
    if hit == 1:
        break
    if running_time() - timer > 210:
        timer = running_time()
        for i, enemy in enumerate(enemys):    
            enemy[1] = (enemy[1] + 1 + 5) % 5
            if enemy[1] == 0:
                if i == 0:
                    enemy[0] = player_x
                else:
                    enemy[0] = random.randint(0, 4)
    if running_time() - bom_timer > 3000:
        bom_timer = running_time()
        if bom < 9:
            bom = (bom + 1)
    sleep(40)
    if press_count > 5:
        addone = [random.randint(0, 4), 0]
        enemys.append(addone)
        press_count = 0
for enemy in enemys:
        display.set_pixel(enemy[0], enemy[1], 5)
display.set_pixel(player_x, player_y, bom)
sleep(1500) 
display.scroll(int(running_time() / 100))    
