#!/usr/bin/env python3

warning = ''

# Get the windspeed in mph
windSpeed = int(input("What is the sustatined wind speed?"))

# Evaluate the windspeed conditions and change warning message
if windSpeed >= 75 and windSpeed <= 95:
    warning = 'This is a category 1 hurricane. Very dangerous winds will produce some damage.'
elif windSpeed >=96 and windSpeed <=110:
    warning = 'This is a category 2 hurricane. Extremely dangerous winds will cause extensive damage.'
elif windSpeed >= 111 and windSpeed <=129:
    warning = 'This is a category 3 hurricane. Devastating damage will occur.'
elif windSpeed >= 130 and windSpeed <=156: 
    warning = 'This is a category 4 hurricane. Catastraphic damage will occur.'
elif windSpeed >= 157: 
    warning = 'This is a category 5 hurricane. GET OUT OF THERE!.'
else:
    warning = 'Tropical storm or lower. Go about your day.'
print(warning)

