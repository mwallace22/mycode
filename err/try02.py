
#!/usr/bin/python3

while True: 
    try: 
        print("Let's divide x by y!")
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        print('The value of x/y: ', x/y)
    except ZeroDivisionError as zerr:
        print('Handling run-time error:', zerr)
    except Exception as err:
        print('We did not anticipate that: ', err)


