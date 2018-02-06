import random

count = 1
secret = random.randint(1, 10)
guess = secret + 1
while guess != secret and count <= 3:
    guess = int(input('Enter your guess: \n'))
    if guess > secret:
        print('Guess lower')
        count += 1
    elif guess < secret:
        print('Guess higher')
        count += 1
    else:
        print('Bingo')
print('Done')
