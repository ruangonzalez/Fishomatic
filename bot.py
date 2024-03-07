from pyautogui import *
import pyautogui
import time
import keyboard

pyautogui.alert("Pressione OK para começar a pescar")    
while not keyboard.is_pressed('q'):
    
    try:
        fish_pos = pyautogui.locateOnScreen('eyeball.png', region=(850, 380, 150, 500), confidence=0.7)       
        if fish_pos is not None:
            pyautogui.moveTo(fish_pos)  
            pyautogui.moveTo(930,255)  
            pyautogui.click() 
            continue  
                           
    except ImageNotFoundException:
    
        time.sleep(0.05) 
    