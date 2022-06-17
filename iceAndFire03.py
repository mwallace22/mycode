#!/usr/bin/python3

import requests

API_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main(): 

    response = requests.get(API_BOOKS)

    decode = response.json()

    for singlebook in decode: 
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        # print ISBN
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")

main()
