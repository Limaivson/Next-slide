import keyboard
import client
from time import sleep

def next(e) -> None:
    print('Next slide')
    client.send(command='next')

def prev(e):
    print('Prev slide')
    client.send(command='prev')

condition = False
print('-> = next | <- = prev | s = exit')

def exit(e):
    global condition
    condition = True

keyboard.on_press_key('s', exit)
keyboard.on_press_key('right', next)
keyboard.on_press_key('left', prev)

while not condition:
    keyboard.wait('s')