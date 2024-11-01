# Imports go at the top
from microbit import *
import speech
l = ["hello", "i like mango", "i exist", "charger", "I own 40000 double a batteries", "hehehe", "i like trains", "my brother plays roblox", "i have friends"]

# Code in a 'while True:' loop repeats forever
while True:
    z = len(l)
    for i in range(0, z, 1):
        e = l[i]
        speech.say(e)
        sleep(1000)
    
