running = True
number = 23
while running:
    inputNumber = int(input('Enter a number: '))
    if inputNumber == number:
        running = False
        print('=')
    elif inputNumber < number:
        print('Enter Higher')
    else:
        print('Enter Lower')
else:
    print('End of Loop')
print('Done')