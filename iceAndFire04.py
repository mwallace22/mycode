#!/usr/bin/python3
import requests
import pprint

API_BOOKS = "https://www.anapioficeandfire.com/api/characters/"

def main(): 

    charLookup = input("Pick a number between 1 and 1000: ")

    response = requests.get(API_BOOKS + charLookup)

    decode = response.json()
    pprint.pprint(decode)

main()
