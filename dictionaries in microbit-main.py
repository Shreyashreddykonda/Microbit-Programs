# Imports go at the top
from microbit import *
import speech
d = {"mango": 20, "banana": 30, "kiwi": 54, "coconut": 23, "lemon": 17}

# Code in a 'while True:' loop repeats forever
while True:
    for i in d.keys():
        speech.say("The value of")
        sleep(125)
        speech.say(i)
        speech.say("is")
        p = d[i]
        p1 = str(p)
        speech.say(p1)
        sleep(1000)

