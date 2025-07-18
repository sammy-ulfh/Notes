#!/usr/bin/env python3

import signal
import sys

from termcolor import colored
from forwardshell import ForwardShell

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa...\n", "red"))
    my_forward_shell.remove_files()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == "__main__":
    my_forward_shell = ForwardShell()
    my_forward_shell.run()
