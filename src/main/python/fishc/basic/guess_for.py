for i in range(1, 4):
    guess = int(input('Enter your guess: \n'))
    if guess > 8:
        print('Guess lower')
    elif guess < 8:
        print('Guess higher')
    else:
        print('Bingo')
        break;
print('Done')