#!/usr/bin/python3

import requests 

URL = "https://www.anapioficeandfire.com/api"

def main():

    response = requests.get(URL)

    decode = response.json()

    print(decode)

main()
