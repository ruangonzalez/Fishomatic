from pyautogui import *
import pyautogui
import time
import keyboard

pyautogui.alert("""             Pressione OK para começar a pescar! 
       pressione 'q' a qualquer momento para parar!""", title="F15H0M4T1C", button="OK")     

def end_game_actions():
    # Clique em receber moedas
    collect_coins_pos = pyautogui.locateOnScreen('collectcoins.png', confidence=0.7)
    if collect_coins_pos is not None:
        pyautogui.click(collect_coins_pos)
        time.sleep(3)
    # Clique em "done"
    done_pos = pyautogui.locateOnScreen('done.png', confidence=0.7)
    if done_pos is not None:
        pyautogui.click(done_pos)
        time.sleep(2)
    # Mova-se para a frente da porta novamente
    pyautogui.moveTo(entrada_da_porta_x, entrada_da_porta_y)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(porta_x, porta_y)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(yes_x, yex_y)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(play_x, play_y)
    pyautogui.click()
    time.sleep(2)
    

regiao_peixes = (850, 380, 150, 500)

entrada_da_porta_x = 1150
entrada_da_porta_y = 500

porta_x = 1150
porta_y = 400

yes_x = 870
yex_y = 550

play_x = 1350
play_y = 800

while not keyboard.is_pressed('q'):
    try:
        fish_pos = pyautogui.locateOnScreen('eyeball.png', region=(regiao_peixes), confidence=0.7)     
        if fish_pos is not None:
            pyautogui.moveTo(fish_pos) 
            pyautogui.moveTo(930,255)  
            pyautogui.click() 
            time.sleep(0.2)
    except ImageNotFoundException: 
        try:
            time.sleep(0.05) 
            game_over_pos = pyautogui.locateOnScreen('game_over.png',region=(670, 270, 600, 650), confidence=0.5)
            if game_over_pos is not None:
                end_game_actions()
            continue       
        except ImageNotFoundException:
            continue              


        