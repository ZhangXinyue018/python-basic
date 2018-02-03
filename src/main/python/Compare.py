number = 23
guess = int(input('Enter Integer: '))
if guess == number:
    print("=")
elif guess < number:
    print("<")
else:
    print(">")
print("done")