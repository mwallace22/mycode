#!/usr/bin/python3

import pprint
import requests

API_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():

    response = requests.get(API_BOOKS)

    decode = response.json()

    pprint.pprint(decode)

main()

