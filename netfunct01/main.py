#!/usr/bin/env python3


def commandpush(devicemd):

    for ip in devicemd.keys(): 
        print(f'Handshaking. .. ... connecting with {ip}')

        for mycmds in devicemd[ip]:
            print(f'Attempting to sending command --> {mycmds}')

    return None

def main(): 

    devicemd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print('Welcome to the network device command pusher')

    print("\nKData set found\n")

    commandpush(devicemd)

main()

