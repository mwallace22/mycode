#!/usr/bin/python3
import uuid

ticket = uuid.uuid1()

try:
    print('Type the name of the config file to load.')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()
except: 
    x = 'General error!'
else: 
    x = 'Switch config file found.'
finally:
    with open("try04.log", "a") as zlog: 
        print('\n\nWriting results of routine to log file')
        print(ticket, ' - ', x, file=zlog)



