from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard
import time


flag = False
guide = False

def on_press(key):
    global flag
    global guide
    if key == keyboard.Key.f2:
        flag = True
    elif key == keyboard.Key.f4:
        guide = True


def on_release(key):
    global flag
    global guide
    if key == keyboard.Key.esc:
        flag = False
        
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
controller = keyboard.Controller()


    
l = input("Loop Type: ")
w = input("Text: ")
t = float(input("Time-Space: "))




listener.start()

if l == "C" or l == "c":
    while True:
        while flag:
            controller.type(w)
            time.sleep(0.1)

            time.sleep(t)
            

elif l == "L" or l == "l":
    RT = int(input("Repeating Limits: "))
    i = 0
    while True:
        if i == RT:
            break
        else:
            while flag:
                if i == RT :
                    break
                else:
                    controller.type(w)
                    time.sleep(0.1)

                    time.sleep(t)
                    i +=1
                
        
    
    


