#!/usr/bin/env python3

import argparse
import subprocess
import signal
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa...\n", "red"))
    exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    argparser = argparse.ArgumentParser(description="Fast ICMP Scanner")
    argparser.add_argument("-t", "--target", dest="target", required=True, help="Individual target or range of targets to scan. (Ex: 192.168.1.1 or 192.168.1.1-100)")

    arguments = argparser.parse_args()

    return arguments.target

def parse_target(target_str):
    
    # 192.168.1.1-100
    target_splitted = target_str.split('.') # ["192", "168", "1", "1-100"]
    first_three_octets = '.'.join(target_splitted[:3]) # "192.168.1"

    if len(target_splitted) == 4:
        if '-' in target_splitted[3]:
            start, end = target_splitted[3].split('-')
            return [f"{first_three_octets}.{i}" for i in range(int(start), int(end)+1)]
        else:
            return [target_str]
    else:
        print(colored("\n[!] Invalid Format.\n", "red"))

def host_discovery(target):
    try:
        ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

        if ping.returncode == 0:
            print(colored(f"\t[i] IP {target} - Active", "green"))
    except subprocess.TimeoutExpired:
        pass

def main():
    target_str = get_arguments()
    targets = parse_target(target_str)

    print(colored("\n[+] Descubriendo Hosts Activos...\n", "yellow"))
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(host_discovery, targets)

if __name__ == "__main__":
    main()
