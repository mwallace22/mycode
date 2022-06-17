#!/usr/bin/python3

import re
import urllib.request

def main():

    print('Where should we search?')
    url = input('> ')

    print(f"Open this URL {url} to search for the phrase: ")
    searchFor = input("> ")

    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    if re.search(searchFor, searchMe):
        print("Found a Match")

    else: 
        print("No match")

main()
