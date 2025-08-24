from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard
import time


flag = False
def on_press(key):
    global flag
    if key == keyboard.Key.f2:
        flag = True

def on_release(key):
    global flag
    if key == keyboard.Key.esc:
        flag = False
        
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
controller = keyboard.Controller()
print("This code is made by Abishek Ganesh")
print("To know How to use, click 'More-info'")
print("Version: 0.00.01(Alpha) \n")
print("===========================================")
word = input("Word: ")
b = eval(input("Time: "))


listener.start()

while True:
    while flag:
        controller.type(word)
        controller.press(Key.enter) 
        controller.release(Key.enter)
        time.sleep(b)

#while True:
    #while flag:
        #controller.type(word)
        #controller.press(Key.enter)
        #controller.release(Key.enter)
        #time.sleep(b)
