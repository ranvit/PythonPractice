import random
secret = random.randint(1,100)
print('I am thinking of a number between 1 and 20.')
print('Take a guess.')
count = 1
guess = int(input())
while(guess != secret):

    count += 1

    if(guess < secret):
        print('Your guess is too low.')
    elif(guess > secret):
        print('Your guess is too high.')
        
    print('Take a guess.')

    guess = int(input())

print('Good job! You guessed my number in ' + str(count) + ' guesses!')
