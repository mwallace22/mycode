#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

def main():
   
    lowerAnimalList = ['cat', 'dog', 'rabbit', 'bird']
    upperAnimalList = []
    upperCase = ''
    for x in lowerAnimalList:
        upperCase = lowerAnimalList[x]
        upperAnimalList.insert(x,upperCase.capitalize())
        
    print(f'Lower Case Animal List: {lowerAnimalList}')
    print(f'Upper Case Animal List: {upperAnimalList}')


main()


