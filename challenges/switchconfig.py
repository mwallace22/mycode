#!/usr/bin/python3
import yaml
import os 
import pip._vendor.requests
from pip._vendor import requests
import crayons
def switchStatus():
    with open('switchdata.yaml', 'r') as switches:
        myswitches = yaml.safe_load(switches)
    for switch in myswitches:
        print(crayons.white('There are 3 switches to configure.')
        for command in switch.get('commands'):
            print(f'Sending {command}')
    print("Ctrl + C to quit")

def main():
    try:
        while True:
            switchStatus()

    except KeyboardInterrupt:



main()


